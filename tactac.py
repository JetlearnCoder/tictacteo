import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
board = []

def check_winner(board,player):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            return True
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column]:
            return True
    if board[2][0] == board[1][1] == board[0][2]:
        return True 
    if board[0][0] == board[1][1] == board[2][2]:
        return True
    return False
    
def create_gameboard():
    board = [[" "," "," "], #1st row
             [" "," "," "], #2nd row
             [" "," "," "]] #3rd row

    current_player = "X"

    def handle_click(row,column):
        nonlocal current_player,board
        #checks if the selected button value is empty
        if board[row][column] == " ":
            board[row][column] = current_player
            button = buttons[row][column]
            button["text"] = current_player
            button["state"] = "disabled"
            if check_winner(board,current_player):
                messagebox.showinfo("Winner Screen",f"Player{current_player}Wins!")
            else:
                current_player = "O" if current_player == "X" else "X"
                                        

    buttons = [] 
    for i in range(3):
        row = []
        for j in range(3):
            button = tk.Button(window, text = " ", width = 15, height = 6, command = lambda row = i, col = j:handle_click(row,col))
            button.grid(row = i, column = j)
            row.append(button)
        buttons.append(row)


create_gameboard()

window.mainloop()
    