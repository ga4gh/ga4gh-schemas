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
        return comments["leading_comments"] + comments["trailing_comments"]

    def _traverse(package, items, tree):
        for item_index, item in enumerate(items):
            item = convert_protodef_to_editable(item)
            if item_index in tree:
                comments = tree[item_index]
                if "leading_comments" in comments or "trailing_comments" in comments:
                    item.comments = _collapse_comments(comments)
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

    tree = collections.defaultdict(collections.defaultdict)
    for loc in proto_file.source_code_info.location:
        if loc.leading_comments or loc.trailing_comments:
            place = tree
            for p in loc.path:
                if not place.has_key(p):
                    place[p] = collections.defaultdict(collections.defaultdict)
                place = place[p]
            place["leading_comments"] = loc.leading_comments
            place["trailing_comments"] = loc.trailing_comments

    return itertools.chain(
        _traverse(proto_file.package, proto_file.enum_type, tree[5]), # 5 is enum_type in FileDescriptorProto
        _traverse(proto_file.package, proto_file.message_type, tree[4]), # 4 is enum_type in FileDescriptorProto
    )

def generate_code(request, response):
    for proto_file in request.proto_file:
        output = []

        # Parse request
        for item, package in traverse(proto_file):
            data = {
                'package': proto_file.package or '&lt;root&gt;',
                'filename': proto_file.name,
                'name': item.name,
                'doc': item.comment
            }

            if item.kind == DescriptorProto:
                data.update({
                    'type': 'Message',
                    'properties': [{
                        'name': f.name,
                        'type': int(f.type),
                        'doc': f.comment
                        }
                        for f in item.field]
                })

            elif item.kind == EnumDescriptorProto:
                data.update({
                    'type': 'Enum',
                    'values': [{
                        'name': v.name,
                        'value': v.number,
                        'doc': v.comment}
                       for v in item.value]
                })

            output.append(data)

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
