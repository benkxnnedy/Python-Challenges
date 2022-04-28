def flatten(list):
    new_list = []
    for x in list:
        for z in x:
            new_list.append(z)

    return new_list


def main():

    numbers = [1, 2]
    numbers2 = [3, 4]
    combined = [numbers, numbers2]

    print(flatten(combined))


if __name__ == "__main__":
    main()
