import text_ui as ui

FILENAME = "sources/words.txt"


def main():
    try:
        user = ui.UI(FILENAME)
        user.loop()
    except ValueError:
        return


main()
