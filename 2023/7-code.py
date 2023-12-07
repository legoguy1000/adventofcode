import re
import math
from collections import Counter

strength = ["1","2","3","4","5","6","7","8","9","T","J","Q","K","A"]

class Hand:
    def __init__(self, hand: str, bid: str) -> None:
        self.hand = hand
        self.bid = int(bid)
        self.hand_type = 0
        self.hand_rank = 0
        self.backup_rank = 0
    
    def calc_hand(self):
        counter = Counter(self.hand)
        if len(counter) == 1 and counter[1] == 5:
            self.hand_type = 7
        if len(counter) == 2 and any(x[1] == 4 for x in counter):
            self.hand_type = 6
        if len(counter) == 2 and any(x[1] == 3 or x[1] == 2 for x in counter):
            self.hand_type = 5
        if len(counter) == 3 and any(x[1] == 3 for x in counter) and len([x[1] == 1 for x in counter]) == 2:
            self.hand_type = 4
        if len(counter) == 3 and len([x[1] == 2 for x in counter]) == 2:
            self.hand_type = 3
        if len(counter) == 4 and len([x[1] == 2 for x in counter]) == 1:
            self.hand_type = 2
        if len(counter) == 5:
            self.hand_type = 1
    
    def calc_backup_rank(self):
        

def part1():
    with open("7-input.txt", "r") as f:
        lines = f.readlines()
    bids = {}
    for line in lines:
        cards, bid = line.split(" ")
        bids[cards] = int(bid)


    

    print("Part 1: {}".format(math.prod(data)))


def part2():
    with open("7-input.txt", "r") as f:
        lines = f.readlines()
    # times = re.findall(r"\d+", lines[0].replace(" ", ""))
    # distances = re.findall(r"\d+", lines[1].replace(" ", ""))
    # time = int(times[0])
    # distance = int(distances[0])
    # print(times)
    # print(distance)
    # data = 0
    # for j in range(0, time + 1, 1):
    #     d = j * (time - j)
    #     if d > distance:
    #         data += 1

    # print("Part 2: {}".format(data))


part1()
part2()
