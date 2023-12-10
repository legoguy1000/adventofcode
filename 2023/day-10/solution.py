import pprint

GRID = []


class Coordinate:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.value = GRID[y][x]
        self.start = self.value == "S"

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


def part1():
    with open("input.txt", "r") as f:
        lines = f.readlines()
    dist = []
    for y, line in enumerate(lines):
        line = line.strip()
        GRID.append(line)
        dist.append([0] * len(line))
        if "S" in line:
            x = line.index("S")
            start = Coordinate(x, y)
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


def part2():
    with open("input.txt", "r") as f:
        lines = f.readlines()
    sums = 0
    # for i, line in enumerate(lines):
    #     rows = []
    #     nums = [int(n) for n in line.strip().split(" ") if n != ""]
    #     rows.append(nums)
    #     while not all([int(n) == 0 for n in nums]):
    #         # print(nums)
    #         temp = [0] * (len(nums) - 1)
    #         for j in range(1, len(nums)):
    #             temp[j - 1] = nums[j] - nums[j - 1]
    #         rows.append(temp)
    #         nums = temp
    #     rows.reverse()
    #     for i, row in enumerate(rows):
    #         if i == 0:
    #             rows[i].insert(0, 0)
    #         else:
    #             temp = rows[i][0] - rows[i - 1][0]
    #             rows[i].insert(0, temp)
    #     # print(rows)
    #     sums += rows[-1][0]
    print("Part 2: {}".format(sums))


part1()
part2()
