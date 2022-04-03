def capital_indexes(word):
    indexes = []
    counter = 0

    for x in word:
        if x.isupper():
            indexes.append(counter)
        counter += 1
    return indexes


def main():
    print(capital_indexes("HeLLo"))


if __name__ == "__main__":
    main()
