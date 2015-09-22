#!/usr/bin/env python2.7
"""
avpr2uml.py: make UML diagrams from Avro AVPR files (which you can easily
generate from AVDL files). Inclusion of other types will be detected and turned
into the appropriate UML edges. ID references will be created if the referencee
has an "id" field, and the referencer has a referenceeNameId(s) field. Some
attempt is made to fuzzy-match referencers to referencees, but it is not perfect
and may require manual adjustment of the resulting edges.

Re-uses sample code and documentation from
<http://users.soe.ucsc.edu/~karplus/bme205/f12/Scaffold.html>
"""

import argparse, sys, os, itertools, re, json

def parse_args(args):
    """
    Takes in the command-line arguments list (args), and returns a nice argparse
    result with fields for all the options.
    Borrows heavily from the argparse documentation examples:
    <http://docs.python.org/library/argparse.html>
    """

    # The command line arguments start with the program name, which we don't
    # want to treat as an argument for argparse. So we remove it.
    args = args[1:]

    # Construct the parser (which is stored in parser)
    # Module docstring lives in __doc__
    # See http://python-forum.com/pythonforum/viewtopic.php?f=3&t=36847
    # And a formatter class so our examples in the docstring look good. Isn't it
    # convenient how we already wrapped it to 80 characters?
    # See http://docs.python.org/library/argparse.html#formatter-class
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    # Now add all the options to it
    parser.add_argument("avprs", type=argparse.FileType("r"), nargs="+",
        help="the AVPR file(s) to read")
    parser.add_argument("--dot", type=argparse.FileType("w"),
        help="GarphViz file to write a UML diagram to")

    return parser.parse_args(args)

def type_to_string(parsed_type, namespace=None, strip_namespace=False):
    """
    Given the JSON representation of a field type (a string naming an Avro
    primitive type, a string naming a qualified user-defiend type, a string
    naming a non-qualified user-defined type, a list of types being unioned
    together, or a dict with a "type" of "array" or "map" and an "items"
    defining a type), produce a string defining the type relative to the given
    namespace.

    If strip_namespace is specified, namespace info will be stripped out.

    """

    if isinstance(parsed_type, list):
        # It's a union. Recurse on each unioned element.
        return ("union<" + ",".join([type_to_string(x, namespace,
            strip_namespace) for x in parsed_type]) + ">")
    elif isinstance(parsed_type, dict):
        # It's an array or map.

        if parsed_type["type"] == "array":
            # For an array we recurse on items
           recurse_on = parsed_type["items"]
        elif parsed_type["type"] == "map":
            # For a map, we recurse on values.
            recurse_on = parsed_type["values"]
        else:
            # This is not allowed to be a template.
            raise RuntimeError("Invalid template {}".format(
                parsed_type["type"]))

        return (parsed_type["type"] + "<" +
            type_to_string(recurse_on, namespace, strip_namespace) + ">")
    elif parsed_type in ["int", "long", "string", "boolean", "float", "double",
        "null", "bytes"]:
        # If it's a primitive type, return it.
        return parsed_type
    elif "." in parsed_type:
        # It has a dot, so assume it's fully qualified. TODO: Handle partially
        # qualified types, where we have to check if this type actually exists.

        parts = parsed_type.split(".")

        parsed_namespace = ".".join(parts[:-1])

        if strip_namespace or parsed_namespace == namespace:
            # Pull out the namespace, sicne we don't want/don't need it
            parsed_type = [-1]

        return parsed_type
    else:
        # Just interpret it in our namespace. Don't fully qualify it.

        # Then give back the type name
        return parsed_type

def find_user_types(parsed_type, namespace=None):
    """
    Given the JSON representation of a field type (a string naming an Avro
    primitive type, a string naming a qualified user-defiend type, a string
    naming a non-qualified user-defined type, a list of types being unioned
    together, or a dict with a "type" of "array" or "map" and an "items"
    defining a type), yield all of the user types it references.

    """

    if isinstance(parsed_type, list):
        # It's a union.
        for option in parsed_type:
            # Recurse on each unioned element.
            for found in find_user_types(option, namespace):
                # And yield everything we find there.
                yield found
    elif isinstance(parsed_type, dict):
        # It's an array or map.

        if parsed_type["type"] == "array":
            # For an array we recurse on items
           recurse_on = parsed_type["items"]
        elif parsed_type["type"] == "map":
            # For a map, we recurse on values.
            recurse_on = parsed_type["values"]
        else:
            # This is not allowed to be a template.
            raise RuntimeError("Invalid template {}".format(
                parsed_type["type"]))

        for found in find_user_types(recurse_on, namespace):
            # Yield everything we find in there.
            yield found
    elif parsed_type in ["int", "long", "string", "boolean", "float", "double",
        "null", "bytes"]:
        # If it's a primitive type, skip it.
        pass
    elif "." in parsed_type:
        # It has a dot, so assume it's fully qualified. TODO: Handle partially
        # qualified types, where we have to check if this type actually exists.
        yield parsed_type
    else:
        # Just interpret it in our namespace.

        if namespace is not None:
            # First attach the namespace if applicable.
            parsed_type = "{}.{}".format(namespace, parsed_type)

        # Then give back the type name
        yield parsed_type

