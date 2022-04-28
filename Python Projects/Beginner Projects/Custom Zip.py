def zap(a, b):

    counter = 0
    list = []
    for x in a:
        list.append((x, b[counter]))
        counter += 1

    return list


def main():
    zap([0,1,2,3], [5,6,7,8])


if __name__ == "__main__":
    main()
