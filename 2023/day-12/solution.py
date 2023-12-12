import re
import math
import itertools

GRID = []
EXPANDED_GRID = []


def pringrid(grid: list[list[str]]):
    for row in grid:
        print(''.join(*zip(*row)))


def part1():
    # new_grid = []
    sum_opts = 0
    for y, line in enumerate(GRID):
        a, b = line.split(" ")
        b = [int(i) for i in b.split(',')]
        print(f"{y} {a}")
        m = list(re.finditer(r"\?", a))
        # print(m)
        for p in range(1, len(m) + 1):
            up = list(itertools.combinations(m, p))
            # print(up)
            for i in up:
                d = list(a)
                # print(i)
                for j in list(i):
                    s = j.start()
                    d[s] = "#"
                k = "".join(d)
                # print(k)
                v = list(re.finditer(r"#+", k))
                counts = [g.end() - g.start() for g in v]
                if counts == b:
                    sum_opts += 1
            # print(d)
        # break




    print("Part 1: {}".format(sum_opts))


def part2():
    galaxies = []
    # print("Part 2: {}".format(dist))


with open("input.txt", "r") as f:
    lines = f.readlines()
for y, line in enumerate(lines):
    line = line.strip()
    GRID.append(line)

# pringrid(GRID)
part1()
part2()
