import sys


def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        text_str = sys.argv[1]
        number = int(sys.argv[2])
        if not text_str.isalpha() or text_str != "":
            if not all(char.isalpha() or char == " " for char in text_str):
                raise AssertionError("the arguments are bad")

        word_list = text_str.split()
        filtered_words = list(
            filter(lambda word: len(word) > number, word_list))
        print(filtered_words)

    except (AssertionError, ValueError):
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
