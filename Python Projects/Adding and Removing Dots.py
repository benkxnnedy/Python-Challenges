def add_dots(word):
    new_word = ""

    for x in word:
        new_word = new_word + x + "."
    new_word = new_word[:-1]

    return new_word


def remove_dots(word):
    new_word = ""

    for x in word:
        if x == ".":
            new_word = new_word + ""
        else:
            new_word = new_word + x
    return new_word


def main():
    print(add_dots("abc"))
    print(remove_dots("H.e.l.l.o"))


if __name__ == "__main__":
    main()
