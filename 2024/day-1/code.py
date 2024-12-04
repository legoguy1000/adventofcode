import os


def part1():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    col1 = []
    col2 = []
    sum = 0
    with open(dir_path + "/input.txt", encoding="utf-8") as f:
        for line in f.readlines():
            if line != "":
                a, b = line.split()
                col1.append(int(a))
                col2.append(int(b))
    col1.sort()
    col2.sort()
    for i in range(len(col1)):
        sum += abs(col1[i] - col2[i])
    print(f"Part1: The Sum is {sum}")


def part2():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    col1 = []
    col2 = []
    sum = 0
    with open(dir_path + "/input.txt", encoding="utf-8") as f:
        for line in f.readlines():
            if line != "":
                a, b = line.split()
                col1.append(int(a))
                col2.append(int(b))
    for item in col1:
        sum += item * col2.count(item)
    print(f"Part 2: The Sum is {sum}")


if __name__ == "__main__":
    part1()
    part2()
