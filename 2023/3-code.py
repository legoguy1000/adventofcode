import re


def part1():
    data = []
    with open("3-input.txt", "r") as f:
        lines = f.readlines()
        for line_num, line in enumerate(lines[:35]):
            temp = []
            line = line.strip()
            line_length = len(line)
            nums = re.findall(r"\d+", line)
            num_index = 0
            for num in nums:
                i = line.index(num, num_index)
                num_index = i
                si = i - 1
                ei = i + len(num)
                if i == 0:
                    si = i
                if i + len(num) == line_length:
                    ei = line_length - 1
                print("{}  -  I: {}, SI: {}, EI: {}".format(num, i, si, ei))
                if re.match(r"[^\d\.]", line[si]):
                    print("start")
                    temp.append(int(num))
                elif re.match(r"[^\d\.]", line[ei]):
                    temp.append(int(num))
                    print("end")
                else:
                    print("else")
                    if line_num < (len(lines)-1):
                        print(lines[line_num+1][si:ei+1])
                    if line_num > 0:
                        print(lines[line_num-1][si:ei+1])
                    if line_num == 0 and len(re.findall(r"[^\d\.]", lines[line_num+1][si:ei+1])) > 0:
                        temp.append(int(num))
                    elif line_num == line_length - 1 and len(re.findall(r"[^\d\.]", lines[line_num-1][si:ei+1])) > 0:
                        temp.append(int(num))
                    elif len(re.findall(r"[^\d\.]", lines[line_num-1][si:ei+1])) > 0 or len(re.findall(r"[^\d\.]", lines[line_num+1][si:ei+1])) > 0:
                        temp.append(int(num))
                        # print("start to end top")
                        # print("start to end bottom")
            print(temp)
            data.append(sum(temp))
    print(data)
    print("Part 1: {}".format(sum(data)))


def part2():
    data1 = []
    with open("3-input.txt", "r") as f:
        for line in f.readlines():
            pass


part1()
part2()
