import sys


def main():
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return
    elif len(sys.argv) == 1:
        print("Provide a string as an argument.")
    if len(sys.argv) == 2 and sys.argv[1] != "":
        string = sys.argv[1]
    else:
        print("Write something in the argument.")
        return
    up_count = sum(1 for char in string if char.isupper())
    low_count = sum(1 for char in string if char.islower())
    punctuation_count = sum(
        1 for char in string if not char.isalnum() and not char.isspace()
    )
    digit_count = sum(1 for char in string if char.isdigit())
    space_count = sum(1 for char in string if char.isspace())
    print(f"The text contains {len(string)} characters:")
    print(f"{up_count} upper letters")
    print(f"{low_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


if __name__ == "__main__":
    main()
