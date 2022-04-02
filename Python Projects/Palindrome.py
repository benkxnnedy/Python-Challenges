def palindrome(word):

    half1 = []
    half2 = []

    length = len(word)
    length = length / 2

    if len(word) % 2 == 0:
        for x in word[0:int(length)]:
            half1.append(x)
        for z in word[int(length):len(word)]:
            half2.append(z)
    else:
        length = length - 0.5
        for a in word[0:int(length)]:
            half1.append(a)
        for b in word[int(length)+1:len(word)]:
            half2.append(b)

    half2.reverse()
    if half1 == half2:
        return True
    else:
        return False


def main():
    print(palindrome("abcba"))


if __name__ == "__main__":
    main()
