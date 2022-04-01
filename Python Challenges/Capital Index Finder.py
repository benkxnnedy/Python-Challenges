def capital_indexes(word):
    index_list = []
    i = 0

    for x in word:

        if x.isupper():
            index_list.append(i)
        i += 1

    return index_list


def main():
    print(capital_indexes("HeLLO"))


if __name__ == "__main__":
    main()
