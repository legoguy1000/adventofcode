import re
import math

def part1():
    with open("8-input.txt", "r") as f:
        lines = f.readlines()
    directions = lines[0]
    nodes = {}
    steps = 0
    for line in lines[2:]:
        match = re.match(r"([A-Z]+) = \(([A-Z]+), ([A-Z]+)\)", line)
        node = match.groups()[0]
        left = match.groups()[1]
        right = match.groups()[2]
        nodes[node] = [left, right]
    cn = "AAA"
    j = 0
    while j < len(directions):
        # print(cn)
        if directions[j] == "L":
            i = 0
        elif directions[j] == "R":
            i = 1
        cn = nodes[cn][i]
        steps += 1
        if cn == "ZZZ":
            break
        j += 1
        if j == len(directions) - 1:
            j = 0
        # print(j)
    print("Part 1: {}".format(steps))


def part2():
    with open("8-input.txt", "r") as f:
        lines = f.readlines()
    directions = lines[0]
    nodes = {}
    for line in lines[2:]:
        match = re.match(r"([\dA-Z]+) = \(([\dA-Z]+), ([\dA-Z]+)\)", line)
        node = match.groups()[0]
        left = match.groups()[1]
        right = match.groups()[2]
        nodes[node] = (left, right)
    print(nodes)
    start_nodes = list(filter(lambda x: x.endswith("A"), nodes.keys()))
    # print(start_nodes)
    ret = 1
    for k, node in enumerate(start_nodes):
        print(f"Node: {node}")
        cn = node
        j = 0
        steps = 0
        while not cn.endswith("Z"):
            # print(cn)
            if directions[j] == "L":
                i = 0
            elif directions[j] == "R":
                i = 1
            cn = nodes[cn][i]
            steps += 1
            j = (j + 1) % (len(directions)-1)
        # print(cn)
        ret = math.lcm(ret, steps)
        # print(f"Part 2: {steps}")
    print(f"Part 2: {ret}")


part1()
part2()
