import re
import math

GRID = []
GRID2 = []

def part1():
    top_sum = 0
    left_sum = 0
    vert_check = []
    for i, group in enumerate(GRID):
        horizontal = False
        for y in range(0, len(group) - 1):
            print(f"Group: {i}, y: {y}")
            top = group[y]
            bot = group[y + 1]
            if top == bot:
                j = 1
                # print(f"{y}: {top} -- {bot}")
                while True:
                    top_i = y - j
                    bot_i = y + 1 + j
                    print(f"{top_i}  --  {bot_i}")
                    if top_i >= 0 and bot_i < len(group):
                        top = group[top_i]
                        bot = group[bot_i]
                    # print(f"{top}  --  {bot}")
                    if top_i == 0 or bot_i == len(group) - 1:
                        if top == bot:
                            top_sum += y + 1
                            horizontal = True
                            break
                    if top != bot:
                        break
                    j += 1
        if not horizontal:
            vert_check.append(i)
    for i in vert_check:
        group = GRID2[i]
        for y in range(0, len(group) - 1):
            top = group[y]
            bot = group[y + 1]
            if top == bot:
                j = 1
                # print(f"{y}: {top} -- {bot}")
                while True:
                    top_i = y - j
                    bot_i = y + 1 + j
                    if top_i >= 0 and bot_i < len(group):
                        top = group[top_i]
                        bot = group[bot_i]
                    # print(f"{top}  --  {bot}")
                    if top_i == 0 or bot_i == len(group) - 1:
                        if top == bot:
                            left_sum += y + 1
                            break
                    if top != bot:
                        break
                    j += 1
    total = top_sum * 100 + left_sum
    print("Part 1: {}".format(total))


def part2():
    top_sum = 0
    left_sum = 0
    vert_check = []
    for i, group in enumerate(GRID):
        horizontal = False
        for y in range(0, len(group) - 1):
            print(f"Group: {i}, y: {y}")
            top = group[y]
            bot = group[y + 1]
            for a in range(0, len(top)):
                top[a] = "#" if top[a] == "." else "."

            if top == bot:
                j = 1
                # print(f"{y}: {top} -- {bot}")
                while True:
                    top_i = y - j
                    bot_i = y + 1 + j
                    print(f"{top_i}  --  {bot_i}")
                    if top_i >= 0 and bot_i < len(group):
                        top = group[top_i]
                        bot = group[bot_i]
                    # print(f"{top}  --  {bot}")
                    if top_i == 0 or bot_i == len(group) - 1:
                        if top == bot:
                            top_sum += y + 1
                            horizontal = True
                            break
                    if top != bot:
                        break
                    j += 1
        if not horizontal:
            vert_check.append(i)



    total = top_sum * 100 + left_sum
    print("Part 2: {}".format(total))


with open("input.txt", "r") as f:
    lines = f.readlines()
temp = []
for y, line in enumerate(lines):
    line = line.strip()
    if line != "":
        temp.append(line)
    if line == "" or y == len(lines) - 1:
        GRID.append(temp)
        temp = []
for group in GRID:
    temp = []
    for x in range(0, len(group[0])):
        col = [line[x] for line in group]
        temp.append("".join(col))
    GRID2.append(temp)


# print(GRID)
# print(GRID2)
# part1()
part2()
