import os


def part1():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    sum = 0
    grid = []
    with open(dir_path + "/input.txt", encoding="utf-8") as f:
        for line in f.readlines():
            grid.append(list(line.strip()))
    x, y = 0, 0
    for i in range(len(grid)):
        if "^" in grid[i]:
            y = i
            x = grid[i].index("^")
            break
    direction = "up"
    positions = []
    while True:
        positions.append((x, y))
        print((x, y))
        if direction == "up" and grid[y - 1][x] != "#":
            if y - 1 < 0:
                break
            y -= 1
        elif direction == "up" and grid[y - 1][x] == "#":
            direction = "right"
            if x + 1 >= len(grid[y]):
                break
            x += 1
        elif direction == "right":
            if x + 1 >= len(grid[y]):
                break
            elif grid[y][x + 1] != "#":
                x += 1
            elif grid[y][x + 1] == "#":
                direction = "down"
                if y + 1 >= len(grid):
                    break
                y += 1
        elif direction == "down":
            if y + 1 >= len(grid):
                break
            elif grid[y + 1][x] != "#":
                y += 1
            elif grid[y + 1][x] == "#":
                direction = "left"
                if x - 1 < 0:
                    break
                x -= 1
        elif direction == "left":
            if grid[y][x - 1] != "#":
                if x - 1 < 0:
                    break
                x -= 1
            elif grid[y][x - 1] == "#":
                direction = "up"
                if y - 1 < 0:
                    break
                y -= 1

    print(f"Part1: The Sum is {len(list(set(positions)))}")


def part2():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    sum = 0
    rules = []
    updates = []
    badupdates = []
    with open(dir_path + "/input.txt", encoding="utf-8") as f:
        for line in f.readlines():
            pass
    print(f"Part 2: The Sum is {sum}")


if __name__ == "__main__":
    part1()
    part2()
