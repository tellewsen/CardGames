"""
Rules (in norwegian)
"""

import random
import sys

from numpy import average

MAX_ROUNDS = 3
INITIAL_DICE_N = 6
LOST_DICE = {1, 6}


def throw_dice(n):
    return (random.randint(1, 6) for _ in range(n))


def play_round():
    score = 0
    n_remaining_dice = INITIAL_DICE_N
    for _ in range(MAX_ROUNDS):
        for die in throw_dice(n_remaining_dice):
            if die in LOST_DICE:
                n_remaining_dice -= 1
            else:
                score += die
    score += sum(throw_dice(INITIAL_DICE_N - n_remaining_dice))
    return score


def main():
    n_games = int(sys.argv[1])
    scores = [play_round() for _ in range(n_games)]
    print(f"Average score of {n_games} rounds: {average(scores)}")


if __name__ == "__main__":
    main()
