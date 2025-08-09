import tkinter as tk
from tkinter import messagebox
import random

# Initialize main window
root = tk.Tk()
root.title("Tic-Tac-Toe 🏆")

# Game variables
current_player = "X"
buttons = [[None for _ in range(3)] for _ in range(3)]
game_mode = None  # "computer" or "2player"

# Function to check winner
def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    return False

# Function for computer move
def computer_move():
    empty_cells = [(r, c) for r in range(3) for c in range(3) if buttons[r][c]["text"] == ""]
    if empty_cells:
        row, col = random.choice(empty_cells)
        buttons[row][col]["text"] = "O"
        if check_winner():
            messagebox.showinfo("Game Over", "Computer wins! 🤖🏆")
            reset_board()
            return
        elif all(buttons[r][c]["text"] != "" for r in range(3) for c in range(3)):
            messagebox.showinfo("Game Over", "It's a tie! 🤝")
            reset_board()

# Button click handler
def on_click(row, col):
    global current_player
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player

        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} wins! 🎉")
            reset_board()
            return
        elif all(buttons[r][c]["text"] != "" for r in range(3) for c in range(3)):
            messagebox.showinfo("Game Over", "It's a tie! 🤝")
            reset_board()
            return

        if game_mode == "2player":
            current_player = "O" if current_player == "X" else "X"
        elif game_mode == "computer":
            computer_move()

# Reset the board
def reset_board():
    global current_player
    current_player = "X"
    for r in range(3):
        for c in range(3):
            buttons[r][c]["text"] = ""

# Function to start the game
def start_game(mode):
    global game_mode
    game_mode = mode
    menu_frame.pack_forget()
    game_frame.pack()

# Create menu frame
menu_frame = tk.Frame(root)
tk.Label(menu_frame, text="🎯 Choose Game Mode", font=("Arial", 16)).pack(pady=10)
tk.Button(menu_frame, text="Play with Computer 🤖", font=("Arial", 14), command=lambda: start_game("computer")).pack(pady=5)
tk.Button(menu_frame, text="Pass and Play 👥", font=("Arial", 14), command=lambda: start_game("2player")).pack(pady=5)
menu_frame.pack()

# Create game frame
game_frame = tk.Frame(root)
for r in range(3):
    for c in range(3):
        buttons[r][c] = tk.Button(game_frame, text="", font=("Arial", 20), width=5, height=2,
                                  command=lambda r=r, c=c: on_click(r, c))
        buttons[r][c].grid(row=r, column=c)

root.mainloop()
