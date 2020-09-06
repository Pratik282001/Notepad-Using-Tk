from tkinter import *

def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value= int(scvalue.get())
        else:
            try:
                value=eval(screen.get())

            except Exception as e:
                print(e)
                value="Error"

        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set("")
        scvalue.update()
    else:
        scvalue.set(scvalue.get() +text)
        scvalue.update()

root=Tk()
root.geometry("644x900")

scvalue=StringVar()
scvalue.set("")
screen=Entry(root, textvar=scvalue, font="lucida 50 bold")
screen.pack(fill=X, ipadx=8, padx=9, pady=9)

f2= Frame(root, bg="grey")

b=Button(f2, text="9", padx=19, pady=9, font="lucida 35 bold")
b.pack(side=LEFT, padx=9, pady=5)
b.bind("<Button-1>", click)

b=Button(f2, text="8", padx=19, pady=9, font="lucida 35 bold")
b.pack(side=LEFT, padx=9, pady=5)
b.bind("<Button-1>", click)

b=Button(f2, text="7", padx=19, pady=9, font="lucida 35 bold")
b.pack(side=LEFT, padx=9, pady=5)
b.bind("<Button-1>", click)

f2.pack()

f3= Frame(root, bg="grey")


b=Button(f3, text="6", padx=19, pady=9, font="lucida 35 bold")
b.pack(side=LEFT, padx=9, pady=5)
b.bind("<Button-1>", click)

b=Button(f3, text="5", padx=19, pady=9, font="lucida 35 bold")
b.pack(side=LEFT, padx=9, pady=5)
b.bind("<Button-1>", click)

b=Button(f3, text="4", padx=19, pady=9, font="lucida 35 bold")
b.pack(side=LEFT, padx=9, pady=5)
b.bind("<Button-1>", click)

f3.pack()

f4= Frame(root, bg="grey")


b=Button(f4, text="3", padx=19, pady=9, font="lucida 35 bold")
b.pack(side=LEFT, padx=9, pady=5)
b.bind("<Button-1>", click)

b=Button(f4, text="2", padx=19, pady=9, font="lucida 35 bold")
b.pack(side=LEFT, padx=9, pady=5)
b.bind("<Button-1>", click)

b=Button(f4, text="1", padx=19, pady=9, font="lucida 35 bold")
b.pack(side=LEFT, padx=9, pady=5)
b.bind("<Button-1>", click)

f4.pack()


f5= Frame(root, bg="grey")


b=Button(f5, text="=", padx=19, pady=9, font="lucida 35 bold")
b.pack(side=LEFT, padx=7, pady=5)
b.bind("<Button-1>", click)

b=Button(f5, text="C", padx=19, pady=9, font="lucida 35 bold")
b.pack(side=LEFT, padx=7, pady=5)
b.bind("<Button-1>", click)

b=Button(f5, text="0", padx=19, pady=9, font="lucida 35 bold")
b.pack(side=LEFT, padx=7, pady=5)
b.bind("<Button-1>", click)

f5.pack()

f6= Frame(root, bg="grey")


b=Button(f6, text="-", padx=19, pady=9, font="lucida 35 bold")
b.pack(side=LEFT, padx=9, pady=5)
b.bind("<Button-1>", click)

b=Button(f6, text="+", padx=19, pady=9, font="lucida 35 bold")
b.pack(side=LEFT, padx=9, pady=5)
b.bind("<Button-1>", click)

b=Button(f6, text="*", padx=19, pady=9, font="lucida 35 bold")
b.pack(side=LEFT, padx=9, pady=5)
b.bind("<Button-1>", click)

f6.pack()

f7= Frame(root, bg="grey")

b=Button(f7, text="/", padx=19, pady=9, font="lucida 35 bold")
b.pack(side=LEFT, padx=9, pady=5)
b.bind("<Button-1>", click)

b=Button(f7, text="%", padx=19, pady=9, font="lucida 35 bold")
b.pack(side=LEFT, padx=9, pady=5)
b.bind("<Button-1>", click)

b=Button(f7, text="", padx=19, pady=9, font="lucida 35 bold")
b.pack(side=LEFT, padx=9, pady=5)
b.bind("<Button-1>", click)

f7.pack()

root.mainloop()