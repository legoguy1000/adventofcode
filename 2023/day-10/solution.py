import pprint
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

GRID = []


class Coordinate:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.value = GRID[y][x]
        self.start = self.value == "S"
        self.tuple = (x, y)

    def __repr__(self):
        return f"Coordinate({self.__str__()})"

    def __str__(self):
        return f"x={self.x}, y={self.y}"

    def check_north(self):
        try:
            nx = self.x
            ny = self.y - 1
            n = GRID[ny][nx]
            if (self.start or self.value in ("|", "J", "L")) and n in ("|", "F", "7"):
                return True
        except IndexError:
            return False

    def check_south(self):
        try:
            nx = self.x
            ny = self.y + 1
            n = GRID[ny][nx]
            if (self.start or self.value in ("|", "F", "7")) and n in ("|", "J", "L"):
                return True
        except IndexError:
            return False

    def check_east(self):
        try:
            nx = self.x + 1
            ny = self.y
            n = GRID[ny][nx]
            if (self.start or self.value in ("L", "F", "-")) and n in ("-", "7", "J"):
                return True
        except IndexError:
            return False

    def check_west(self):
        try:
            nx = self.x - 1
            ny = self.y
            n = GRID[ny][nx]
            if (self.start or self.value in ("J", "7", "-")) and n in ("-", "L", "F"):
                return True
        except IndexError:
            return False


def compare_pos(a: Coordinate, b: Coordinate):
    if a.x == b.x and a.y == b.y:
        return True
    return False


def followpath(current: Coordinate, previous: Coordinate) -> (Coordinate, bool):
    run = True
    nc = None
    # print(f"current: {current}, previous: {previous}")
    if current.check_north() and not compare_pos(previous, Coordinate(current.x, current.y - 1)):
        nc = Coordinate(current.x, current.y - 1)
        # print("Going North")
    elif current.check_south() and not compare_pos(previous, Coordinate(current.x, current.y + 1)):
        nc = Coordinate(current.x, current.y + 1)
        # print("Going South")
    elif current.check_east() and not compare_pos(previous, Coordinate(current.x + 1, current.y)):
        nc = Coordinate(current.x + 1, current.y)
        # print("Going East")
    elif current.check_west() and not compare_pos(previous, Coordinate(current.x - 1, current.y)):
        nc = Coordinate(current.x - 1, current.y)
        # print("Going West")
    else:
        run = False
        # print("Get F'd")
    return nc, run


def part1(start: Coordinate):
    dist = []
    for _, row in enumerate(GRID):
        dist.append([0] * len(row))
    # print(GRID)
    print(f"Start: {start}")
    if start.check_north():
        count = 1
        previous = start
        current = Coordinate(start.x, start.y - 1)
        dist[current.y][current.x] = count
        run = True
        while run:
            count += 1
            # print(current)
            nc, run = followpath(current, previous)
            previous = current
            if nc is not None:
                current = nc
                if dist[current.y][current.x] == 0 or count < dist[current.y][current.x]:
                    dist[current.y][current.x] = count
    if start.check_south():
        count = 1
        previous = start
        current = Coordinate(start.x, start.y + 1)
        dist[current.y][current.x] = count
        run = True
        while run:
            count += 1
            # print(current)
            nc, run = followpath(current, previous)
            previous = current
            if nc is not None:
                current = nc
                if dist[current.y][current.x] == 0 or count < dist[current.y][current.x]:
                    dist[current.y][current.x] = count

    if start.check_east():
        count = 1
        previous = start
        current = Coordinate(start.x + 1, start.y)
        dist[current.y][current.x] = count
        run = True
        while run:
            count += 1
            # print(current)
            nc, run = followpath(current, previous)
            previous = current
            if nc is not None:
                current = nc
                if dist[current.y][current.x] == 0 or count < dist[current.y][current.x]:
                    dist[current.y][current.x] = count
    if start.check_west():
        count = 1
        previous = start
        current = Coordinate(start.x - 1, start.y)
        dist[current.y][current.x] = count
        run = True
        while run:
            count += 1
            # print(current)
            nc, run = followpath(current, previous)
            previous = current
            if nc is not None:
                current = nc
                if dist[current.y][current.x] == 0 or count < dist[current.y][current.x]:
                    dist[current.y][current.x] = count
    
    # pprint.pprint(dist)
    max_dist = 0
    for row in dist:
        nm = max(row)
        if nm > max_dist:
            max_dist = nm
    print("Part 1: {}".format(max_dist))


def part2(start: Coordinate):
    points = []
    # print(GRID)
    print(f"Start: {start}")
    if start.check_north():
        previous = start
        current = Coordinate(start.x, start.y - 1)
        run = True
        while run:
            # print(current)
            nc, run = followpath(current, previous)
            previous = current
            if nc is not None:
                current = nc
    elif start.check_south():
        if start.tuple not in points:
            points.append(start.tuple)
        previous = start
        current = Coordinate(start.x, start.y + 1)
        run = True
        while run:
            if current.tuple not in points:
                points.append(current.tuple)
            # print(current)
            nc, run = followpath(current, previous)
            previous = current
            if nc is not None:
                current = nc
    elif start.check_east():
        previous = start
        current = Coordinate(start.x + 1, start.y)
        run = True
        while run:
            # print(current)
            nc, run = followpath(current, previous)
            previous = current
            if nc is not None:
                current = nc
    elif start.check_west():
        previous = start
        current = Coordinate(start.x - 1, start.y)
        run = True
        while run:
            # print(current)
            nc, run = followpath(current, previous)
            previous = current
            if nc is not None:
                current = nc
    enclosed = 0
    poly = Polygon(list(points))
    # print(points)
    # print(poly)
    # new_grid = []
    # for _, row in enumerate(GRID):
    #     new_grid.append(["x"] * len(row))
    # for (x, y) in list(points):
    #     new_grid[y][x] = "."
    # for row in new_grid:
    #     print(''.join(*zip(*row)))

    for y, row in enumerate(GRID):
        for x, _ in enumerate(row):
            point = Point(x, y)
            if (x, y) not in points and x > 0 and x < len(row) -1 and y > 0 and y < len(GRID) - 1:
                if poly.contains(point):
                    enclosed += 1

    print("Part 2: {}".format(enclosed))


with open("input.txt", "r") as f:
    lines = f.readlines()
for y, line in enumerate(lines):
    line = line.strip()
    GRID.append(line)
    if "S" in line:
        x = line.index("S")
        start = Coordinate(x, y)

part1(start)
part2(start)
