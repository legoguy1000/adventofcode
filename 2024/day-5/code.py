import os


def check_rule(update: list[str], rule: list[str]) -> bool:
    if not all([x in update for x in rule]):
        return True
    if update.index(rule[0]) < update.index(rule[1]):
        return True
    return False


def part1():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    sum = 0
    rules = []
    updates = []
    with open(dir_path + "/input.txt", encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip()
            if line == "":
                continue
            elif "|" in line:
                rules.append(line.split("|"))
            elif "," in line:
                updates.append(line.split(","))
    for update in updates:
        validupdate = True
        for rule in rules:
            if not check_rule(update, rule):
                validupdate = False
                break
        if validupdate:
            middle = int(len(update) / 2)
            sum += int(update[middle])
    print(f"Part1: The Sum is {sum}")


def part2():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    sum = 0
    rules = []
    updates = []
    badupdates = []
    with open(dir_path + "/input.txt", encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip()
            if line == "":
                continue
            elif "|" in line:
                rules.append(line.split("|"))
            elif "," in line:
                updates.append(line.split(","))
    for update in updates:
        for rule in rules:
            if not check_rule(update, rule):
                badupdates.append(update)
                break
    for update in badupdates:
        # print(update)
        for i in range(len(update)):
            for rule in rules:
                if not all([x in update for x in rule]):
                    continue
                if update.index(rule[0]) > update.index(rule[1]):
                    update.insert(
                        update.index(rule[0]), update.pop(update.index(rule[1]))
                    )
        middle = int(len(update) / 2)
        sum += int(update[middle])
    print(f"Part 2: The Sum is {sum}")


if __name__ == "__main__":
    part1()
    part2()
