
f1= Frame(root, bg="grey")
b=Button(f1, text="9", padx=19, pady=9, font="lucida 35 bold")
b.pack(side=LEFT, padx=7, pady=4)
b.bind("<Button-1>", click)

b=Button(f1, text="8", padx=19, pady=9, font="lucida 35 bold")
b.pack(side=LEFT, padx=7, pady=4)
b.bind("<Button-1>", click)

b=Button(f1, text="7", padx=19, pady=9, font="lucida 35 bold")
b.pack(side=LEFT, padx=7, pady=4)
b.bind("<Button-1>", click)

b=Button(f1, text="6", padx=19, pady=9, font="lucida 35 bold")
b.pack(side=LEFT, padx=7, pady=4)
b.bind("<Button-1>", click)

f1.pack()