import tkinter as tk
from tkinter import *
import winsound

def beep(frequency):
    winsound.Beep(frequency, 200)

top = tk.Tk()

top.geometry("600x500")

answer = Text(width=35, height=2)
answer.place(x=100, y=100)


def show(x):
    try:
        if x == "=":
            final_answer = eval(answer.get(1.0, "end-1c"))
            answer.delete(1.0, END)
            answer.insert(tk.INSERT, final_answer)
        else:
            answer.insert(tk.INSERT, x)

    except:
        answer.delete(1.0, END)

B1 = Button(top, text = "1", width = 10, height = 5, bg="blue", fg="white", activebackground="#2ECC71",
    activeforeground="white", command=lambda: beep(500) and show("1"))
B1.place(x=100, y=150)

B2 = Button(top, text = "2", width = 10, height = 5, bg="blue", fg="white", activebackground="#2ECC71",
    activeforeground="white", command=lambda: beep(600) and show("2"))
B2.place(x=200, y=150)

B3 = Button(top, text = "3", width = 10, height = 5, bg="blue", fg="white", activebackground="#2ECC71",
    activeforeground="white", command=lambda: beep(700) and show("3"))
B3.place(x=300, y=150)

B4 = Button(top, text = "4", width = 10, height = 5, bg="blue", fg="white", activebackground="#2ECC71",
    activeforeground="white", command=lambda: beep(800) and show("4"))
B4.place(x=400, y=150)

B5 = Button(top, text = "5", width = 10, height = 5, bg="blue", fg="white", activebackground="#2ECC71",
    activeforeground="white", command=lambda: beep(900) and show("5"))
B5.place(x=100, y=250)

B6 = Button(top, text = "6", width = 10, height = 5, bg="blue", fg="white", activebackground="#2ECC71",
    activeforeground="white", command=lambda: beep(1000) and show("6"))
B6.place(x=200, y=250)

B7 = Button(top, text = "7", width = 10, height = 5, bg="blue", fg="white", activebackground="#2ECC71",
    activeforeground="white", command=lambda: beep(1100) and show("7"))
B7.place(x=300, y=250)

B8 = Button(top, text = "8", width = 10, height = 5, bg="blue", fg="white", activebackground="#2ECC71",
    activeforeground="white", command=lambda: beep(1200) and show("8"))
B8.place(x=400, y=250)

B9 = Button(top, text = "9", width = 10, height = 5, bg="blue", fg="white", activebackground="#2ECC71",
    activeforeground="white", command=lambda: beep(1300) and show("9"))
B9.place(x=100, y=350)

B10 = Button(top, text = "10", width = 10, height = 5, bg="blue", fg="white", activebackground="#2ECC71",
    activeforeground="white", command=lambda: beep(1400) and show("10"))
B10.place(x=200, y=350)

B11 = Button(top, text = "11", width = 10, height = 5, bg="blue", fg="white", activebackground="#2ECC71",
    activeforeground="white", command=lambda: beep(1500) and show("11"))
B11.place(x=300, y=350)

B12 = Button(top, text = "12", width = 10, height = 5, bg="blue", fg="white", activebackground="#2ECC71",
    activeforeground="white", command=lambda: beep(1600) and show("12"))
B12.place(x=400, y=350)

top.mainloop()