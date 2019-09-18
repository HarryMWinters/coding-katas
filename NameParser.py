#!/usr/bin/env python3

import argparse
import json

helpString = """
This script takes kebab-case string and converts them to all of the below formats and saves those 
converted stings to an output file.


Proper capitalization:
    Space seperated word string with non-trivial word capitalized,
i.e. hello-new-challange becomes Hello New Challange

Underscore capitalization:
    Same as proper capitalization but underscores instead of spaces.

Camelcase (lower):
    Spaces between words are removed the first letter of each word besides the first word is capitalizec.
i.e. hello-new-challange become helloNewChallange.

PascalCase:
    Like camelcase but the first letter of the first word is also capitalized.
"""


def pascalConversion(string):
    return "".join(w.capitalize() for w in string.split("-"))


def properCapConversion(string):
    uncapitalized = ["a", "an", "the", "for", "and", "nor", "but",
                     "or", "yet", "at",  "by",  "from", "of", "on", "to", "with"]
    # Common articles, coordinate conjuctions and prepositions which should not be capitalized.
    outList = []
    for position, word in enumerate(string.split("-")):
        if position == 0:
            outList.append(word.capitalize())
        elif word in uncapitalized:
            outList.append(word)
        else:
            outList.append(word.capitalize())
    return " ".join(outList)


def underCapConversion(string):
    return properCapConversion(string).replace(" ", "_")


def camelConversion(string):
    outList = []
    for position, word in enumerate(string.split("-")):
        if position == 0:
            outList.append(word)
        else:
            outList.append(word.capitalize())
    return "".join(outList)


def lowUnderConversion(string):
    return string.replace("-", "_")


converters = {
    "PASCAL": pascalConversion,
    "PROPERCAP": properCapConversion,
    "UNDERCAP": underCapConversion,
    "CAMEL": camelConversion,
    "LOWUNDER": lowUnderConversion,
    "KEBAB": lambda s: s}


def collectArgs():
    """
    Simple argument parser. Takes no arguments (aside from the command line input_string
    in position one and outputfile).

    returns: input_string, conversion_target_string
    """
    parser = argparse.ArgumentParser(description=help)
    parser.add_argument('input_string', action="store",
                        help='A kebab case string is the first positional argument and is required.')
    parser.add_argument("--outputFile", action="store",
                        required=True, help="Target file for outpus as json.")

    args = parser.parse_args()
    return args.input_string, args.outputFile


def main():
    inputString, outputFile = collectArgs()
    out = {k: converters[k](inputString) for k in converters.keys()}
    with open(outputFile, "w") as file:
        json.dump(out, file)
    exit(0)


if __name__ == "__main__":
    main()
