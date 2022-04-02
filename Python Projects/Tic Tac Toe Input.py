def get_row_col(input):

    d1 = 0
    d2 = 0

    if input[0] == "A":
        d2 = 0
    elif input[0] == "B":
        d2 = 1
    elif input[0] == "C":
        d2 = 2

    d1 = int(input[1]) - 1

    location = (d1, d2)
    return location


def main():
    print(get_row_col("B1"))


if __name__ == "__main__":
    main()
