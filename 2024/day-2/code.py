import copy
import os


def checksafe(values: list[int]) -> bool:
    diffs = []
    for i in range(1, len(values)):
        diffs.append(values[i] - values[i - 1])
    if diffs.count(0) > 0:
        return False
    elif (all([x > 0 for x in diffs]) or all([x < 0 for x in diffs])) and all(
        [abs(x) <= 3 for x in diffs]
    ):
        return True
    return False


def part1():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    safe_count = 0
    with open(dir_path + "/input.txt", encoding="utf-8") as f:
        for line in f.readlines():
            if line == "":
                continue
            values = list(map(int, line.split()))
            if checksafe(values=values):
                safe_count += 1
    print(f"Part1: The Sum is {safe_count}")


def part2():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    safe_count = 0
    with open(dir_path + "/input.txt", encoding="utf-8") as f:
        for line in f.readlines():
            if line == "":
                continue
            # print(line)
            values = list(map(int, line.split()))
            if checksafe(values=values):
                safe_count += 1
            else:
                for i in range(0, len(values)):
                    vals = copy.deepcopy(values)
                    vals.pop(i)
                    # print(vals)
                    if checksafe(values=vals):
                        safe_count += 1
                        break
    print(f"Part 2: The Sum is {safe_count}")


if __name__ == "__main__":
    part1()
    part2()
