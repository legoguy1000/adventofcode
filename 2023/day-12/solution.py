import re
import math
import itertools

GRID = []
EXPANDED_GRID = []


def pringrid(grid: list[list[str]]):
    for row in grid:
        print(''.join(*zip(*row)))


def part1():
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
    # i == current position within dots
    # bi == current position within blocks
    # current == length of current block of '#'
    # state space is len(dots) * len(blocks) * len(dots)
    DP = {}
    def f(dots, blocks, i, bi, current):
        key = (i, bi, current)
        if key in DP:
            return DP[key]
        if i==len(dots):
            if bi==len(blocks) and current==0:
                return 1
            elif bi==len(blocks)-1 and blocks[bi]==current:
                return 1
            else:
                return 0
        ans = 0
        for c in ['.', '#']:
            if dots[i]==c or dots[i]=='?':
                if c=='.' and current==0:
                    ans += f(dots, blocks, i+1, bi, 0)
                elif c=='.' and current>0 and bi<len(blocks) and blocks[bi]==current:
                    ans += f(dots, blocks, i+1, bi+1, 0)
                elif c=='#':
                    ans += f(dots, blocks, i+1, bi, current+1)
        DP[key] = ans
        return ans
    sum_opts = 0
    for y, line in enumerate(GRID):
        a, b = line.split(" ")    
        a = "?".join([a, a, a, a, a])
        b = [int(i) for i in b.split(',')] * 5
        print(f"{y} {a} {b}")
        DP.clear()
        sum_opts += f(a, b, 0, 0, 0)
    print("Part 2: {}".format(sum_opts))


with open("input.txt", "r") as f:
    lines = f.readlines()
for y, line in enumerate(lines):
    line = line.strip()
    GRID.append(line)

# pringrid(GRID)
# part1()
part2()
