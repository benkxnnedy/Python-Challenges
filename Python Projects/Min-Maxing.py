def largest_difference(numbers):
    difference = max(numbers) - min(numbers)
    return difference


def main():
    print(largest_difference([1 ,2, 5]))


if __name__ == "__main__":
    main()
    