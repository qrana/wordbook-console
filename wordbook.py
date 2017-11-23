"""
The logic and methods of the wordbook are implemented here.
"""


from file import *
import random as r


class Wordbook:
    """
    This class defines the behavior of the main data structure. The indivisual
    words are in a list as Translation objects. This keeps track of all the
    words while the program is running.
    """
    def __init__(self, filename):
        """
        :param filename: name of the file from which to read
        """
        self.__filename = filename  # string
        self.__wordbook = read_file(filename)  # list of "Translation":s
        self.__indx = -1  # set to -1 because is incremented before indexing

    def __iter__(self):
        """
        Used when iterating over Wordbook class instances
        :return: self
        """
        return self

    def __next__(self):
        """
        Tells the iterator the next item in the class instance
        :return: next word in the word book
        """
        self.__indx += 1
        try:
            return self.__wordbook[self.__indx]
        except IndexError:
            self.indx_ = -1
            raise StopIteration

    def empty(self):
        """
        :return: Boolean indicating weather the class instance is empty
        """
        return len(self.__wordbook) == 0

    @property
    def wordbook(self):
        return self.__wordbook

    @staticmethod
    def print_line(forward, reverse, word_type, difficulty):
        """
        Formats a single line for printing and prints it
        :param forward: All the forward direction translations in a list
        :param reverse: All the reverse direction translations in a list
        :param word_type: The type of the word, eg. noun, verb
        :param difficulty: The difficulty as a string
        :return: None
        """
        print("{0:10}".format(word_type),
              "{0:15} -".format(difficulty),
              "{0:50} -".format(", ".join(forward)),
              "{0:50}".format(", ".join(reverse)))

    def print(self, reverse=False):
        """
        prints the words stored in the class
        :param reverse: tells the method if the words need to be printed in
        reverse
        :return: None
        """
        if reverse:
            for translation in sorted(self.__wordbook,
                                      key=lambda x: x.reverse[0]):
                difficulty = self.format_difficulty(translation.difficulty)
                word_type = self.format_word_type(translation.class_type)
                self.print_line(translation.forward, translation.reverse,
                                word_type, difficulty)

        else:
            for translation in sorted(self.__wordbook,
                                      key=lambda x: x.forward[0]):
                difficulty = self.format_difficulty(translation.difficulty)
                word_type = self.format_word_type(translation.class_type)
                self.print_line(translation.forward, translation.reverse,
                                word_type, difficulty)

    def does_word_exist(self, word):
        """
        Tests if the word is already in the class instance
        :param word: the word to be tested as a Translation
        :return: boolean idicating the existence
        """
        for translation in self.__wordbook:
            for fwd in translation.forward:
                if fwd in word.forward:
                    return True
            for rev in translation.reverse:
                if rev in word.reverse:
                    return True
        return False

    def add_word(self, forward=None, reverse=None, class_type=None,
                 difficulty=10):
        """
        Used for adding a word to the main word file
        :param forward: list of forward direction words
        :param reverse: list of reverse direction words
        :param class_type: the type of the class as a character
        :param difficulty: difficulty of the added word as an int
        :return: None
        """
        translation = Translation(forward, reverse, class_type, difficulty)
        if self.does_word_exist(translation):
            print("Word already exists")
            return
        self.__wordbook.append(translation)
        print("Word added")

    def guess_words(self, translation, translations):
        """
        Word's difficulty rating is increased if the answer is incorrect and
        decreased if the answer is correct.
        :param translation: the Translation class instance of the word to be
                            guessed
        :param translations: list of correct solutions
        :return: None
        """
        j = 0
        while j < len(translations):
            answers = [x.lower() for x in translations]
            corrects = []
            for word in answers:
                new_word = self.remove_braces(word)
                corrects.append(new_word)
            while corrects:
                guess = input(str(j + 1) + ": ")
                if guess.lower() not in corrects:
                    print("Wrong answer!")
                    translation.increment_difficulty()
                    print(corrects[0])
                else:
                    j += 1
                    corrects.remove(guess.lower())
                    translation.decrement_difficulty()

    def test_words(self, reverse=False):
        """
        Used for letting the user test their knowledge of the words.
        :return: None
        """
        used_inx = []
        for i in range(3):
            word_index = r.randint(0, len(self.__wordbook) - 1)
            while word_index in used_inx:
                word_index = r.randint(0, len(self.__wordbook) - 1)
            used_inx.append(word_index)
            translation = self.__wordbook[word_index]
            if reverse:
                print(", ".join(translation.forward), "(" +
                      self.format_word_type(translation.class_type) + ")")
                translations = translation.reverse
            else:
                print(", ".join(translation.reverse), "(" +
                      self.format_word_type(translation.class_type) + ")")
                translations = translation.forward
            self.guess_words(translation, translations)

    def save(self):
        """
        Used to save the current progress.
        :return: None
        """
        clear_file(self.__filename)
        for translation in self.__wordbook:
            write_line(self.__filename, format_line(translation))

    def add_wordbook(self, filename):
        """
        Used to add word from another wordbook to this wordbook
        :param filename: filename of the other wordbook data
        :return: None
        """
        other = Wordbook(filename)
        for translation in other.wordbook:
            current_forwards = [x.forward for x in self.__wordbook]
            other_forwards = [x.forward for x in other]
            for fwd in other_forwards:
                if fwd not in current_forwards:
                    self.__wordbook.append(translation)
                else:
                    print("Word", translation.forward, "already exists")

    @staticmethod
    def remove_braces(word):
        start = word.find("(")
        end = word.find(")")
        if start != -1 and end != -1:
            result = word[0:start] + word[end + 1:]
        else:
            result = word
        return result

    @staticmethod
    def format_difficulty(difficulty):
        if 0 <= difficulty <= 2:
            return "Easy"
        elif difficulty <= 5:
            return "Almost easy"
        elif difficulty <= 7:
            return "Moderate"
        elif difficulty <= 10:
            return "Hard"
        else:
            return "Very hard"

    @staticmethod
    def format_word_type(word_type):
        if word_type == "n":
            return "Noun"
        elif word_type == "v":
            return "Verb"
        elif word_type == "a":
            return "Adjective"
        elif word_type == "s":
            return "Sentence"
        elif word_type == "e":
            return "Expression"
        elif word_type == "d":
            return "Adverb"
        else:
            return "Other"
