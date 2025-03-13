# Author
Rachel Curry
Created: Jan 27th, 2025
Last Updated: March 12th, 2025

# Requirements
Python 3 and Tkinter must be installed

# Setup
Clone the repo or download the files. Go to the directory and run python3 mainUI.py (the driver file)

# Gameplay
1. A popup window will appear asking if you want to play as x or o.
2. x always goes first. If you choose o, the cpu will go first.
3. This program uses the minimax algorithm, and the cpu will always win, or it will be a draw.
4. This minimax algorithm has, as of the last update (3/12/25), been updated to use alpha beta
pruning. This allows branches or parts of branches from the minimax tree to be eliminated
before they have to be evaluated fully, because there is a more optimal score that is already 
stored. It also now uses move ordering, which sorts the moves based on how they were previously
evaluated (i.e., which ones were the most optimal before), and allows pruning to happen earlier
in the evaluation, which in turn then checks less nodes. 


# OS Note
The tkinter button color functionality does not work in a macOS environment. This is a known issue 
about this library and I have not set up a workaround yet. 