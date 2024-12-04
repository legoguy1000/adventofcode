import os

# def a(grid: list[list[str]], x: int, y: int, dir: int):
#     if dir == 1:

#         def check(grid: list[list[str]], x: int, y: int):
#             return [grid[y][x + k] for k in range(0, 4)]

#     if dir == 2:

#         def check(grid: list[list[str]], x: int, y: int):
#             return [grid[y][x - k] for k in range(0, 4)]

#     return check


def checkpoint(grid: list[list[str]], x: int, y: int) -> int:
    good = []
    try:
        good.append("".join([grid[y][x + k] for k in range(0, 4)]))
    except IndexError:
        pass
        # print("y, x - k bad")
    try:
        if x - 3 < 0:
            raise IndexError
        good.append("".join([grid[y][x - k] for k in range(0, 4)]))
    except IndexError:
        pass
        # print("y, x - k bad")
    try:
        good.append("".join([grid[y + k][x] for k in range(0, 4)]))
    except IndexError:
        pass
    try:
        if y - 3 < 0:
            raise IndexError
        good.append("".join([grid[y - k][x] for k in range(0, 4)]))
    except IndexError:
        pass
    try:
        if y - 3 < 0:
            raise IndexError
        good.append("".join([grid[y - k][x + k] for k in range(0, 4)]))
    except IndexError:
        pass
    try:
        if x - 3 < 0 or y - 3 < 0:
            raise IndexError
        good.append("".join([grid[y - k][x - k] for k in range(0, 4)]))
    except IndexError:
        pass
    try:
        if x - 3 < 0:
            raise IndexError
        good.append("".join([grid[y + k][x - k] for k in range(0, 4)]))
    except IndexError:
        pass
    try:
        good.append("".join([grid[y + k][x + k] for k in range(0, 4)]))
    except IndexError:
        pass
    try:
        if x - 3 < 0 or y - 3 < 0:
            raise IndexError
        good.append("".join([grid[y - k][x - k] for k in range(0, 4)]))
    except IndexError:
        pass
    a = [x for x in good if x == "XMAS"]
    print(a)
    return len(a)


def part1():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    sum = 0
    grid = []
    with open(dir_path + "/input.txt", encoding="utf-8") as f:
        for line in f.readlines():
            grid.append(list(line.strip()))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            sum += checkpoint(grid, j, i)

    print(f"Part1: The Sum is {sum}")


def part2():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    sum = 0
    matches = []
    do = True
    with open(dir_path + "/input.txt", encoding="utf-8") as f:
        for line in f.readlines():
            pass
    print(f"Part 2: The Sum is {sum}")


if __name__ == "__main__":
    part1()
    # part2()
