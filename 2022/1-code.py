


if __name__ == "__main__":
    data = []
    with open("input.txt", "r") as f:
        temp = 0
        for line in f.readlines():
            stripped = line.strip()
            # print(stripped)
            if stripped != "":
                temp += int(stripped)
            else:
                data.append(temp)
                temp = 0
    data.sort()
    print(data)
    print(sum(data[-3:]))