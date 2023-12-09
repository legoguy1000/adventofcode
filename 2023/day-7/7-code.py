import re
import math
from collections import Counter
from functools import cmp_to_key

strength1 = ["1","2","3","4","5","6","7","8","9","T","J","Q","K","A"]
strength2 = ["1","J","2","3","4","5","6","7","8","9","T","Q","K","A"]


def calc_hand(hand: str) -> int:
    counter = Counter(hand)
    counter_list = list(counter.items())
    if len(counter) == 1 and counter_list[0][1] == 5:  # 5 of a kind
        return 7
    if len(counter) == 2 and any(x[1] == 4 for x in counter_list):  # 4 of a kind
        return 6
    if len(counter) == 2 and any(x[1] == 3 or x[1] == 2 for x in counter_list):  # full house
        return 5
    if len(counter) == 3 and any(x[1] == 3 for x in counter_list) and len(list(filter(lambda x: x[1] == 1, counter_list))) == 2:  # 3 of a kind
        return 4
    if len(counter) == 3 and len(list(filter(lambda x: x[1] == 2, counter_list))) == 2:  # 2 pair
        return 3
    if len(counter) == 4 and len(list(filter(lambda x: x[1] == 2, counter_list))) == 1:  # 1 pair
        return 2
    if len(counter) == 5:  # high card
        return 1

class Hand:
    def __init__(self, hand: str, bid: str) -> None:
        self.hand = hand
        self.orig_hand = hand
        self.bid = int(bid)
        self.hand_type = 0
        self.hand_rank = 0
        self.backup_rank = [0] * 5

    def __repr__(self):
        return f"Hand({self.__str__()})"

    def __str__(self):
        return f"hand={self.hand}, bid={self.bid}, hand_typ={self.hand_type}, backup_rank={self.backup_rank}, hand_rank={self.hand_rank}"

    def calc_hand(self):
        self.hand_type = calc_hand(self.hand)

    def calc_backup_rank_part1(self):
        self.backup_rank = [strength1.index(x) for x in self.orig_hand]

    def calc_backup_rank_part2(self):
        self.backup_rank = [strength2.index(x) for x in self.orig_hand]

    def replace_j(self):
        if "J" not in self.hand:
            return
        ht = calc_hand(self.hand)
        top_hand = self.hand
        for card in ["2","3","4","5","6","7","8","9","T","Q","K","A"]:
            new_hand = self.hand.replace("J", card)
            nht = calc_hand(new_hand)
            if nht > ht:
                ht = nht
                top_hand = new_hand
        self.hand = top_hand


def compare_hand(hand1: Hand, hand2: Hand) -> int:
    if hand1.hand_type > hand2.hand_type:
        return 1
    elif hand1.hand_type < hand2.hand_type:
        return -1
    else:
        for i in range(0, len(hand1.backup_rank), 1):
            if hand1.backup_rank[i] > hand2.backup_rank[i]:
                return 1
            elif hand1.backup_rank[i] < hand2.backup_rank[i]:
                return -1
       

def part1():
    ranks = []
    with open("7-input.txt", "r") as f:
        lines = f.readlines()
    sum = 0
    for line in lines:
        cards, bid = line.split(" ")
        hand = Hand(cards, bid)
        hand.calc_hand()
        hand.calc_backup_rank_part1()
        ranks.append(hand)
        # print(hand)
    # ranks.sort(key=compare_hand)
    ranks_sorted = sorted(ranks, key=cmp_to_key(compare_hand))
    for i, hand in enumerate(ranks_sorted):
        sum += hand.bid * (i + 1)
    print("Part 1: {}".format(sum))


def part2():
    ranks = []
    with open("7-input.txt", "r") as f:
        lines = f.readlines()
    sum = 0
    for line in lines:
        cards, bid = line.split(" ")
        hand = Hand(cards, bid)
        hand.replace_j()
        hand.calc_hand()
        hand.calc_backup_rank_part2()        
        ranks.append(hand)
        # print(hand)
    # ranks.sort(key=compare_hand)
    ranks_sorted = sorted(ranks, key=cmp_to_key(compare_hand))
    for i, hand in enumerate(ranks_sorted):
        sum += hand.bid * (i + 1)
    print("Part 2: {}".format(sum))


part1()
part2()
