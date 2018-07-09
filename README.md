# WarGame
This repository contains code to simulate the card game war and some ML analysis on the output to predict whether the game will finish or not. 

# War.py
Class which when initialized with a seed of cards simulates a game of war.
Assume no shuffling. The game ends when a player has either too few cards for war or no cards left.
The game also ends if no player has won in 10,000 turns. 
Saves whether the game is winnable or not, as well the turn count needed to finish. 

# main.py
Runs n simulations of WarGame and saves the seeds, turns needed for someone to win, as well as whether the game is winnable or not.

# MLanalysis.py
Reeds the output files of main.py and tests some basic ML algorithms on the ouput.
