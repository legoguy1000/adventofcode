import re


def part1():
    data = []
    with open("4-input.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        card, numbers = line.strip().split(": ")
        winning_str, choices_str = numbers.strip().split("|")
        winning = re.findall(r"\d+", winning_str)
        choices = re.findall(r"\d+", choices_str)
        # print(winning)
        # print(choices)
        temp = [x for x in choices if x in winning]
        # print(temp)
        score = int(2 ** (len(temp) - 1))
        # print(score)
        data.append(score)
    print("Part 1: {}".format(sum(data)))


def part2():
    with open("4-input.txt", "r") as f:
        lines = f.readlines()
    data = [0] * len(lines)
    for card, line in enumerate(lines):
        _, numbers = line.strip().split(": ")
        winning_str, choices_str = numbers.strip().split("|")
        winning = re.findall(r"\d+", winning_str)
        choices = re.findall(r"\d+", choices_str)
        temp = [x for x in choices if x in winning]
        data[card] += 1
        print(data[card])
        for c in range(1, len(temp)+1, 1):
            data[card + c] += 1 * data[card]
    print("Part 2: {}".format(sum(data)))


part1()
part2()
