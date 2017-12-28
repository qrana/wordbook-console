"""
Main file of the program
"""

import text_ui as ui

FILENAME = "sources/words.txt"


def main():
    """
    Main function that initializes the program.
    """
    try:
        user = ui.UI(FILENAME)
        user.loop()
    except ValueError:
        return


main()
