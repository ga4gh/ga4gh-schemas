#!/usr/bin/env python2.7
"""
avdlDoxyFilter.py: hack Avro IDL files into vaguely C++-like files that Doxygen
can read.

Re-uses sample code and documentation from
<http://users.soe.ucsc.edu/~karplus/bme205/f12/Scaffold.html>
"""

import argparse, sys, os, itertools, re

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
    parser.add_argument("avdl", type=argparse.FileType('r'),
        help="the AVDL file to read")

    return parser.parse_args(args)


def main(args):
    """
    Parses command line arguments, and does the work of the program.
    "args" specifies the program arguments, with args[0] being the executable
    name. The return value should be used as the program's exit code.
    """

    options = parse_args(args) # This holds the nicely-parsed options object

    # Are we in a comment?
    in_comment = False

    # What level of braces are we in?
    brace_level = 0;

    for line in options.avdl:
        # For every line of Avro

        # See if it's a comment start or end.
        comment_starter = line.rfind("/*")
        comment_ender = line.rfind("*/")

        if(comment_starter != -1 and (comment_ender == -1 or
            comment_ender < comment_starter)):
            # We have entered a multiline comment

            in_comment = True
        elif comment_ender != -1:
            # We have ended a multiline comment and not started another one.
            in_comment = False

        if in_comment:
            # Just pass comments as-is
            print(line.rstrip())
            continue

        # How many unbalanced braces do we have outside comments?
        brace_change = line.count("{") - line.count("}")

        if line.lstrip().startswith("protocol"):
            # It's a protocol, so make it a Module and an Interface.

            # Grab the protocol name
            name = re.search('protocol\s+(\S+)', line).group(1)

            # Make the open lines
            print("namespace {} {{".format(name))
            #print("interface {} {{".format(name))

        elif line.lstrip().startswith("record"):
            # It's a record, so make it a Struct.

            # Grab the record name
            name = re.search('record\s+(\S+)', line).group(1)

            print("struct {} {{".format(name))

        elif line.lstrip().startswith("union"):
            # We need to fix up the union with semicolons.

            # Parse out the union
            match = re.search("union\s*{(.*)}(.*)", line)

            # What got unioned?
            unioned = match.group(1)

            # What's the rest of the line?
            rest = match.group(2)

            # Make the union a template as far as Doxygen knows.
            print("union<{}>{}".format(unioned, rest))


        elif line.rstrip().endswith("}"):
            # The line is closing something, so it needs a semicolon.
            print("{};".format(line.rstrip()))
        else:
            # Pass other lines
            print(line.rstrip())

        # Change the brace level.
        brace_level += brace_change

if __name__ == "__main__" :
    sys.exit(main(sys.argv))
