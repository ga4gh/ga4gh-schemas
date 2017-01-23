#!/usr/bin/env python

"""
Authors: Malisa Smith, Adam Novak, David Steinberg

Plugin for generating a UML diagram of the GA4GH schema.
The resulting png file is then used in RST files to create Sphinx documentation.

Usage:
    protoc --plugin=protoc-gen-custom=<script path>/protobuf-uml.py --custom_out=<uml dir> <proto file(s)>
"""

import sys, os
from google.protobuf.compiler import plugin_pb2 as plugin
from graphviz import Source

# Check the message to see if it is a trivial map.
def is_trivial_map(nested_type):
    # Define a trivial map to be a message with a nested_type.name
    # that ends in "Entry" with two fields, "key" and "value". The
    # "value" field has a type that is not 11 (and a list) or 14.
    if nested_type.name.endswith("Entry") and len(nested_type.field) == 2 and nested_type.field[0].name == "key" and nested_type.field[1].name == "value" and not ((nested_type.field[1].type == 11 and not nested_type.field[1].type_name == ".google.protobuf.ListValue") or nested_type.field[1] == 14):
        return True
    else:
        return False

# Parse a message. Pass in all the dictionaries to be updated, as well
# as the relevant message Parse the name, field, nested_type, and
# enum_type fields in DescriptorProto:
# https://github.com/google/protobuf/blob/master/src/google/protobuf/descriptor.proto#L92
def parse_message(cluster, fields, containments, nests, id_targets, id_references, clusters, message, message_index=None):
    # Track all the fields in the message
    fields[message.name] = []

    for field_index in range(0, len(message.field)):
        field = message.field[field_index]
        fields[message.name].append((field.name, field.type))
        # Deal with containments, id_targets, and id_references, if
        # applicable.  Containments are signified by a field.type
        # of 11 (for TYPE_MESSAGE) or 14 (for TYPE_ENUM). The type of
        # containment can be determined by looking at field.type_name.
        # Maps will also come up as type 11 and will have a
        # field.type_name of something like
        # .ga4gh.Feature.AttributesEntry, where the actual field name
        # is attributes
        if field.type == 11 or field.type == 14:
            # We are likely adding containments of trivial maps,
            # e.g. ('VariantCallEffect', 'InfoEntry', 'info'). But the
            # edge is only drawn if the map/message itself is not a
            # trivial map. When drawing containment edges, the program
            # checks if the field type_name is a key in the fields
            # dictionary.
            containments.add((message.name, field.type_name.split(".")[-1], field.name))
        # id_targets are simply fields where field.name is "id"
        if field.name.lower() == "id":
            id_targets[message.name.lower()] = (message.name, field.name.lower().split(".")[-1])
        # id_references are fields which end in id or ids
        elif field.name.lower().endswith("id") or field.name.lower().endswith("ids"):
            if field.name.lower().endswith("id"):
                destination = field.name.lower()[0:-2]
            elif field.name.lower().endswith("ids"):
                destination = field.name.lower()[0:-3]
            destination = destination.replace("_", "")
            id_references.add((message.name, destination, field.name))

    for nested_type in message.nested_type:
        # Nested messages can be defined without actually using it in
        # a field in the outer message. So, a nested_type is not
        # necessarily used in a field.

        # Note: according to
        # https://developers.google.com/protocol-buffers/docs/proto#backwards-compatibility
        # maps are sent as messages (not map-types) "on the wire". We
        # don't want to draw nodes for nested types that are trivial
        # maps of string to string.  So, check if we want to process
        # the nested_type further:
        if not is_trivial_map(nested_type):
            # The nested_type is nested within the message.
            # Nested_type is itself a message, so recursively call
            # this function.
            parse_message(cluster, fields, containments, nests, id_targets, id_references, clusters, nested_type)

    for enum_type in message.enum_type: # A nested Enum
        # Define it as a top-level type. So it has a fields entry.
        fields[enum_type.name] = []
        for field in enum_type.value:
            fields[enum_type.name].append((field.name, 9))
        # Finally, add it to the cluster
        clusters[cluster.name].append(enum_type.name)

    # Add the name of the message as a type in the current cluster
    clusters[cluster.name].append(message.name)

def parse_cluster(cluster, fields, containments, nests, id_targets, id_references, clusters):
    cluster_name = cluster.name
    if cluster_name.endswith("google/protobuf/struct.proto") or cluster_name.endswith("google/api/http.proto") or cluster_name.endswith("google/protobuf/descriptor.proto"):
        pass
    else:
        clusters[cluster_name] = []

        # process all the enum-types in the cluster
        for enum in cluster.enum_type:
            # Track all the enum "fields"
            fields[enum.name] = []
            for field in enum.value:
                # An Enum field is a string. field types in
                # DescriptorProto uses 9 for TYPE_STRING
                fields[enum.name].append((field.name, 9))
            # Record the name of the enum as a type in the current cluster
            clusters[cluster.name].append(enum.name)

        # Track all the message-types in the cluster
        for message_index in range(0, len(cluster.message_type)):
            message = cluster.message_type[message_index]
            # Recursively parse each message
            parse_message(cluster, fields, containments, nests, id_targets, id_references, clusters, message, message_index)
            # Note: the message will add itself to the cluster

