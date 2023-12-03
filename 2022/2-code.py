"""
Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. 
"The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. 
The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
"""

rock = 1
paper = 2
scissors = 3
win = 6
draw = 3
lose = 0

alg = {
    "A": { # Rock
        "X": rock + draw,
        "Y": paper + win,
        "Z": scissors + lose
    },
    "B": { # Paper
        "X": rock + lose,
        "Y": paper + draw,
        "Z": scissors + win
    },
    "C": { # Scissors
        "X": rock + win,
        "Y": paper + lose,
        "Z": scissors + draw
    }
}

"""
The Elf finishes helping with the tent and sneaks back over to you. 
"Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"
"""
alg2 = {
    "A": { # Rock
        "X": scissors + lose,
        "Y": rock + draw,
        "Z": paper + win
    },
    "B": { # Paper
        "X": rock + lose,
        "Y": paper + draw,
        "Z": scissors + win
    },
    "C": { # Scissors
        "X": paper + lose,
        "Y": scissors + draw,
        "Z": rock + win
    }
}

score1 = 0
score2 = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        (oponent, me) = line.strip().split(" ")
        score1 += alg.get(oponent).get(me,0)
        score2 += alg2.get(oponent).get(me,0)
    print(f"Score 1: {score1}")
    print(f"Score 2: {score2}")