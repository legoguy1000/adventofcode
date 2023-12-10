

def part1():
    with open("input.txt", "r") as f:
        lines = f.readlines()
    sums = 0
    for i, line in enumerate(lines):
        rows = []
        nums = [int(n) for n in line.strip().split(" ")]
        rows.append(nums)
        while not all([int(n) == 0 for n in nums]):
            # print(nums)
            temp = [0] * (len(nums) - 1)
            for j in range(1, len(nums)):
                temp[j - 1] = nums[j] - nums[j - 1]
            rows.append(temp)
            nums = temp
        rows.reverse()
        for i, row in enumerate(rows):
            if i == 0:
                rows[i].append(0)
            else:
                temp = rows[i][-1] + rows[i - 1][-1]
                rows[i].append(temp)
        # print(rows)
        sums += rows[-1][-1]
    print("Part 1: {}".format(sums))


def part2():
    with open("input.txt", "r") as f:
        lines = f.readlines()
    sums = 0
    for i, line in enumerate(lines):
        rows = []
        nums = [int(n) for n in line.strip().split(" ") if n != ""]
        rows.append(nums)
        while not all([int(n) == 0 for n in nums]):
            # print(nums)
            temp = [0] * (len(nums) - 1)
            for j in range(1, len(nums)):
                temp[j - 1] = nums[j] - nums[j - 1]
            rows.append(temp)
            nums = temp
        rows.reverse()
        for i, row in enumerate(rows):
            if i == 0:
                rows[i].insert(0, 0)
            else:
                temp = rows[i][0] - rows[i - 1][0]
                rows[i].insert(0, temp)
        # print(rows)
        sums += rows[-1][0]
    print("Part 2: {}".format(sums))


part1()
part2()
