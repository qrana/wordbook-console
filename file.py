"""
The file input/output and file formating is handled here.
"""

from translation import *


def read_file(filename):
    try:
        file = open(filename, 'r', encoding='utf-8')
        wordbook = []
        for line in file:
            line_object = line.rstrip().split(';')
            fwds = []
            revs = []
            class_type = line_object[0]
            difficulty = int(line_object[-1])
            # start iterating from 1 as 0 is the class type
            # iterate as long as the field is not empty
            i = 1
            while line_object[i]:
                word = line_object[i].strip(' ')
                if is_auto_completable(word):
                    word = auto_complete_plural(line_object[i - 1],
                                                line_object[i])
                fwds.append(word)
                i += 1
            i += 1
            while line_object[i] and i < len(line_object) - 1:
                word = line_object[i].strip(' ')
                if is_auto_completable(word):
                    word = auto_complete_plural(line_object[i - 1],
                                                line_object[i])
                revs.append(word)
                i += 1
            wordbook.append(Translation(fwds, revs, class_type, difficulty))
        file.close()
    except IOError:
        print("ERROR READING FILE")
        return []
    return wordbook


def format_line(translation):
    return translation.class_type + \
        ";" + ";".join(translation.forward) +\
        ";;" + ";".join(translation.reverse) + \
        ";" + str(translation.difficulty) + "\n"


def write_line(filename, line):
    try:
        file = open(filename, 'a', encoding='utf-8')
        file.write(line)
        file.close()
    except IOError:
        print("ERROR WRITING THE FILE")


def clear_file(filename):
    try:
        open(filename, "w", encoding='utf-8').close()
    except IOError:
        print("Error clearing file")


def is_auto_completable(testable):
    testable = testable.strip()
    return testable[0] == "-"


def auto_complete_plural(singular, plural_end):
    try:
        singular_no_article = singular.split(" ")[1]
        plural_list = [x for x in plural_end]
        plural_list.remove("-")
        plural = singular_no_article + "".join(plural_list).strip()
    except IndexError:
        return plural_end
    return plural
