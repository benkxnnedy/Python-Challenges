def online_count(users):

    counter = 0

    for x in users:
        if users.get(x) == "online":
            counter += 1

    return counter


def main():
    users = {
        "Ross": "online",
        "Joey": "Online"
    }

    print(online_count(users))


if __name__ == "__main__":
    main()
