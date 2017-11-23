"""
This module defines the Translation class.
"""


class Translation:
    """
    The point of this class is to define a clear interface to access different
    information about the translation.

    This is a class for a single word and its forms and translations. It has all
    the forward translations, meaning the direction of the default translation
    direction as well as the actual translations in the reverse list.

    This class also defines a class type and difficulty for the individual
    translation.
    """
    def __init__(self, forward, reverse, class_type, difficulty=10):
        self.__forward = forward
        self.__reverse = reverse
        self.__class_type = class_type
        self.__difficulty = difficulty

    def __lt__(self, other):
        return self.__forward < other.forward

    @property
    def forward(self):
        return self.__forward

    @property
    def reverse(self):
        return self.__reverse

    @property
    def class_type(self):
        return self.__class_type

    @property
    def difficulty(self):
        return self.__difficulty

    def increment_difficulty(self):
        if self.__difficulty <= 10:
            self.__difficulty += 1

    def decrement_difficulty(self):
        if self.__difficulty > 0:
            self.__difficulty -= 1
