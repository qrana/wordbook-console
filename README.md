This is a small  program that lets you save words to a text file and test your
knowledge of them. The program is run by running the main file. Python 3.6 
is used but should work on older versions of python 3.

--------------------------------------------------------------------------------

A source file is intended to be used with this, as it is the place where
progress is stored. An example of a correctly formatted source file is in
sources/words.txt. Two semicolons separate two languages. Word type means the
tyoe of the word:

n = Noun
v = Verb
a = Adjective
s = Sentence
e = Expression
d = Adverb
o = Other

Other is the default type for words. At the end of the line is the difficulty
between 0 and 10, 10 being the default. The difficulty algorithm is still in
development but currently decreases with correct answers and increases with
incorrect. Future testing and printing options are coming based on word type
and difficulty.
