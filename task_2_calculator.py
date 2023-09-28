from tkinter import *
from PIL import Image,ImageTk

r = Tk(className="Calculator by RM")
r.resizable(0,0)

c = ""
INP = StringVar()

def ac():
    global c
    c = ""
    INP.set(c)

def calc(i):
    try:
        global c
        c=str(eval(i))
        INP.set(c)
    except:
        c="error"
        INP.set(c)

def inp(p):
    global c
    c += p
    INP.set(c)

b1 = Button(r,text="(",bg="grey",command=lambda:inp("("),width=8,height=2)
b1.grid(row=1,column=0)

b2 = Button(r,text=")",bg="grey",command=lambda:inp(")"),width=8,height=2)
b2.grid(row=1,column=1)

b3 = Button(r,text="%",bg="grey",command=lambda:inp("/100"),width=8,height=2)
b3.grid(row=1,column=2)

b4 = Button(r,text="AC",bg="grey",command=lambda:ac(),width=8,height=2)
b4.grid(row=1,column=3)

b5 = Button(r,text="7",bg="grey",command=lambda:inp("7"),width=8,height=2)
b5.grid(row=2,column=0)

b6 = Button(r,text="8",bg="grey",command=lambda:inp("8"),width=8,height=2)
b6.grid(row=2,column=1)

b7 = Button(r,text="9",bg="grey",command=lambda:inp("9"),width=8,height=2)
b7.grid(row=2,column=2)

b8 = Button(r,text="/",bg="grey",command=lambda:inp("/"),width=8,height=2)
b8.grid(row=2,column=3)

b9 = Button(r,text="4",bg="grey",command=lambda:inp("4"),width=8,height=2)
b9.grid(row=3,column=0)

b10 = Button(r,text="5",bg="grey",command=lambda:inp("5"),width=8,height=2)
b10.grid(row=3,column=1)

b11 = Button(r,text="6",bg="grey",command=lambda:inp("6"),width=8,height=2)
b11.grid(row=3,column=2)

b12 = Button(r,text="*",bg="grey",command=lambda:inp("*"),width=8,height=2)
b12.grid(row=3,column=3)

b13 = Button(r,text="1",bg="grey",command=lambda:inp("1"),width=8,height=2)
b13.grid(row=4,column=0)

b14 = Button(r,text="2",bg="grey",command=lambda:inp("2"),width=8,height=2)
b14.grid(row=4,column=1)

b15 = Button(r,text="3",bg="grey",command=lambda:inp("3"),width=8,height=2)
b15.grid(row=4,column=2)

b16 = Button(r,text="-",bg="grey",command=lambda:inp("-"),width=8,height=2)
b16.grid(row=4,column=3)

b17 = Button(r,text="0",bg="grey",command=lambda:inp("0"),width=8,height=2)
b17.grid(row=5,column=0)

b18 = Button(r,text=".",bg="grey",command=lambda:inp("."),width=8,height=2)
b18.grid(row=5,column=1)

b19 = Button(r,text="=",bg="grey",command=lambda:calc(c),width=8,height=2)
b19.grid(row=5,column=2)

b20 = Button(r,text="+",bg="grey",command=lambda:inp("+"),width=8,height=2)
b20.grid(row=5,column=3)

display = Entry(bg="light grey",font=("arial black",20,"bold"),textvariable=INP,justify="right",width=15)
display.grid(row=0,column=0,columnspan=4)

r.mainloop()
