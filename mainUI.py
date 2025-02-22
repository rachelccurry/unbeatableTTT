# Rachel Curry
# Clean Coders Pre-Interview Exercise
# Tic-Tac-Toe Game - Unbeatable
# January 27th, 2025
# driver file for non-console version

import tkinter as tk
import unbeatableTTT_UI as ttt

if __name__ == "__main__":

    root = tk.Tk()
    game = ttt.unbeatableTTTGameUI(root)
    root.mainloop()