import random
import numpy as np
from war import WarGame
import time
# Set up a deck and shuffle it
deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4,
        5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7,
        8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10,
        11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13,
        14, 14, 14, 14]

# Variables and empty lists
n = 10000  # Number of simulations
seeds = np.empty((n, 52), dtype=int)
won_games = np.empty(n)
counts = np.empty(n)
t1 = time.time()  # start timer

# Play n games and shuffle the deck each time.
for i in range(n):
    random.shuffle(deck)  # Shuffle
    current_game = WarGame(deck)  # Initialize game
    seeds[i] = deck.copy()  # Save a copy of the deck.
    won_games[i] = current_game.winnable  # Save winnable or not
    counts[i] = current_game.counter  # Save count

# Write to file
# t3 = time.time()
with open('seeds.txt', 'ab') as f:
    np.savetxt(f, seeds, fmt='%i')  # , header='Seed')
with open('counts.txt', 'ab') as f:
    np.savetxt(f, counts, fmt='%i#')  # , header='Counts')
with open('wins.txt', 'ab') as f:
    np.savetxt(f, won_games, fmt='%i')  # , header='Win/Lose')

# t4 = time.time()
# print('Took ' + '%.2f' % (t4-t3) + ' seconds to save to file')

t2 = time.time()  # End timer
print('Took ' + '%.2f' % (t2-t1) + ' seconds to run ' + str(n) + ' iterations')