def type_to_node(type_name):
    """
    Convert an Avro type name (with dots) to a GraphViz node identifier.

    """

    # First double underscores
    type_name = type_name.replace("_", "__")
    # Then turn dots into underscores
    type_name = type_name.replace(".", "_")

    return type_name

def type_to_display(type_name):
    """
    Convert an Avro fully qualified type name (with dots) to a display name.

    """

    # Get the thing after the last dot, if any.
    return type_name.split(".")[-1]

def dot_escape(label_content):
    """
    Escape the given string so it is safe inside a GraphViz record label. Only
    actually handles the caharcters found in Avro type definitions, so not
    general purpose.

    """

    return (label_content.replace("&", "&amp;").replace("<", "&lt;")
        .replace(">", "&gt;").replace("\"", "&quot;"))

def parse_avprs(avpr_files):
    """
    Given an iterator of AVPR file objects to read, return three things: a dict
    from fully qualified type names to lists of (field name, field type) tuples,
    and a set of (container, containee) containment tuples, and a set of
    (referencer, referencee) ID reference tuples.

    """

    # Holds the fields for each type, as lists of tuples of (name, type),
    # indexed by type. All types are fully qualified.
    fields = {}

    # Holds edge tuples for containment from container to contained.
    containments = set()

    # Holds a dict from lower-case short name to fully-qualified name for
    # everything with an "id" field.
    id_targets = {}

    # Holds a set of tuples of ID references, (fully qualified name of
    # referencer, lower-case target name)
    id_references = set()

    for avpr_file in avpr_files:
        # Load each protocol that we want to look at.
        protocol = json.load(avpr_file)

        # Grab the namespace if set
        protocol_namespace = protocol.get("namespace", None)

        for defined_type in protocol.get("types", []):
            # Get the name of the type
            type_name = defined_type["name"]

            type_namespace = defined_type.get("namespace", protocol_namespace)

            if type_namespace is not None:
                type_name = "{}.{}".format(type_namespace, type_name)

            if fields.has_key(type_name):
                # Already saw this one.
                continue

            # Record this one as actually existing.
            fields[type_name] = []

            print("Type {}".format(type_name))

            if defined_type["type"] == "record":
                # We can have fields.

                for field in defined_type["fields"]:
                    # Parse out each field's name and type
                    field_type = type_to_string(field["type"], type_namespace)
                    field_name = field["name"]

                    # Announce every field with its type
                    print("\t{} {}".format(field_type, field_name))

                    # Record the field for the UML.
                    fields[type_name].append((field_name, field_type))

                    for used in find_user_types(field["type"], type_namespace):
                        # Announce all the user types it uses
                        print("\t\tContainment of {}".format(used))

                        # And record them
                        containments.add((type_name, used))

                    if (field_name.lower() == "id" and
                        u"string" in field_type):

                        # This is a possible ID target. Decide what we would
                        # expect to appear in an ID reference field name.
                        target_name = type_to_display(type_name).lower()

                        if id_targets.has_key(target_name):
                            # This target is ambiguous.
                            id_targets[target_name] = None
                            print("WARNING: ID target {} exists twice!")
                        else:
                            # Say it points here
                            id_targets[target_name] = type_name

                        print("\t\tFound ID target {}".format(target_name))

                    elif (field_name.lower().endswith("id") or
                        field_name.lower().endswith("ids")):
                        # This is probably an ID reference

                        if field_name.lower().endswith("id"):
                            # Chop off exactly these characters
                            destination = field_name.lower()[0:-2]
                        elif field_name.lower().endswith("ids"):
                            # Chop off these instead. TODO: this is super ugly
                            # and regexes are better.
                            destination = field_name.lower()[0:-3]

                        # Announce and save the reference
                        print("\t\tFound ID reference to {}".format(
                            destination))
                        id_references.add((type_name, destination))

    # Now we have to match ID references to targets. This holds the actual
    # referencing edges, as (from, to) fully qualified name tuples.
    references = set()

    for from_name, to_target in id_references:
        # For each reference

        if id_targets.has_key(to_target):
            # We point to something, what is it?
            to_name = id_targets[to_target]

            if to_name is None:
                # We point to something that's ambiguous
                print("WARNING: Ambiguous target {} used by {}!".format(
                    to_target, from_name))
            else:
                # We point to a real thing. Add the edge.
                print("Matched reference from {} to {} exactly".format(
                    from_name, to_name))
                references.add((from_name, to_name))

        else:
            # None of these targets matches exactly
            print("WARNING: {} wanted target {} but it does not exist!".format(
                from_name, to_target))

            # We will find partial matches, and save them as target, full name
            # tuples.
            partial_matches = []

            for actual_target, to_name in id_targets.iteritems():
                # For each possible target, see if it is a partial match
                if (actual_target in to_target or
                    to_target in actual_target):

                    partial_matches.append((actual_target, to_name))

            if len(partial_matches) == 1:
                # We found exactly one partial match. Unpack it!
                actual_target, to_name = partial_matches[0]

                # Announce and record the match
                print("WARNING: Matched reference from {} to {} on partial "
                    "match of {} and {}".format(from_name, to_name, to_target,
                    actual_target))
                references.add((from_name, to_name))
            elif len(partial_matches) > 1:
                # Complain we got no matches, or too many
                print("WARNING: {} partial matches: {}".format(
                    len(partial_matches),
                    ", ".join([x[1] for x in partial_matches])))




    return fields, containments, references

