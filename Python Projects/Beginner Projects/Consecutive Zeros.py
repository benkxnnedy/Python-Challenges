def consecutive_zeros(binary):
    largest = 0
    counter = 0

    for x in binary:
        if x == "0":
            counter += 1
        else:
            counter = 0

        if largest < counter:
            largest = counter

    return largest


def main():
    print(consecutive_zeros("10101"))


if __name__ == "__main__":
    main()
