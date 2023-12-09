import re


def part1():
    data1 = []
    max_red = 12
    max_green = 13
    max_blue = 14
    with open("2-input.txt", "r") as f:
        for line in f.readlines():
            game, data = line.strip().split(": ")
            blue = re.findall(r"(\d+) blue", data)
            red = re.findall(r"(\d+) red", data)
            green = re.findall(r"(\d+) green", data)
            if max([int(i) for i in blue]) <= max_blue and max([int(i) for i in green]) <= max_green and max([int(i) for i in red]) <= max_red:
                game_id = re.match("Game (\d+)", game)
                data1.append(int(game_id[1]))
        print("Part 1: {}".format(sum(data1)))


def part2():
    data1 = []
    with open("2-input.txt", "r") as f:
        for line in f.readlines():
            game, data = line.strip().split(": ")
            blue = re.findall(r"(\d+) blue", data)
            red = re.findall(r"(\d+) red", data)
            green = re.findall(r"(\d+) green", data)
            max_blue = max([int(i) for i in blue])
            max_green = max([int(i) for i in green])
            max_red = max([int(i) for i in red])
            power = max_blue * max_red * max_green
            data1.append(power)
        print("Part 2: {}".format(sum(data1)))


part1()
part2()
