from tkinter import *
from tkinter import messagebox

screen = Tk()
screen.title("Tic Tac Toe")
screen.geometry("510x530")
screen.configure(background = "yellow")
turn = "player 1"
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
player1_point = 0
player2_point = 0

def check_tie():
    if buttons == []:
        messagebox.showinfo("Game Over!", "Tie!")
        reset()

def reset():
    global board, turn, turn_indicator, buttons
    buttons = [bt1, bt2, bt3, bt4, bt5, bt6, bt7, bt8, bt9]
    for i in buttons:
        if i["text"] == "o" or i["text"] == "x":
            i["text"] = "-"
            i["bg"] = "black"
            i["fg"] = "white"
            board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
            turn = "player 1"
            turn_indicator["text"] = "Turn: Player 1"

def check_winnerV2():
    global player1_point, player2_point, player1_score, player2_score
    if board[0] == board[1] == board[2] and board[0] != "-" and board[1] != "-" and board[2] != "-":
        messagebox.showinfo("Game Over!", f"Player {board[0]} Win!")
        if board[0] == "o" and board[1] == "o" and board[2] == "o":
            player1_point += 1
            player1_score["text"] = player1_point
        elif board[0] == "x" and board[1] == "x" and board[2] == "x":
            player2_point += 1
            player2_score["text"] = player2_point
        reset()
        return
    elif board[3] == board[4] == board[5] and board[3] != "-" and board[4] != "-" and board[5] != "-":
        messagebox.showinfo("Game Over!", f"Player {board[3]} Win!")
        if board[3] == "o" and board[4] == "o" and board[5] == "o":
            player1_point += 1
            player1_score["text"] = player1_point
        elif board[3] == "x" and board[4] == "x" and board[5] == "x":
            player2_point += 1
            player2_score["text"] = player2_point
        reset()
        return
    elif board[6] == board[7] == board[8] and board[6] != "-" and board[7] != "-" and board[8] != "-":
        messagebox.showinfo("Game Over!", f"Player {board[7]} Win!")
        if board[6] == "o" and board[7] == "o" and board[8] == "o":
            player1_point += 1
            player1_score["text"] = player1_point
        elif board[6] == "x" and board[7] == "x" and board[8] == "x":
            player2_point += 1
            player2_score["text"] = player2_point
        reset()
        return
    elif board[0] == board[3] == board[6] and board[0] != "-" and board[3] != "-" and board[6] != "-":
        messagebox.showinfo("Game Over!", f"Player {board[6]} Win!")
        if board[0] == "o" and board[3] == "o" and board[6] == "o":
            player1_point += 1
            player1_score["text"] = player1_point
        elif board[0] == "x" and board[3] == "x" and board[6] == "x":
            player2_point += 1
            player2_score["text"] = player2_point
        reset()
        return
    elif board[1] == board[4] == board[7] and board[1] != "-" and board[4] != "-" and board[7] != "-":
        messagebox.showinfo("Game Over!", f"Player {board[1]} Win!")
        if board[1] == "o" and board[4] == "o" and board[7] == "o":
            player1_point += 1
            player1_score["text"] = player1_point
        elif board[1] == "x" and board[4] == "x" and board[7] == "x":
            player2_point += 1
            player2_score["text"] = player2_point
        reset()
        return
    elif board[2] == board[5] == board[8] and board[2] != "-" and board[5] != "-" and board[8] != "-":
        messagebox.showinfo("Game Over!", f"Player {board[5]} Win!")
        if board[2] == "o" and board[5] == "o" and board[8] == "o":
            player1_point += 1
            player1_score["text"] = player1_point
        elif board[2] == "x" and board[5] == "x" and board[8] == "x":
            player2_point += 1
            player2_score["text"] = player2_point
        reset()
        return
    elif board[0] == board[4] == board[8] and board[0] != "-" and board[4] != "-" and board[8] != "-":
        messagebox.showinfo("Game Over!", f"Player {board[4]} Win!")
        if board[0] == "o" and board[4] == "o" and board[8] == "o":
            player1_point += 1
            player1_score["text"] = player1_point
        elif board[0] == "x" and board[4] == "x" and board[8] == "x":
            player2_point += 1
            player2_score["text"] = player2_point
        reset()
        return
    elif board[2] == board[4] == board[6] and board[2] != "-" and board[4] != "-" and board[6] != "-":
        messagebox.showinfo("Game Over!", f"Player {board[2]} Win!")
        if board[2] == "o" and board[4] == "o" and board[6] == "o":
            player1_point += 1
            player1_score["text"] = player1_point
        elif board[2] == "x" and board[4] == "x" and board[6] == "x":
            player2_point += 1
            player2_score["text"] = player2_point
        reset()
        return

