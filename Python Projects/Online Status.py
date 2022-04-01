def online_count(users):

    counter = 0

    for x in users:
        if users.get(x) == "Online":
            counter += 1

    return counter


def main():
    users = {
        "Ross": "Online",
        "Joey": "Offline",
        "Monica": "Online"
    }

    print(online_count(users))


if __name__ == "__main__":
    main()
