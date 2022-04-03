def format_number(number):

    if number > 0:
        counter = 1
        new_string = ""

        string = str(number)

        for x in reversed(string):
            new_string += x
            if counter % 3 == 0 and counter != 0:
                new_string += ","
            counter += 1

        if new_string[-1] == ",":
            new_string = new_string[:-1]

        return new_string[::-1]
    else:
        return str(number)


def main():
    print(format_number(4500000))


if __name__ == "__main__":
    main()
