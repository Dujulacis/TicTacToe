from tabnanny import check
from tkinter import*
from tkinter import messagebox #messages
mW=Tk()
mW.title("TicTacToe")

speletajsX=True
count=0

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
        messagebox.showinfo("TicTacToe", "X is winner!")
    elif (btn1["text"]=="O" and btn2["text"]=="O" and btn3["text"]=="O" 
    or btn4["text"]=="O" and btn5["text"]=="O" and btn6["text"]=="O"
    or btn7["text"]=="O" and btn8["text"]=="O" and btn9["text"]=="O"
    or btn1["text"]=="O" and btn4["text"]=="O" and btn7["text"]=="O"
    or btn2["text"]=="O" and btn5["text"]=="O" and btn8["text"]=="O"
    or btn3["text"]=="O" and btn6["text"]=="O" and btn9["text"]=="O"
    or btn1["text"]=="O" and btn5["text"]=="O" and btn9["text"]=="O"
    or btn3["text"]=="O" and btn5["text"]=="O" and btn7["text"]=="O"):
        winner=True
        messagebox.showinfo("TicTacToe", "O is winner!")
    elif count==9:
        messagebox.showinfo("TicTacToe", "No one has won!")



btn1=Button(mW, text="", fg="red", width=5, height=2, font=("Verdana", 24), command=lambda: btnClick(btn1)) 
btn2=Button(mW, text="", fg="red", width=5, height=2, font=("Verdana", 24), command=lambda: btnClick(btn2))
btn3=Button(mW, text="", fg="red", width=5, height=2, font=("Verdana", 24), command=lambda: btnClick(btn3))
btn4=Button(mW, text="", fg="red", width=5, height=2, font=("Verdana", 24), command=lambda: btnClick(btn4))
btn5=Button(mW, text="", fg="red", width=5, height=2, font=("Verdana", 24), command=lambda: btnClick(btn5))
btn6=Button(mW, text="", fg="red", width=5, height=2, font=("Verdana", 24), command=lambda: btnClick(btn6))
btn7=Button(mW, text="", fg="red", width=5, height=2, font=("Verdana", 24), command=lambda: btnClick(btn7))
btn8=Button(mW, text="", fg="red", width=5, height=2, font=("Verdana", 24), command=lambda: btnClick(btn8))
btn9=Button(mW, text="", fg="red", width=5, height=2, font=("Verdana", 24), command=lambda: btnClick(btn9))

btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)
btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)

mW.mainloop()