def update_bt(pos, btns):
    global turn, turn_indicator
    if btns["text"] == "-":
        if turn == "player 1":
            btns["text"] = "o"
            btns["bg"] = "blue"
            btns["fg"] = "yellow"
            board[pos] = "o"
            turn = "player 2"
            turn_indicator["text"] = "Turn: Player 2"

        elif turn == "player 2":
            btns["text"] = "x"
            btns["bg"] = "red"
            btns["fg"] = "green"
            board[pos] = "x"
            turn = "player 1"
            turn_indicator["text"] = "Turn: Player 1"
        
        buttons.remove(btns)
        check_winnerV2()
        check_tie()
    else:
        messagebox.showwarning("Oops!", "You can't pick the square that has already been picked!")

frame1 = Frame(screen, width = 120, height = 50)
frame2 = Frame(screen, width = 120, height = 50)
frame3 = Frame(screen, width = 120, height = 50)

frame1.pack(pady = 8)
frame2.pack(pady = 8)
frame3.pack(pady = 8)

title = Label(text = "Welcome to TicTacToe! (2 players)", font = ("arial", 24, "underline"), bg = "cyan")
title.pack()
turn_indicator = Label(text = "Turn: Player 1", font = ("arial", 24, "underline"), bg = "red")
turn_indicator.pack()

player1_score = Label(text = player1_point, font = ("arial", 24, "bold"), bg = "blue", fg = "white", width = 10)
player1_score.pack(side = LEFT)
player2_score = Label(text = player2_point, font = ("arial", 24, "bold"), bg = "red", fg = "white", width = 10)
player2_score.pack(side = RIGHT)

bt1 = Button(frame1, text = "-", fg = "white", width = 3, height = 1, bg = "black", font = 'Arial 42 bold', command = lambda: update_bt(0, bt1))
bt1.grid(row = 0, column = 1)
bt2 = Button(frame1, text = "-", fg = "white", width = 3, height = 1, bg = "black", font = 'Arial 42 bold', command = lambda: update_bt(1, bt2))
bt2.grid(row = 0, column = 2)
bt3 = Button(frame1, text = "-", fg = "white", width = 3, height = 1, bg = "black", font = 'Arial 42 bold', command = lambda: update_bt(2, bt3))
bt3.grid(row = 0, column = 3)
bt4 = Button(frame2, text = "-", fg = "white", width = 3, height = 1, bg = "black", font = 'Arial 42 bold', command = lambda: update_bt(3, bt4))
bt4.grid(row = 1, column = 1)
bt5 = Button(frame2, text = "-", fg = "white", width = 3, height = 1, bg = "black", font = 'Arial 42 bold', command = lambda: update_bt(4, bt5))
bt5.grid(row = 1, column = 2)
bt6 = Button(frame2, text = "-", fg = "white", width = 3, height = 1, bg = "black", font = 'Arial 42 bold', command = lambda: update_bt(5, bt6))
bt6.grid(row = 1, column = 3)
bt7 = Button(frame3, text = "-", fg = "white", width = 3, height = 1, bg = "black", font = 'Arial 42 bold', command = lambda: update_bt(6, bt7))
bt7.grid(row = 2, column = 1)
bt8 = Button(frame3, text = "-", fg = "white", width = 3, height = 1, bg = "black", font = 'Arial 42 bold', command = lambda: update_bt(7, bt8))
bt8.grid(row = 2, column = 2)
bt9 = Button(frame3, text = "-", fg = "white", width = 3, height = 1, bg = "black", font = 'Arial 42 bold', command = lambda: update_bt(8, bt9))
bt9.grid(row = 2, column = 3)

buttons = [bt1, bt2, bt3, bt4, bt5, bt6, bt7, bt8, bt9]

screen.mainloop()