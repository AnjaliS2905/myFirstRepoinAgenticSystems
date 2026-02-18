users = [
    {
        "name": "Anjali",
        "scores": [98, 99, 96],
        "roles": {"developer", "admin", "maintainer"}
    },
    {
        "name": "Ankit",
        "scores": [70, 75, 78],
        "roles": {"viewer", "admin"}
    },
    {
        "name": "Mayank",
        "scores": [88, 92, 84],
        "roles": {"editor", "viewer"}
    }
]


def average_calculator(users):
    avgs = []
    for user in users:
        average = sum(user["scores"]) / len(user["scores"])
        avgs.append((user["name"], average)) 
    return avgs


def role_checker(roles):
    return True if "admin" in roles else False 


def main():
    mem_avg = average_calculator(users)

    for user in users:
        print("Name:", user["name"])

        for avg_data in mem_avg:
            if avg_data[0] == user["name"]:
                average = avg_data[1]
                break

        print("Average Score:", average)
        print("Admin Access:", role_checker(user["roles"]))
        print("-" * 30)


if __name__ == "__main__":
    main()
