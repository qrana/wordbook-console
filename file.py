"""
The file input/output and file formating is handled here.
"""

from translation import Translation


def read_file(filename):
    """
    Reads the word data from a file.
    :param filename: the filename/location as a string
    :return: List of Translation obbjects
    """
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
            i = 1  # tells the field number of the line
            while line_object[i]:  # loop until found an ampty field
                word = line_object[i].strip(' ')
                if is_auto_completable(word):
                    word = auto_complete_plural(line_object[i - 1],
                                                line_object[i])
                fwds.append(word)
                i += 1
            i += 1 # accounts for the empty field
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
    except IndexError:
        print("ERROR IN THE FILE")
        return []
    return wordbook


def format_line(translation):
    """
    Formats the line to be written in a correct format
    :param translation: the Translation object that is to be formatted
    :return: a string of the formatted line
    """
    return translation.class_type + \
        ";" + ";".join(translation.forward) +\
        ";;" + ";".join(translation.reverse) + \
        ";" + str(translation.difficulty) + "\n"


def write_line(filename, line):
    """
    Writes a single line to the file
    :param filename: name of the file as a string
    :param line: line to be written as a string
    :return: None
    """
    try:
        file = open(filename, 'a', encoding='utf-8')
        file.write(line)
        file.close()
    except IOError:
        print("ERROR WRITING THE FILE")


def clear_file(filename):
    """
    Empties the file
    :param filename: the file to be emptied
    :return: None
    """
    try:
        open(filename, "w", encoding='utf-8').close()
    except IOError:
        print("Error clearing file")


def is_auto_completable(testable):
    """
    Test if a string should be auto-completed by adding the body of the word
    from the singular form.

    For example "-en" is to be auto-completed by replacing "-" with the base
    from another owrd.

    :param testable: the word to be tested as a string
    :return: boolean indicating the need to auto-complete
    """
    testable = testable.strip()
    return testable[0] == "-"


def auto_complete_plural(singular, plural_end):
    """
    Auto-completed plurals based on the test described in the previous function.
    :param singular: the base form of the word as a string
    :param plural_end: the plural ending as a string
    :return: the two parameters auto-completed into a word
    """
    try:
        singular_no_article = singular.split(" ")[1]
        plural_list = [x for x in plural_end]
        plural_list.remove("-")
        plural = singular_no_article + "".join(plural_list).strip()
    except IndexError:
        return plural_end
    return plural
