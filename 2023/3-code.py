import re
import math
from typing import Dict, List


def part1():
    data = []
    with open("3-input.txt", "r") as f:
        lines = f.readlines()
        for line_num, line in enumerate(lines):
            temp = []
            line = line.strip()
            line_length = len(line)
            nums = re.finditer(r"\d+", line)
            for num in nums:
                i = num.start()
                si = i - 1
                ei = num.end()
                # if i == 0:
                #     si = i
                # if i + len(num) == line_length:
                #     ei = line_length - 1
                # print("{}  -  I: {}, SI: {}, EI: {}".format(num.group(0), i, si, ei))
                part_num = False
                for x in range(si, ei+1):
                    for y in range(line_num-1, line_num+2):
                        if (y >= 0 and y < len(lines)) and (x >= 0 and x < line_length):
                            if re.match(r"[^\d\.]", lines[y][x]):
                                part_num = True
                if part_num:
                    temp.append(int(num.group()))
            # print(temp)
            data.append(sum(temp))
    # print(data)
    print("Part 1: {}".format(sum(data)))


def part2():
    data = []
    with open("3-input.txt", "r") as f:
        lines = f.readlines()
    positions = dict()
    for line_num, line in enumerate(lines):
        line = line.strip()
        line_length = len(line)
        nums = re.finditer(r"\d+", line)
        for num in nums:
            i = num.start()
            si = i - 1
            ei = num.end()
            # print("{}  -  I: {}, SI: {}, EI: {}".format(num.group(0), i, si, ei))
            for x in range(si, ei+1):
                for y in range(line_num-1, line_num+2):
                    if (y >= 0 and y < len(lines)) and (x >= 0 and x < line_length):
                        if lines[y][x] == "*":
                            key = "{},{}".format(x, y)
                            if key not in positions.keys():
                                positions[key] = []
                            positions[key].append(int(num.group(0)))
    for pos, vals in positions.items():
        print(vals)
        if len(vals) == 2:
            data.append(math.prod(vals))
    # print(data)
    print("Part 2: {}".format(sum(data)))


part1()
part2()
