import os

def getlast(arr: list) -> int:
    i = len(arr) - 1
    for item in arr[::-1]:
        if item != ".":
            return i
        else:
            i -= 1

def part1():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    total = 0
    with open(dir_path + "/input.txt", encoding="utf-8") as f:
        line = f.readline()
        arr = []
        id = 0
        for i in range(0,len(line)):
            if i % 2 == 0:
                arr.extend([str(id)]*int(line[i]))
                id += 1
            else:
                arr.extend(["."]*int(line[i]))
        print(arr)
        last = len(arr)
        for i in range(0,len(arr)):
            if arr[i] == ".":
                if i >= last:
                    print(arr)
                    break
                last = getlast(arr)
                arr[i], arr[last] = arr[last], "."
        total = sum([int(arr[i]) * i for i in range(0,len(arr)) if arr[i] != "."])

    print(f"Part1: The Sum is {total}")


def part2():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    sum = 0
    sum = 0
    with open(dir_path + "/input.txt", encoding="utf-8") as f:
        line = f.readline()
        
    print(f"Part 2: The Sum is {sum}")


if __name__ == "__main__":
    part1()
    part2()
