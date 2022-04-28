def count(word):

    counter = 1
    for x in word:

        if x == "-":
            counter += 1
    return counter

def main():
    print(count("ho-tel"))
    print(count("cat"))
    print(count("met-a-phor"))
    print(count("ter-min-a-tor"))


if __name__ == "__main__":
    main()