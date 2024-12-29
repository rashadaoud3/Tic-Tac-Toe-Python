# Rasha Daoud
# Created: 21 March 2023
# Email: rashadaoud134@gmail.com

from tkinter import *
import random

# Constants for players and colors
PLAYER_X = "x"
PLAYER_O = "o"
COLOR_WIN = "green"
COLOR_TIE = "yellow"

def next_turn(row, column):
    global player, x_wins, o_wins

    if buttons[row][column]['text'] == "" and check_winner() is False:

        buttons[row][column]['text'] = player

        winner = check_winner()

        if winner is False:
            player = PLAYER_O if player == PLAYER_X else PLAYER_X
            label.config(text=(player + " turn"))

        elif winner is True:
            if player == PLAYER_X:
                x_wins += 1
            else:
                o_wins += 1
            update_score()
            label.config(text=(player + " wins"))

        elif winner == "Tie":
            label.config(text="Tie!")

def check_rows():
    for row in buttons:
        if row[0]['text'] == row[1]['text'] == row[2]['text'] != "":
            for button in row:
                button.config(bg=COLOR_WIN)
            return True
    return False

def check_columns():
    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != "":
            for row in range(3):
                buttons[row][col].config(bg=COLOR_WIN)
            return True
    return False

def check_diagonals():
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg=COLOR_WIN)
        buttons[1][1].config(bg=COLOR_WIN)
        buttons[2][2].config(bg=COLOR_WIN)
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg=COLOR_WIN)
        buttons[1][1].config(bg=COLOR_WIN)
        buttons[2][0].config(bg=COLOR_WIN)
        return True
    return False

def check_winner():
    if check_rows() or check_columns() or check_diagonals():
        return True
    if not empty_spaces():
        for row in buttons:
            for button in row:
                button.config(bg=COLOR_TIE)
        return "Tie"
    return False

def empty_spaces():
    for row in buttons:
        for button in row:
            if button['text'] == "":
                return True
    return False

def reset_buttons():
    for row in buttons:
        for button in row:
            button.config(text="", bg="#F0F0F0")

def new_game():
    global player

    player = random.choice([PLAYER_X, PLAYER_O])
    label.config(text=player + " turn")
    reset_buttons()

def update_score():
    score_label.config(text=f"X Wins: {x_wins} | O Wins: {o_wins}")

window = Tk()
window.title("Tic-Tac-Toe")

player = random.choice([PLAYER_X, PLAYER_O])
x_wins = 0
o_wins = 0

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(text=player + " turn", font=('consolas', 40))
label.pack(side="top")

score_label = Label(text=f"X Wins: {x_wins} | O Wins: {o_wins}", font=('consolas', 20))
score_label.pack(side="top")

reset_button = Button(text="Restart", font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()