def write_graph(fields, containments, nests, matched_references, clusters):

    # Start a digraph
    graph = "digraph UML {\n"

    # Set the image's size, in inches
    graph += "size= \"33,33\";\n"

    # Add a title
    graph += "labelloc=\"t\";\n"
    graph += "label=<<FONT POINT-SIZE=\"45\">GA4GH Schema Diagram</FONT>>;\n"

    # Define node properties: shaped like UML items.
    graph += "node [\n"
    graph += "\tshape=plaintext\n"
    graph += "]\n\n"

    # Draw each node/type/record as a table
    for type_name, field_list in fields.items():

        graph += "{} [label=<\n".format(type_name)
        graph += "<TABLE BORDER='0' CELLBORDER='1' CELLSPACING='0' CELLPADDING='4' bgcolor='#002060' color='#002060'>\n"
        graph += "\t<TR>\n"
        graph += "\t\t<TD COLSPAN='2' bgcolor='#79A6FF' border='3'><FONT POINT-SIZE='20' color='white'>{}</FONT>".format(type_name)

        graph += "</TD>\n"
        graph += "\t</TR>\n"

        # Now draw the rows of fields for the type. A field_list of
        # [a, b, c, d, e, f, g] will have [a, e] in row 1, [b, f] in
        # row 2, [c, g] in row 3, and just [d] in row 4
        num_fields = len(field_list)
        for i in range(0, num_fields//2 + num_fields%2):
            # Draw one row.
            graph += "\t<TR>\n"
            # Port number and displayed text will be the i'th field's
            # name
            graph += "\t\t<TD align='left' port='{}'><FONT color='white'>- {}</FONT></TD>\n".format(field_list[i][0], field_list[i][0])
            if (num_fields%2) == 1 and (i == num_fields//2 + num_fields%2 - 1):
                # Don't draw the second cell in the row if you have an
                # odd number of fields and it is the last row
                pass
            else:
                graph += "\t\t<TD align='left' port='{}'><FONT color='white'>- {}</FONT></TD>\n".format(field_list[num_fields//2 + num_fields%2 + i][0], field_list[num_fields//2 + num_fields%2 + i][0])
            graph += "\t</TR>\n"

        # Finish the table
        graph += "</TABLE>>];\n\n"

    # Now define the clusters/subgraphs
    for cluster_name, cluster_types in clusters.items():
        graph += "subgraph cluster_{} {{\n".format(cluster_name.replace(".", "_").replace("/", "_"))
        graph += "\tstyle=\"rounded, filled\";\n"
        graph += "\tcolor=lightgrey;\n"
        graph += "\tnode [style=filled,color=white];\n"
        graph += "\tlabel = \"{}\";\n".format(cluster_name.replace(".", "_"))

        # After all the cluster formatting, define the cluster types
        for cluster_type in cluster_types:
            # cluster_type should match up with a type_name from fields
            graph += "\t{};\n".format(cluster_type)
        graph += "}\n\n"

    # Define edge properties for containments
    graph += "edge [\n"
    graph += "\tdir=both\n"
    graph += "\tarrowtail=odiamond\n"
    graph += "\tarrowhead=none\n"
    graph += "\tcolor=\"#C55A11\"\n"
    graph += "\tpenwidth=2\n"
    graph += "]\n\n"

    for container, containee, container_field_name in containments:
        # Now do the containment edges
        # Only write the edge if the containee is a top-level field in fields.
        if containee in fields:
            graph += "{}:{}:w -> {}\n".format(container,
                                                    container_field_name, containee)

    # Define edge properties for references
    graph += "\nedge [\n"
    graph += "\tdir=both\n"
    graph += "\tarrowtail=none\n"
    graph += "\tarrowhead=vee\n"
    graph += "\tstyle=dashed\n"
    graph += "\tcolor=\"darkgreen\"\n"
    graph += "\tpenwidth=2\n"
    graph += "]\n\n"

    for referencer, referencer_field, referencee in matched_references:
        # Now do the reference edges
        graph += "{}:{}:w -> {}:id:w\n".format(referencer, referencer_field,
            referencee)

    # Close the digraph off.
    graph += "}\n"
    graph = graph.replace("\n", " ").replace("\t", " ")

    src = Source(graph, format='svg')
    src.render('_build/generated_images/schema_uml')

def parse_descriptor(request):

    # Holds the fields for each type, as lists of tuples of (name,
    # type), indexed by type. All types are fully qualified.
    fields = {}

    # Holds edge tuples for containment from container to contained.
    containments = set()

    # Holds edge tuples for nested type edges, from parent type to
    # nested type.
    nests = set()

    # Holds a dictionary from lower-case short name to fully-qualified
    # name for everything with an "id" field. E.g. if Variant has an
    # id, then key is "variant" and value is "Variant"
    id_targets = {}

    # Holds a set of tuples of ID references, (fully qualified name of
    # referencer, lower-case target name)
    id_references = set()

    # Holds the field names from each original .proto file, in order
    # to draw one cluster of fields for each file
    # Key: cluster/file name     Value: tuple of field names
    clusters = {}

    for cluster in request.proto_file:
        parse_cluster(cluster, fields, containments, nests, id_targets, id_references, clusters)

    # Now match the id references to targets. Tuples of strings,
    # i.e. (referencer, referencer_field, referencee)
    matched_references = set()
    for id_reference in id_references:
        if id_reference[1] in id_targets:
            matched_references.add((id_reference[0], id_reference[2], id_targets[id_reference[1]][0]))

    return (fields, containments, nests, matched_references, clusters)

def generate_code(request):
    (fields, containments, nests, matched_references, clusters) = parse_descriptor(request)
    write_graph(fields, containments, nests, matched_references, clusters)

if __name__ == '__main__':
    # Read request message from stdin
    data = sys.stdin.read()

    # Parse request
    request = plugin.CodeGeneratorRequest()
    request.ParseFromString(data)

    # Generate code
    generate_code(request)
