def all_equal(list):

    counter = 0

    list = iter(list)
    
    for x in list:

        print(next(list))
        if next(list) == x:
            break
        else:
            return False
    return True



def main():
    print(all_equal([1,1,1,3,1,1]))

if __name__ == "__main__":
    main()
