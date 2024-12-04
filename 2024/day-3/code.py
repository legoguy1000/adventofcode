import os
import re

REGEX = r"(mul\(\d+,\d+\))"
REGEX1 = r"mul\((\d+),(\d+)\)"
REGEX2 = r"do\(\)|don't\(\)|mul\(\d+,\d+\)"


def part1():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    sum = 0
    matches = []
    with open(dir_path + "/input.txt", encoding="utf-8") as f:
        for line in f.readlines():
            matches += re.findall(REGEX, line)
        for match in matches:
            a = re.findall(REGEX1, match)
            sum += int(a[0][0]) * int(a[0][1])
    print(f"Part1: The Sum is {sum}")


def part2():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    sum = 0
    matches = []
    do = True
    with open(dir_path + "/input.txt", encoding="utf-8") as f:
        for line in f.readlines():
            matches += re.findall(REGEX2, line)
        for match in matches:
            if do and match.startswith("mul"):
                a = re.findall(REGEX1, match)
                sum += int(a[0][0]) * int(a[0][1])
            elif match == "don't()":
                do = False
            elif match == "do()":
                do = True
    print(f"Part 2: The Sum is {sum}")


if __name__ == "__main__":
    part1()
    part2()
