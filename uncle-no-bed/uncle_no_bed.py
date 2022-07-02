"""
Simple script to figure out how often one should expect to win when playing
the card game with the unknown name dubbed 'Uncle does not want to go to bed'.

The rules are simple:
 - Start with one card on the table, and the rest in your hand.
 - Put the first card in your deck on the table to the right of the first one.
 - If the card has the same suit or value as the card to the left of it or the
   one three steps to the left you can put the card there instead.
 - If that changes anything such that the above is true for any other cards,
   you can do the same for those.
 - Continue adding cards on the right until you have no cards left in your
   hand.
 - If there is only one stack of cards left with all the cards in it you've
   won.

There are many strategies to choose from, and I've tried to implement a few
simple ones.

Which choices do we have?
1. Do we always move when we can? There will be situations where waiting for
the next card will allow us to end up with fewer stacks after the second card
than if we had moved beforehand. If we were counting cards, you could argue
that we could play the odds in the later stages of the game, hoping for the
right card, but I assume we're below that level.

2. If we can move two places, which one do we choose? On no information
other than my experience with playing the game, it seems the most successful
strategy is to minimize the number of stacks.

So what kind of move schemes can we do? There are a few options:
 - Move to the closest stack. (Naive)
 - Move to the stack three steps over. (Naive)
 - If the same suit, move at random/short/far. If different suit, pick same
   suit. (Here we try to maximize the number of possible matching cards)
 - Pick one of these schemes at random every time we have to choose. (Random
   things are rarely efficient)
 - Do the random one ten times and pick the one that gives the smallest number
   of stacks. (This one is stupidly inefficient.)

The more sophisticated approach - and the ones most humans probably end up
doing without even thinking about it - is to walk all possible paths, and
picking the one with the least stacks left on the table. This one is
significantly slower than the naive ways, but can be faster than the random one
in some cases.

Even so, it is probably the one that results in the most wins in the least
amount of time.

Made by: Andreas Ellewsen
Started: 30/07/19
"""

import datetime
import random

from strategies import move_all_paths
from strategies import move_card_simple_far
from strategies import move_card_simple_short
from strategies import move_min_stacks
from strategies import move_random


class Card(object):
    """Basic playing cards"""

    def __init__(self, suit, value):
        # Suit must be 0,1,2,3 representing D, H, C, S
        # Value must be 1 to 13
        self.suit = suit
        self.value = value

    def __repr__(self):
        if self.suit == 0:
            suit = 'H'
        elif self.suit == 1:
            suit = 'D'
        elif self.suit == 2:
            suit = 'C'
        elif self.suit == 3:
            suit = 'S'
        else:
            suit = str(self.suit)
        return ''.join((suit, str(self.value)))


class GamePlayer(object):
    def __init__(self, strategy):
        self.strategy = strategy

    def play_game(self, cards):
        table = [cards.pop()]
        while cards:
            table.append(cards.pop())
            table = self.strategy(table)
        if len(table) == 1:
            return True
        else:
            return False

    def __call__(self, cards):
        self.won = self.play_game(cards)


def play_with_stats(stats, cards, strategy):
    gp = GamePlayer(strategy)
    gp(cards.copy())
    if gp.won:
        stats.append(cards.copy())
    return stats


def print_stats(stats, n):
    print("     " + "    ".join(key for key in stats))
    print("Won " + "   ".join(("{:>3}".format(len(hands)) for _, hands in
                               stats.items())))
    print("Pct " + "   ".join(("{:>3}".format(len(hands) / n * 100) for
                               _, hands in stats.items())))
    print("Winning hands:")
    for strategy, hands in stats.items():
        print(strategy)
        for hand in hands:
            print(hand)


def main():
    """Test the various strategies and evaluate them"""
    # Stats variables
    t_start = datetime.datetime.now()
    stats = {'ms': [],
             'ss': [],
             'sf': [],
             'mr': [],
             'mp': [],
             }
    # Try a ton of hands with the different strategies and save some stats
    # about them
    n = int(1e5)
    cards = [Card(i, j) for i in range(0, 4) for j in range(1, 14)]
    for i in range(n):
        if i % 1000 == 0:
            print(i)
        # Shuffle cards
        random.shuffle(cards)
        # Move all paths
        try:
            stats['mp'] = play_with_stats(stats['mp'], cards, move_all_paths)
        except MemoryError:
            pass
        # Move min stacks
        stats['ms'] = play_with_stats(stats['ms'], cards, move_min_stacks)
        # Simple short
        stats['ss'] = play_with_stats(stats['ss'], cards,
                                      move_card_simple_short)
        # Simple far
        stats['sf'] = play_with_stats(stats['sf'], cards, move_card_simple_far)
        # Simple random
        stats['mr'] = play_with_stats(stats['mr'], cards, move_random)

    # Print stats
    t_stop = datetime.datetime.now()
    print("Took", (t_stop - t_start), 'to finish')
    print_stats(stats, n)


if __name__ == "__main__":
    main()
