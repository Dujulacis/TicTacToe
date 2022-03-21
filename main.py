from cgitb import strong
from tabnanny import check
from tkinter import*
from tkinter import messagebox #messages
mW=Tk()
mW.title("TicTacToe")
speletajsX=True
speletajsXX=0
speletajsOO=0
count=0

def infoLogs():
    newWindow=Toplevel()
    newWindow.title('About the game')
    newWindow.geometry("300x300")
    title=Label(newWindow, text="TIC TAC TOE", font=(23))
    desc=Label(newWindow, text="The game is played on a grid thats 3 squares by 3 squares. You are X, your friend is O. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner. If someone wins, the players change sides. When all 9 squares are full, the game is over. ", wraplength=300, justify="left", font=(18))
    credits=Label(newWindow, text="Made by duja", font=(16), )
    title.grid(row=0, column=0)
    desc.grid(row=1,column=0)
    credits.grid(row=2, column=0)
    return 0

def reset():
    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)
    btn6.config(state=NORMAL)
    btn7.config(state=NORMAL)
    btn8.config(state=NORMAL)
    btn9.config(state=NORMAL)

    btn1["text"]=""
    btn2["text"]=""
    btn3["text"]=""
    btn4["text"]=""
    btn5["text"]=""
    btn6["text"]=""
    btn7["text"]=""
    btn8["text"]=""
    btn9["text"]=""

    global winner, count, speletajsX, speletajsXX, speletajsOO
    winner=False
    count=0
    if speletajsXX==1:
        speletajsX=False
    elif speletajsOO==1:
        speletajsX==True
    speletajsXX=0
    speletajsOO=0
    return 0

def btnClick(button):
    global speletajsX, count
    if button["text"]=="" and speletajsX==True: #player
        button["text"]="X"
        speletajsX=False #players turn ends
        count+=1 #+1 
        checkWinner()
    elif button["text"]=="" and speletajsX==False:
        button["text"]="O"
        speletajsX=True
        count+=1
        checkWinner()
    else:
        messagebox.showerror("TicTacToe", "Someone already clicked here!")

def disButtons():
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)
    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    btn9.config(state=DISABLED)

def checkWinner():
    global winner
    if (btn1["text"]=="X" and btn2["text"]=="X" and btn3["text"]=="X" 
    or btn4["text"]=="X" and btn5["text"]=="X" and btn6["text"]=="X"
    or btn7["text"]=="X" and btn8["text"]=="X" and btn9["text"]=="X"
    or btn1["text"]=="X" and btn4["text"]=="X" and btn7["text"]=="X"
    or btn2["text"]=="X" and btn5["text"]=="X" and btn8["text"]=="X"
    or btn3["text"]=="X" and btn6["text"]=="X" and btn9["text"]=="X"
    or btn1["text"]=="X" and btn5["text"]=="X" and btn9["text"]=="X"
    or btn3["text"]=="X" and btn5["text"]=="X" and btn7["text"]=="X"):
        winner=True
        speletajsXX=1
        disButtons()
        res = messagebox.askyesno("TicTacToe", "X is winner! New game?")
        if res == True:
            reset()
        else:
            return 0
    elif (btn1["text"]=="O" and btn2["text"]=="O" and btn3["text"]=="O" 
    or btn4["text"]=="O" and btn5["text"]=="O" and btn6["text"]=="O"
    or btn7["text"]=="O" and btn8["text"]=="O" and btn9["text"]=="O"
    or btn1["text"]=="O" and btn4["text"]=="O" and btn7["text"]=="O"
    or btn2["text"]=="O" and btn5["text"]=="O" and btn8["text"]=="O"
    or btn3["text"]=="O" and btn6["text"]=="O" and btn9["text"]=="O"
    or btn1["text"]=="O" and btn5["text"]=="O" and btn9["text"]=="O"
    or btn3["text"]=="O" and btn5["text"]=="O" and btn7["text"]=="O"):
        winner=True
        speletajsOO=1
        disButtons()
        res = messagebox.askyesno("TicTacToe", "O is winner! New game?")
        if res == True:
            reset()
        else:
            return 0

    elif count==9:
        disButtons()
        res = messagebox.askyesno("TicTacToe", "No one has won! New game?")
        if res == True:
            reset()
        else:
            return 0


btn1=Button(mW, text="", bg="white", fg="black", width=5, height=2, font=("Verdana", 24), command=lambda: btnClick(btn1)) 
btn2=Button(mW, text="", bg="white", fg="black", width=5, height=2, font=("Verdana", 24), command=lambda: btnClick(btn2))
btn3=Button(mW, text="", bg="white", fg="black", width=5, height=2, font=("Verdana", 24), command=lambda: btnClick(btn3))
btn4=Button(mW, text="", bg="white", fg="black", width=5, height=2, font=("Verdana", 24), command=lambda: btnClick(btn4))
btn5=Button(mW, text="", bg="white", fg="black", width=5, height=2, font=("Verdana", 24), command=lambda: btnClick(btn5))
btn6=Button(mW, text="", bg="white", fg="black", width=5, height=2, font=("Verdana", 24), command=lambda: btnClick(btn6))
btn7=Button(mW, text="", bg="white", fg="black", width=5, height=2, font=("Verdana", 24), command=lambda: btnClick(btn7))
btn8=Button(mW, text="", bg="white", fg="black", width=5, height=2, font=("Verdana", 24), command=lambda: btnClick(btn8))
btn9=Button(mW, text="", bg="white", fg="black", width=5, height=2, font=("Verdana", 24), command=lambda: btnClick(btn9))

btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)
btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)

galvenaIzvelne=Menu(mW)
mW.config(menu=galvenaIzvelne)
options=Menu(galvenaIzvelne,tearoff=False)
galvenaIzvelne.add_cascade(label="Options", menu=options)
options.add_command(label="New Game", command=reset)
options.add_command(label="Exit", command=mW.quit)
galvenaIzvelne.add_command(label="About the game",command=infoLogs)

mW.mainloop()