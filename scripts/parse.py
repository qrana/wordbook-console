"""
This file contains a script that can be used to parse an input file into a
format supported by the main program.
"""

# TODO: fix too many words being removed

import os
import re

PATH = os.getcwd() + "/sources"
INFILE = "irregular-verbs-swedish-raw.txt"
INFILENAME = os.path.join(os.path.expanduser('~'), PATH + "/" + INFILE)
OUTFILE = "irregular-verbs-swedish.txt"
OUTFILENAME = os.path.join(os.path.expanduser('~'), PATH + "/" + OUTFILE)

CONTENT = []

with open(INFILENAME, "r", encoding="utf-8") as file:
    for line in file:
        line = line.rstrip()

        # skip comments
        if re.match(r"\s*#.*", line):
            print("removed comment: " + line)
            continue

        # translation matches a string inside braces at the end of the line
        translation = re.search(r"\(([;, \w]+)\)$", line)
        if isinstance(translation, type(None)):
            print(line, "TRANSLATION NOT FOUND")
            translated_word = input("Please type the translation: ")
        else:
            translated_word = translation[translation.lastindex]

        # remove stuff between braces
        stuff = re.search(r"\(([^)]+\))", line)
        stuff_groups = stuff.groups()
        new_line = ""
        for i in range(len(stuff_groups)):
            new_line += line[:stuff.start(i + 1) - 1] + line[stuff.end(i + 1):]
            start_brace = new_line.find("(")
            new_line = new_line[:start_brace:]

        new_line += ";;" + translated_word
        new_line = new_line.replace(",", ";")
        CONTENT.append(new_line)

with open(OUTFILENAME, 'w', encoding="utf-8") as file:
    for line in CONTENT:
        file.write("v;" + line + ";10\n")
