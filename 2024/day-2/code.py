import os


def part1():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    safe_count = 0
    with open(dir_path + "/input.txt", encoding="utf-8") as f:
        for line in f.readlines():
            if line == "":
                continue
            values = list(map(int, line.split()))
            increasing = False
            decreasing = False
            safe = False
            if values[1] - values[0] > 0 and abs(values[0] - values[1]) <= 3:
                increasing = True
            elif values[1] - values[0] < 0 and abs(values[0] - values[1]) <= 3:
                decreasing = True
            else:
                continue
            for i in range(2, len(values)):
                if (
                    increasing
                    and values[i] - values[i - 1] > 0
                    and abs(values[i] - values[i - 1]) <= 3
                    and abs(values[i] - values[i - 1]) > 0
                ):
                    safe = True
                elif (
                    decreasing
                    and values[i] - values[i - 1] < 0
                    and abs(values[i] - values[i - 1]) <= 3
                    and abs(values[i] - values[i - 1]) > 0
                ):
                    safe = True
                else:
                    safe = False
                    break
            if safe:
                safe_count += 1
    print(f"Part1: The Sum is {safe_count}")


def part2():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    safe_count = 0
    with open(dir_path + "/input.txt", encoding="utf-8") as f:
        for line in f.readlines():
            if line == "":
                continue
            print(line)
            values = list(map(int, line.split()))
            increasing = False
            decreasing = False
            safe = False
            unsafe_indicators = 0
            if values[1] - values[0] > 0 and abs(values[0] - values[1]) <= 3:
                increasing = True
            elif values[1] - values[0] < 0 and abs(values[0] - values[1]) <= 3:
                decreasing = True
            else:
                unsafe_indicators += 1
            for i in range(2, len(values)):
                # print(f"{values[i]} {values[i - 1]}")
                if (
                    increasing
                    and values[i] - values[i - 1] > 0
                    and abs(values[i] - values[i - 1]) <= 3
                    and abs(values[i] - values[i - 1]) > 0
                ):
                    safe = True
                    # print("1")
                elif (
                    decreasing
                    and values[i] - values[i - 1] < 0
                    and abs(values[i] - values[i - 1]) <= 3
                    and abs(values[i] - values[i - 1]) > 0
                ):
                    safe = True
                    # print("2")
                else:
                    unsafe_indicators += 1
                    # print("3")
                if unsafe_indicators > 1:
                    safe = False
                    break
            print(safe)
            if safe:
                safe_count += 1
    print(f"Part 2: The Sum is {safe_count}")


if __name__ == "__main__":
    part1()
    part2()
