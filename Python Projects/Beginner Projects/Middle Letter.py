def mid(word):

    length = len(word)
    middle_index = (length+1)/2

    if middle_index.is_integer():
        middle_letter = word[int(middle_index-1)]
    else:
        middle_letter = ""

    return middle_letter


def main():
    print(mid("abcdefgh"))


if __name__ == "__main__":
    main()
