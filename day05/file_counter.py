import sys


def char_cnt(text):
    return len(text)


def lines_cnt(text):
    if text == "":
        return 0
    return text.count("\n") + 1


def words_cnt(text):
    if text == "":
        return 0
    return text.count(" ") + 1


def main():
    print(sys.argv)

    if len(sys.argv) != 2:
        print("Usage: python count.py FILENAME")

    path = sys.argv[1]
    with open(path) as f:
        text = f.read()

    char_cnt(text)
    lines_cnt(text)
    words_cnt(text)
