import re


def part1():
    data = []
    with open("1-input.txt", "r") as f:
        for line in f.readlines():
            c = re.sub("[^\\d]", "", line)
            if len(c) == 1:
                data.append(int(c[0]+c[0]))
            else:
                data.append(int(c[0]+c[-1:]))
        print("Part 1: " + str(sum(data)))


def part2():
    data = []
    words = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }
    with open("1-input.txt", "r") as f:
        for line in f.readlines():
            line = line.strip()
            line_orig = line
            # print (line_orig)
            while True:
                word_index = {}
                for key, _ in words.items():
                    try:
                        i = line.index(key)
                        word_index[key] = i
                    except ValueError:
                        word_index[key] = 10000
                word_min = min(word_index, key=word_index.get)
                try:
                    line = line.replace(word_min, words.get(word_min), 1)
                    # print(line)
                except ValueError:
                    pass
                if all([val == 10000 for val in word_index.values()]):
                    break

            c = re.sub("[^\\d]", "", line)
            value = ""
            if len(c) == 1:
                value = c[0]+c[0]
            else:
                value = c[0]+c[-1:]
            # print(line_orig + " --- " + line + " ---  " + value)
            data.append(int(value))
        print("Part 2: " + str(sum(data)))


part1()
part2()
