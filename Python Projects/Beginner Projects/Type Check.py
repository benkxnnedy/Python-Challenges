def only_ints(num1, num2):

    if isinstance(num1, bool) or isinstance(num2, bool):
        return False
    else:
        if isinstance(num1, int) and isinstance(num2, int):
            return True
        else:
            return False


def main():
    print(only_ints(1, True))


if __name__ == "__main__":
    main()


