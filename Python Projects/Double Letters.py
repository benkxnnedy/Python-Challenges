def double_letters(word):

    previous_letter = ""

    for x in word:
        if x == previous_letter:
            return True
        else:
            previous_letter = x
    return False


def main():
    print(double_letters("Hello"))


if __name__ == "__main__":
    main()
    