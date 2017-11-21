"""
This module defines the Translation class. It is similar to namedtuple from
collections, but mutable.
"""


class Translation:
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
