import os
import itertools
from operator import mul

def sumnum(x,y) -> int:
    return x + y

def concat(x,y) -> int:
    return int(str(x)+str(y))

def check_equation(data: dict, funcs: list) -> bool:
    permutations = list(itertools.product(funcs, repeat=len(data["vals"])-1))
    for perm in permutations:
        total = data["vals"][0]
        i = 1
        for fn in perm:
            total = fn(total, data["vals"][i])
            i += 1
        if total == data["total"]:
            return True
    return False


def part1():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    sum = 0
    with open(dir_path + "/input.txt", encoding="utf-8") as f:
        for line in f.readlines():
            total, vals = line.split(":")
            if check_equation({
                "total": int(total),
                "vals": list(map(int, vals.strip().split(" ")))
            }, [sumnum, mul]):
                sum += int(total)
            

    print(f"Part1: The Sum is {sum}")


def part2():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    sum = 0
    with open(dir_path + "/input.txt", encoding="utf-8") as f:
        for line in f.readlines():
            total, vals = line.split(":")
            if check_equation({
                "total": int(total),
                "vals": list(map(int, vals.strip().split(" ")))
            }, [sumnum, mul, concat]):
                sum += int(total)
    print(f"Part 2: The Sum is {sum}")


if __name__ == "__main__":
    part1()
    part2()
