import re
import math


def part1():
    with open("6-input.txt", "r") as f:
        lines = f.readlines()
    times = re.findall(r"\d+", lines[0])
    distance = re.findall(r"\d+", lines[1])
    print(times)
    print(distance)
    data = [0] * len(times)
    for i in range(0, len(times), 1):
        for j in range(0, int(times[i]) + 1, 1):
            d = j * (int(times[i]) - j)
            if d > int(distance[i]):
                data[i] += 1

    print("Part 1: {}".format(math.prod(data)))


def part2():
    with open("6-input.txt", "r") as f:
        lines = f.readlines()
    times = re.findall(r"\d+", lines[0].replace(" ", ""))
    distances = re.findall(r"\d+", lines[1].replace(" ", ""))
    time = int(times[0])
    distance = int(distances[0])
    print(times)
    print(distance)
    data = 0
    for j in range(0, time + 1, 1):
        d = j * (time - j)
        if d > distance:
            data += 1

    print("Part 2: {}".format(data))


part1()
part2()
