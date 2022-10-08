"""
Simulation to get a feeling for how many points you can expect to get
per round if you just keep going until you lose
"""

import collections
import random
import statistics

POINTS: dict[tuple[int, ...], tuple[int, int]] = {
    # (Dice #, count): (score, # used die)
    (1, 1): (100, 1),
    (1, 2): (200, 2),
    (1, 3): (1000, 3),
    (1, 4): (2000, 4),
    (1, 5): (4000, 5),
    (1, 6): (8000, 6),
    (2, 3): (200, 3),
    (2, 4): (400, 4),
    (2, 5): (800, 5),
    (2, 6): (1600, 6),
    (3, 3): (300, 3),
    (3, 4): (600, 4),
    (3, 5): (1200, 5),
    (3, 6): (2400, 6),
    (4, 3): (400, 3),
    (4, 4): (800, 4),
    (4, 5): (1600, 5),
    (4, 6): (3200, 6),
    (5, 1): (50, 1),
    (5, 2): (100, 2),
    (5, 3): (500, 3),
    (5, 4): (1000, 4),
    (5, 5): (2000, 5),
    (5, 6): (4000, 6),
    (6, 3): (600, 3),
    (6, 4): (1200, 4),
    (6, 5): (2400, 5),
    (6, 6): (4800, 6),
}


def throw_n_dice(n: int) -> tuple[int]:
    """Get a tuple of length n with ints 1 to 6"""
    return tuple(sorted([random.randint(1, 6) for _ in range(n)]))


def is_three_pairs(die: tuple[int, ...]) -> bool:
    """Check if we got three pairs"""
    counts = collections.Counter(die)
    if len(counts.keys()) != 3:
        return False
    for v in counts.values():
        if v != 2:
            return False
    return True


def is_straight(die: tuple[int, ...]) -> bool:
    """Check if we got straight"""
    return die == (1, 2, 3, 4, 5, 6)


def collect_points(die: tuple[int, ...]) -> tuple[int, int]:
    """Figure out how many points we got from this set of die"""
    points = 0
    used_die = 0
    if len(die) == 6:
        if is_three_pairs(die):
            return 1500, 6
        if is_straight(die):
            return 2000, 6
    for i in (1, 2, 3, 4, 5, 6):
        count = die.count(i)
        result = POINTS.get((i, count))
        if result:
            points += result[0]
            used_die += result[1]
    return points, used_die


def play_game():
    """
    Play until you lose and return how many points you had before
    losing
    """
    has_lost = False
    points = 0
    saved_die = 0
    while not has_lost:
        if saved_die == 6:
            saved_die = 0
        die = throw_n_dice(6 - saved_die)
        earned_points, n_used_die = collect_points(die)
        if earned_points == 0:
            has_lost = True
            break
        points += earned_points
        saved_die += n_used_die
    return points


def main():
    """
    Play a ton of games and spit out some useful statistics
    """
    scores = []
    for _ in range(100_000):
        points = play_game()
        scores.append(points)
    print("fmean: ", statistics.fmean(scores))
    print("median: ", statistics.median(scores))
    print("quantiles: ", statistics.quantiles(scores, n=4))


if __name__ == "__main__":
    main()
