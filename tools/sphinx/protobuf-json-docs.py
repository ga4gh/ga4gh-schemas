#!/usr/bin/env python

import sys
import collections

from google.protobuf.compiler import plugin_pb2 as plugin
import itertools
import json
from google.protobuf.descriptor_pb2 import DescriptorProto, EnumDescriptorProto, EnumValueDescriptorProto, FieldDescriptorProto

def convert_protodef_to_editable(proto):
    class Editable(object):
        def __init__(self, prot):
            self.kind = type(prot)
            self.name = prot.name
            self.comment = ""
            if isinstance(prot, EnumDescriptorProto):
                self.value = [convert_protodef_to_editable(x) for x in prot.value]
            elif isinstance(prot, DescriptorProto):
                self.field = [convert_protodef_to_editable(x) for x in prot.field]
            elif isinstance(prot, EnumValueDescriptorProto):
                self.number = prot.number
            elif isinstance(prot, FieldDescriptorProto):
                self.type = prot.type
            else:
                raise Exception, type(prot)

    return Editable(proto)

def traverse(proto_file):

    def _collapse_comments(comments):
        return (comments["leading_comments"] + comments["trailing_comments"]).strip()

    def _traverse(package, items, tree):
        for item_index, item in enumerate(items):
            item = convert_protodef_to_editable(item)
            if item_index in tree:
                comments = tree[item_index]
                if "leading_comments" in comments or "trailing_comments" in comments:
                    item.comment = _collapse_comments(comments)
                    #raise Exception, item.__dict__
                    del comments["leading_comments"]
                    del comments["trailing_comments"]
                if item.kind is EnumDescriptorProto:
                    if 2 in comments: # value in EnumDescriptorProto
                        for k in comments[2]:
                            value_comment = comments[2][k]
                            if value_comment != {}:
                                item.value[k].comment = _collapse_comments(value_comment)
                elif item.kind is DescriptorProto:
                    if 2 in comments: # field in DescriptorProto
                        for k in comments[2]:
                            field_comment = comments[2][k]
                            if field_comment != {}:
                                item.field[k].comment = _collapse_comments(field_comment)
                else:
                    raise Exception, item.kind

            yield item, package

            if isinstance(item, DescriptorProto):
                for enum in item.enum_type:
                    yield enum, package

                for nested in item.nested_type:
                    nested_package = package + item.name

                    for nested_item in _traverse(nested, nested_package):
                        yield nested_item, nested_package

    import pprint
    open("dump", "w").write(pprint.pformat(proto_file.source_code_info))

    tree = collections.defaultdict(collections.defaultdict)
    for loc in proto_file.source_code_info.location:
        if loc.leading_comments or loc.trailing_comments or loc.leading_detached_comments:
            place = tree
            for p in loc.path:
                if not place.has_key(p):
                    place[p] = collections.defaultdict(collections.defaultdict)
                place = place[p]
            place["leading_comments"] = loc.leading_comments
            place["trailing_comments"] = loc.trailing_comments
            place["leading_detached_comments"] = loc.leading_detached_comments

    if set(tree.keys()).difference(set([4,5,12])) != set():
        raise Exception, sorted(tree.keys())

    return {"types":
        itertools.chain(
            _traverse(proto_file.package, proto_file.enum_type, tree[5]), # 5 is enum_type in FileDescriptorProto
            _traverse(proto_file.package, proto_file.message_type, tree[4]), # 4 is enum_type in FileDescriptorProto
        ),
        "file": tree[12]
    }

def generate_code(request, response):
    for proto_file in request.proto_file:
        types = []

        results = traverse(proto_file)
        for item, package in results["types"]:
            data = {
                'name': item.name,
                'doc': item.comment
            }

            if item.kind == DescriptorProto:
                data.update({
                    'type': 'message',
                    'fields': []
                })
                for f in item.field:
                    if f.type in [1]:
                        kind = "double"
                    elif f.type in [3]:
                        kind = "long"
                    elif f.type in [5]:
                        kind = "integer"
                    elif f.type in [8]:
                        kind = "boolean"
                    elif f.type in [9]:
                        kind = "string"
                    elif f.type in [11]:
                        kind = "message"
                    elif f.type in [12]:
                        kind = "bytes"
                    elif f.type in [14]:
                        kind = "enum"
                    else:
                        raise Exception, f.type
                    data["fields"].append({
                        'name': f.name,
                        'type': kind,
                        'doc': f.comment
                        })

            elif item.kind == EnumDescriptorProto:
                comments = ["\n* `%s`: %s"%(v.name, v.comment) for v in item.value]
                data.update({
                    'type': 'enum',
                    'symbols': [v.name for v in item.value]
                })
                data["doc"] += " ".join(comments)

            types.append(data)

        if results["file"].has_key("leading_detached_comments"):
            comments = "".join(results["file"]["leading_detached_comments"])
        else:
            comments = ""
        output = {
            "types": types,
            "protocol": proto_file.name.split("/")[-1].split(".")[0],
            'doc': comments,
            "namespace": proto_file.package,
        }

        # Fill response
        f = response.file.add()
        f.name = proto_file.name + '.json'
        f.content = json.dumps(output, indent=2)


if __name__ == '__main__':
    # Read request message from stdin
    data = sys.stdin.read()

    # Parse request
    request = plugin.CodeGeneratorRequest()
    request.ParseFromString(data)

    # Create response
    response = plugin.CodeGeneratorResponse()

    # Generate code
    generate_code(request, response)

    # Serialise response message
    output = response.SerializeToString()

    # Write to stdout
    sys.stdout.write(output)