def write_graph(dot_file, fields, containments, references):
    """
    Given a file object to write to, a dict from type names to lists of (name,
    type) field tuples, a set of (container, containee) containment edges, and a
    set of (referencer, referencee) ID reference edges, and write a GraphViz
    UML.

    See <http://www.ffnn.nl/pages/articles/media/uml-diagrams-using-graphviz-
    dot.php>

    """

    # Start a digraph
    dot_file.write("digraph UML {\n")

    # Define node properties: shaped like UML items.
    dot_file.write("node [\n")
    dot_file.write("\tshape=record\n")
    dot_file.write("]\n")

    for type_name, field_list in fields.iteritems():
        # Put a node for each type.
        dot_file.write("{} [\n".format(type_to_node(type_name)))

        # Start out the UML body bit with the class name
        dot_file.write("\tlabel=\"{{{}".format(type_to_display(type_name)))

        for field_name, field_type in field_list:
            # Put each field. Escape the field types.
            dot_file.write("|{} : {}".format(field_name,
                dot_escape(field_type)))

        # Close the label
        dot_file.write("}\"\n")

        # And the node
        dot_file.write("]\n")

    # Define edge properties for containments
    dot_file.write("edge [\n")
    dot_file.write("\tdir=both\n")
    dot_file.write("\tarrowtail=odiamond\n")
    dot_file.write("\tarrowhead=none\n")
    dot_file.write("]\n")

    for container, containee in containments:
        # Now do the containment edges
        dot_file.write("{} -> {}\n".format(type_to_node(container),
            type_to_node(containee)))

    # Define edge properties for references
    dot_file.write("edge [\n")
    dot_file.write("\tdir=both\n")
    dot_file.write("\tarrowtail=none\n")
    dot_file.write("\tarrowhead=vee\n")
    dot_file.write("\tstyle=dashed\n")
    dot_file.write("]\n")

    for referencer, referencee in references:
        # Now do the reference edges
        dot_file.write("{} -> {}\n".format(type_to_node(referencer),
            type_to_node(referencee)))

    # Close the digraph off.
    dot_file.write("}\n")



def main(args):
    """
    Parses command line arguments, and does the work of the program.
    "args" specifies the program arguments, with args[0] being the executable
    name. The return value should be used as the program's exit code.
    """

    options = parse_args(args) # This holds the nicely-parsed options object

    # Parse the AVPR files and get a dict of (field name, field type) tuple
    # lists for each user-defined type, a set of (container, containee)
    # containment relationships, an a similar set of reference relationships.
    fields, containments, references = parse_avprs(options.avprs)

    if options.dot is not None:
        # Now we do the output to GraphViz format.
        write_graph(options.dot, fields, containments, references)











if __name__ == "__main__" :
    sys.exit(main(sys.argv))
