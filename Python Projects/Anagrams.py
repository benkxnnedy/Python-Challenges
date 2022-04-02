def is_anagram(word1, word2):

    word1_characters = sorted(word1.lower())
    word2_characters = sorted(word2.lower())

    if word1_characters == word2_characters:
        return True
    else:
        return False


def main():
    print(is_anagram("Typhoon", "Opython"))
    print(is_anagram("Alice", "Bob"))


if __name__ == "__main__":
    main()

