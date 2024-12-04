import os


def checkXMAS(grid: list[list[str]], x: int, y: int) -> int:
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
    return good.count("XMAS")


def checkX_MAS(grid: list[list[str]], x: int, y: int) -> int:
    good = ["MAS", "SAM"]
    if grid[y][x] != "A":
        return 0
    try:
        if x - 1 < 0 or y - 1 < 0:
            raise IndexError
        diag1 = grid[y - 1][x - 1] + grid[y][x] + grid[y + 1][x + 1]
        diag2 = grid[y - 1][x + 1] + grid[y][x] + grid[y + 1][x - 1]
        if diag1 in good and diag2 in good:
            return 1
    except IndexError:
        pass
    return 0


def part1():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    sum = 0
    grid = []
    with open(dir_path + "/input.txt", encoding="utf-8") as f:
        for line in f.readlines():
            grid.append(list(line.strip()))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            sum += checkXMAS(grid, j, i)

    print(f"Part1: The Sum is {sum}")


def part2():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    sum = 0
    grid = []
    with open(dir_path + "/input.txt", encoding="utf-8") as f:
        for line in f.readlines():
            grid.append(list(line.strip()))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            sum += checkX_MAS(grid, j, i)
    print(f"Part 2: The Sum is {sum}")


if __name__ == "__main__":
    part1()
    part2()
