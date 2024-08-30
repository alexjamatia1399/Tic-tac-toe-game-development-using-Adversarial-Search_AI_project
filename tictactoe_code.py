from tkinter import*

root = Tk()
root.geometry("500x500")
root.title("Tic Tac Toe")

frame1 = Frame(root)
frame1.pack()
titleLabel = Label(frame1, text="TIC-TAC-TOE", font=("Arial Rounded MT Bold",25), bg="blue", fg="white")
titleLabel.pack()

frame2 = Frame(root)
frame2.pack()

board = {1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ", 9:" "}
over = 0
turn = "X"


def winner(player):
    if board[1]==player and board[2]==player and board[3]==player :
        return True
    elif board[4]==player and board[5]==player and board[6]==player :
        return True
    elif board[7]==player and board[8]==player and board[9]==player :
        return True
    elif board[1]==player and board[4]==player and board[7]==player :
        return True
    elif board[2]==player and board[5]==player and board[8]==player :
        return True
    elif board[3]==player and board[6]==player and board[9]==player :
        return True
    elif board[1]==player and board[5]==player and board[9]==player :
        return True
    elif board[3]==player and board[5]==player and board[7]==player :
        return True
    
def draw():
    for i in range(1,10):
        if board[i] == " ":
            return False
    return True


def Minimax(board, AIturn, alpha, beta):
    if winner("O"):
        return 1
    if winner("X"):
        return -1
    if draw():
        return 0
    if AIturn:
        bestScore = -2
        for i in range(1, 10):
            if board[i] == " ":
                board[i] = "O"
                score = Minimax(board, False, alpha, beta)
                board[i] = " "
                bestScore = max(bestScore, score)
                alpha = max(alpha, bestScore)
                if beta <= alpha:
                    break
        return bestScore
    else:
        bestScore = 2
        for i in range(1, 10):
            if board[i] == " ":
                board[i] = "X"
                score = Minimax(board, True, alpha, beta)
                board[i] = " "
                bestScore = min(bestScore, score)
                beta = min(beta, bestScore)
                if beta <= alpha:
                    break
        return bestScore



def playAI():
    bestScore = -2
    best = 0
    alpha = -10
    beta = 10
    for i in range(1,10):
        if board[i]==" ":
            board[i] = "O"
            score = Minimax(board, False, alpha, beta)
            board[i] = " "
            if score > bestScore:
                bestScore = score
                best = i
    board[best] = "O"


def play(event):
    global turn
    global board
    global over
    button = event.widget
    btntxt = str(button)
    btn = btntxt[-1]
    if btn == "n":
        btn = 1
    else:
        btn = int(btn)
    
    if button["text"] == " " and over==0:
        if turn == "X":
            button["text"] = "X"
            board[btn] = turn
            if winner(turn):
                winLabel = Label(frame2, text=f"{turn} WINS", bg="blue", fg="white", font=("Arial Rounded MT Bold", 25))
                winLabel.grid(row=3, column=0, columnspan=3)
                over = 1
            elif draw():
                winLabel = Label(frame2, text=f"IT'S A DRAW", bg="blue", fg="white", font=("Arial Rounded MT Bold", 25))
                winLabel.grid(row=3, column=0, columnspan=3)
                over = 1
            turn = "O"
            
            playAI()
            if winner(turn):
                winLabel = Label(frame2, text=f"{turn} WINS", bg="blue", fg="white", font=("Arial Rounded MT Bold", 25))
                winLabel.grid(row=3, column=0, columnspan=3)
                over = 1
            elif draw():
                winLabel = Label(frame2, text=f"IT'S A DRAW", bg="blue", fg="white", font=("Arial Rounded MT Bold", 25))
                winLabel.grid(row=3, column=0, columnspan=3)
                over = 1
            turn = "X"
            
            for i in range(1,10):
                buttons[i-1]["text"] = board[i]
        


def restart():
    global board
    global turn
    global over
    for i in range(1,10):
        board[i] = " "
    for btn in buttons:
        btn["text"] = " "
    over = 0
    turn  = "X" 
    winLabel = Label(frame2, text="", width=30, height=3, bg="white")
    winLabel.grid(row=3, column=0, columnspan=3)


btn1 = Button(frame2, text=" ", width=4, height=2, font=("Monospace", 25), bg="blue", fg="white", relief=RAISED, borderwidth=5)
btn1.grid(row=0, column=0)
btn1.bind("<Button-1>", play)
btn2 = Button(frame2, text=" ", width=4, height=2, font=("Monospace", 25), bg="blue", fg="white", relief=RAISED, borderwidth=5)
btn2.grid(row=0, column=1)
btn2.bind("<Button-1>", play)
btn3 = Button(frame2, text=" ", width=4, height=2, font=("Monospace", 25), bg="blue", fg="white", relief=RAISED, borderwidth=5)
btn3.grid(row=0, column=2)
btn3.bind("<Button-1>", play)
btn4 = Button(frame2, text=" ", width=4, height=2, font=("Monospace", 25), bg="blue", fg="white", relief=RAISED, borderwidth=5)
btn4.grid(row=1, column=0)
btn4.bind("<Button-1>", play)
btn5 = Button(frame2, text=" ", width=4, height=2, font=("Monospace", 25), bg="blue", fg="white", relief=RAISED, borderwidth=5)
btn5.grid(row=1, column=1)
btn5.bind("<Button-1>", play)
btn6 = Button(frame2, text=" ", width=4, height=2, font=("Monospace", 25), bg="blue", fg="white", relief=RAISED, borderwidth=5)
btn6.grid(row=1, column=2)
btn6.bind("<Button-1>", play)
btn7 = Button(frame2, text=" ", width=4, height=2, font=("Monospace", 25), bg="blue", fg="white", relief=RAISED, borderwidth=5)
btn7.grid(row=2, column=0)
btn7.bind("<Button-1>", play)
btn8 = Button(frame2, text=" ", width=4, height=2, font=("Monospace", 25), bg="blue", fg="white", relief=RAISED, borderwidth=5)
btn8.grid(row=2, column=1)
btn8.bind("<Button-1>", play)
btn9 = Button(frame2, text=" ", width=4, height=2, font=("Monospace", 25), bg="blue", fg="white", relief=RAISED, borderwidth=5)
btn9.grid(row=2, column=2)
btn9.bind("<Button-1>", play)

winLabel = Label(frame2, text="", width=30, height=3, bg="white")
winLabel.grid(row=3, column=0, columnspan=3)

buttons = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]

btnrestart = Button(frame2, text="RESTART", width=12, height=1, font=("Arial Rounded MT Bold", 20), 
                    bg="blue", fg="white", relief=RAISED, borderwidth=5, command=restart)
btnrestart.grid(row=4, column=0, columnspan=3)

root.mainloop()








