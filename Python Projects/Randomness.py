import random


def random_number():
    number = random.randint(1, 100)
    return number


def main():

    for x in range(5):
        print(random_number())


if __name__ == "__main__":
    main()
