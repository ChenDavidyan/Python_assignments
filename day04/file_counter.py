import sys


def file_counter(path):
    with open(path) as f:
        text = f.read()
        print("number of characters in the file:", len(text))

        print("number of lines in the file:", text.count("/n") + 1)

        print("number of words in the file:", text.count(" ") + 1)


def main():
    if len(sys.argv) != 2:
        print("Usage: python count.py FILENAME")

    path = sys.argv[1]
    file_counter(path)


main()
