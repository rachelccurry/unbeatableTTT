# Rachel Curry
# Clean Coders Pre-Interview Exercise
# Tic-Tac-Toe Game - Unbeatable
# January 27th, 2025
# Version with a non-console UI

import tkinter as tk
from tkinter import messagebox

class unbeatableTTTGameUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.root.resizable(False, False)
        self.center_window()
        self.root.withdraw()

        self.board = [["" for i in range(3)] for j in range(3)]
        self.player = ""
        self.cpu = ""
        self.current_player = ""

        self.buttons = [[None for i in range(3)] for j in range(3)]
        
        self.board_setup()
        self.choose_player()

    def center_window(self):
        window_width = 400
        window_height = 450

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        self.root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
    
    def board_setup(self):
        for row in range(3):
            self.root.grid_rowconfigure(row, weight=1, minsize=100)
        for col in range(3):
            self.root.grid_columnconfigure(col, weight=1, minsize=100)
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text="", font=("Arial", 24), width=5, height=2,
                            command=lambda r=row, c=col: self.on_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button
    
    def choose_player(self):
        def set_player(player_choice):
            self.player = player_choice
            self.cpu = "o" if player_choice == "x" else "x"
            self.current_player = "x"

            popup.destroy()
            self.root.deiconify()

            if self.cpu == "x":
                self.root.after(500, self.cpu_move)

        def on_close():
            self.root.quit()
        
        popup = tk.Toplevel(self.root)
        popup.title("Choose a Letter (x goes first)")

        popup.resizable(False, False)
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        popup_width = 350
        popup_height = 150
        position_top = (screen_height // 2) - (popup_height // 2)
        position_left = (screen_width // 2) - (popup_width // 2)
        popup.geometry(f"{popup_width}x{popup_height}+{position_left}+{position_top}")

        frame = tk.Frame(popup)
        frame.pack(expand=True)

        button_frame = tk.Frame(frame)
        button_frame.pack(pady=5)

        tk.Button(button_frame, text="x", font=("Arial", 14), command=lambda: set_player("x")).pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="o", font=("Arial", 14), command=lambda: set_player("o")).pack(side=tk.RIGHT, padx=10)

        popup.protocol("WM_DELETE_WINDOW", on_close)

    def on_click(self, row, col):
        if self.board[row][col] == "" and self.current_player == self.player:
            self.board[row][col] = self.player
            self.buttons[row][col]["text"] = self.player

            winner = self.find_winner()
            if winner:
                messagebox.showinfo(message="It's over - " + winner + " wins")
                self.reset_board()
                return
            elif self.is_draw():
                messagebox.showinfo(message="ew a draw")
                self.reset_board()
                return
            else:
                self.current_player = self.cpu
                self.root.after(500, self.cpu_move)
 
    def minimax(self, depth, is_maximizing):
        winner = self.find_winner()
        if winner == self.cpu:
            return 10 - depth
        elif winner == self.player:
            return depth - 10
        elif self.is_draw():
            return 0

        if is_maximizing: # cpu move
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == "":
                        self.board[i][j] = self.cpu # try a move
                        score = self.minimax(depth + 1, False) # recursion
                        self.board[i][j] = ""  # undo the move
                        best_score = max(score, best_score)
            return best_score
        else: # user move
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == "":
                        self.board[i][j] = self.player
                        score = self.minimax(depth + 1, True)
                        self.board[i][j] = ""
                        best_score = min(score, best_score)
            return best_score

    def cpu_move(self):
        best_score = -float('inf')
        best_move = None

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "": 
                    self.board[i][j] = self.cpu # try a move
                    score = self.minimax(0, False) # call the minimax logic method
                    self.board[i][j] = "" # undo the move
                    
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        if best_move:
            row, col = best_move
            self.board[row][col] = self.cpu
            self.buttons[row][col]["text"] = self.cpu

            winner = self.find_winner()
            if winner:
                messagebox.showinfo(message="It's over - " + winner + " wins")
                self.reset_board()
                return
            elif self.is_draw():
                messagebox.showinfo(message="ew a draw")
                self.reset_board()
                return
            else:
                self.current_player = self.player

    def is_draw(self):
        board_full = True
        for row in self.board:
            for cell in row:
                if cell == "":
                    board_full = False

        winner = self.find_winner()

        if board_full and winner == None:
            return True
        else:
            return False
  
    def find_winner(self):
        if self.check_diagonals():
            winner = self.check_diagonals()
        elif self.check_rows_cols():
            winner = self.check_rows_cols()
        else:
            winner = None
        return winner
    
    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.board[row][col] = ""
                self.buttons[row][col]["text"] = ""
        self.play_again()

    def play_again(self):
        answer = messagebox.askyesno("Game Over", "Do you want to play again?")
        if answer:
            self.choose_player()
        else:
            self.root.quit()

    def check_rows_cols(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return self.board[0][i]
        return None
            
    def check_diagonals(self):
        if self.board[0][0] == self.board[1][1] == self.board [2][2] != "":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return self.board[0][2]
        return None