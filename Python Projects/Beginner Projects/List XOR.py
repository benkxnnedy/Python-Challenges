def list_xor(n, list1, list2):

    if n in list1 and n in list2:
        return False
    elif n not in list1 and n not in list2:
        return False
    else:
        return True

def main():
    print(list_xor(1, [1, 2, 3], [4, 5, 6]))

if __name__ == "__main__":
    main()
