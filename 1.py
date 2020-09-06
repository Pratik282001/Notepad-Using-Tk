# from win32com.client import Dispatch
# import time
# import requests
# import json
# def speak(str):
#     time.sleep(1)
#     speak= Dispatch("SAPI.SpVoice")
#     speak.Speak(str)
    
# if __name__ == '__main__':
#     # in place API_KEY you can use your own api keys from website newsapi.org ;)
#     # one example is given below
#     response = requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=c546cd7dd0e4454d81e3d3b684eff6bf")
#     # response = requests.get("http://newsapi.org/v2/everything?q=apple&from=2020-09-03&to=2020-09-03&sortBy=popularity&apiKey=API_KEY")
#     text = response.text
#     my_json = json.loads(text)
#     speak("    today's top headlines are")
#     for i in range(0, 11):
#         print(my_json['articles'][i]['title'])
#         speak(my_json['articles'][i]['title'])
#         print(my_json['articles'][i]['description'])
#         speak(my_json['articles'][i]['description'])
#         print()
#     speak("  these were some top headlines")


# exit()

from tkinter import *
from PIL import Image,ImageTk

root= Tk()

def call():
    print(uservalue.get())
    print(passvalue.get())

root.geometry("444x444")
root.title('jacob')

# myslider=Scale(root, from_=0, to=1000)
# myslider.pack()

myslider=Scale(root, from_=0, to=1000, orient=HORIZONTAL)
myslider.pack()
#---------------------------------------------------
# youmenu=Menu(root)
# m1=Menu(youmenu, tearoff=0) #can be 1
# m1.add_command(label="hello")
# m1.add_command(label="hello")
# m1.add_command(label="hello")
# root.config(menu=youmenu)
# youmenu.add_cascade(label="file",menu=m1)

# m2=Menu(youmenu, tearoff=0) #can be 1
# m2.add_command(label="hello")
# m2.add_separator()
# m2.add_command(label="hello")
# m2.add_command(label="hello")
# root.config(menu=youmenu)
# youmenu.add_cascade(label="file",menu=m2)

#------------------------------------------------

# def myfun():
#     exit()

# mymenu=Menu(root)
# mymenu.add_command(label="file", command=myfun)
# mymenu.add_command(label="exit", command=myfun)

# root.config(menu=mymenu)
#--------------------------------------------------
# user=Label(root, pady=8,padx=8, text="name")
# pass1=Label(root, pady=8,padx=8, text="Pass")
# user.grid()
# pass1.grid()

# uservalue=StringVar()
# passvalue=StringVar()

# userentry=Entry(root, textvariable=uservalue)
# passentry=Entry(root, textvariable=passvalue)

# userentry.grid(row=0, column=1)
# passentry.grid(row=1, column=1)

# b=Button(root, text="Submit", command=call)
# b.grid()
#-----------------------------------------------
# f1=Frame(root, bg='grey', borderwidth=6, relief=SUNKEN)
# f1.pack(side=LEFT, fill='y')

# f2=Frame(root, bg='grey', borderwidth=8, relief=SUNKEN)
# f2.pack(side=TOP, fill="x")

# l2=Button(f2, command=call, text="call")
# l2.pack()

# l=Label(f1,pady=8,padx=8, text="Project Tkinter")
# l.pack()
# l1=Label(f2,pady=8,padx=8, text="Project Tkinter")
# l1.pack()

# photo=PhotoImage(file="box.png")
# image=Image.open('blox.jpg')
# photo=ImageTk.PhotoImage(image)

# b=Label(image=photo, relief=SUNKEN, background='red')
# b.pack()
# c=Label(text="hello world",foreground='blue',relief=SUNKEN, background='red')
# c.pack()
 
root.mainloop()