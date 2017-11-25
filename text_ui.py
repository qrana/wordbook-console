"""
The text ui is implemented here.
"""

import wordbook as wb


class UI:
    def __init__(self, location):
        wordbook = wb.Wordbook(location)
        if wordbook.empty():
            raise ValueError
        self.wordbook_ = wordbook

    def loop(self):
        """
        Used for keeping the UI running. Loops until user enters quit.
        :return: None
        """
        while True:
            try:
                print("Commands: add, fileadd, print, rprint, test, rtest, "
                      "stest, quit")
                input_str = input(">> ").split(" ")
                command = input_str[0]
                if len(input_str) > 1:
                    raise SyntaxError
                elif command.lower() == "quit":
                    self.wordbook_.save()
                    print("Bye!")
                    return
                elif command.lower() == "add":
                    translation = self.add()
                    self.wordbook_.add_word(translation)
                elif command.lower() == "fileadd":
                    filename = input("Enter file name: ")
                    self.wordbook_.add_wordbook(filename)
                elif command.lower() == "print":
                    self.wordbook_.print()
                elif command.lower() == "rprint":
                    self.wordbook_.print(reverse=True)
                elif command.lower() == "test":
                    self.wordbook_.test_words()
                elif command.lower() == "rtest":
                    self.wordbook_.test_words(reverse=True)
                elif command.lower() == "stest":
                    self.wordbook_.test_sentences()
                else:
                    raise SyntaxError
            except SyntaxError:
                print("Incorrect input, try again")

    @staticmethod
    def add():
        """
        Used for adding a word to the dictionary
        :return: the parameters of the word to be added
        """
        forwds = []
        revs = []
        forw = "Spam"
        while forw != "":
            forw = input("Forward direction: ")
            if forw:
                forwds.append(forw.lower())
        rev = "Eggs"
        while rev != "":
            rev = input("Reverse direction: ")
            if rev:
                revs.append(rev.lower())
        class_type_ok = False
        class_type = "o"
        accepted_class_types = ["n", "v", "a", "o"]
        while not class_type_ok:
            class_type = input("Class type: ")
            class_type = class_type.lower()
            if class_type in accepted_class_types:
                class_type_ok = True
            else:
                print("Accepted types: n, v, a, o")
        return forwds, revs, class_type
