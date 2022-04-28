def all_equal(list):

    for x in list:

        for z in list:
            if x != z:
                return False

    return True



def main():
    print(all_equal([1,1,1]))

if __name__ == "__main__":
    main()
