import re

GRID = []
EXPANDED_GRID = []


def pringrid(grid: list[list[str]]):
    for row in grid:
        print(''.join(*zip(*row)))


def part1():
    expanded_grid = []
    for y, line in enumerate(GRID):
        expanded_grid.append(line)
        if "#" not in line:
            expanded_grid.append(line)
    a = 0
    for x in range(0, len(GRID[0])):
        if all([line[x] == "." for line in GRID]):
            # print(f"COL empty: {x}")
            for y, line in enumerate(expanded_grid):
                line_arr = list(line)
                line_arr.insert(x + a, ".")
                expanded_grid[y] = "".join(line_arr)
            a += 1
    # pringrid(EXPANDED_GRID)

    for y, line in enumerate(expanded_grid):
        for x, sym in enumerate(line):
            if sym == "#":
                galaxies.append((x, y))
    dist = 0
    for i in range(0, len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            p1 = galaxies[i]
            p2 = galaxies[j]
            d = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
            # print(f"Point 1: {p1}, Point 2: {p2}, Distance: {d}")
            dist += d
    print("Part 1: {}".format(dist))


def part2():
    expanded_grid = []
    galaxies = []
    empy_rows = set()
    empy_cols = set()
    for y, line in enumerate(GRID):
        # expanded_grid.append(line)
        if "#" not in line:
            print(f"Row empty: {y}")
            empy_rows.add(y)
            # expanded_grid.extend([line] * 1000000)
    for x in range(0, len(GRID[0])):
        if all([line[x] == "." for line in GRID]):
            print(f"COL empty: {x}")
            empy_cols.add(x)
    print(f"Empty Rows: {empy_rows}")
    print(f"Empty Cols: {empy_cols}")
    # pringrid(EXPANDED_GRID)

    for y, line in enumerate(GRID):
        if "#" in line:
            matches = re.finditer(r"#", line)
            for m in matches:
                galaxies.append((m.start(), y))
    print(galaxies)
    dist = 0
    for i in range(0, len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            p1 = galaxies[i]
            p2 = galaxies[j]
            print(f"Point 1: {p1}, Point 2: {p2}")
            max_x = max([p1[0], p2[0]])
            min_x = min([p1[0], p2[0]])
            ec = [x for x in range(min_x, max_x) if x in empy_cols]
            print(f"EC: {ec}")
            max_y = max([p1[1], p2[1]])
            min_y = min([p1[1], p2[1]])
            er = [y for y in range(min_y, max_y) if x in empy_rows]
            print(f"ER: {er}")
            x_diff = abs(p1[0] - p2[0]) + len(ec) * 10
            y_diff = abs(p1[1] - p2[1]) + len(er) * 10
            d = x_diff + y_diff
            # print(f"Point 1: {p1}, Point 2: {p2}, Distance: {d}")
            dist += d
            # break
        # break

    print("Part 2: {}".format(dist))


with open("sample1.txt", "r") as f:
    lines = f.readlines()
galaxies = []
for y, line in enumerate(lines):
    line = line.strip()
    GRID.append(line)

# pringrid(GRID)
# print()
# print()


part1()
part2()
