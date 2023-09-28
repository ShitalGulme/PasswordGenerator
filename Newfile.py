from tkinter import *
from tkinter.ttk import*

master = Tk()

master.geometry("200*200")

def openNewWindow():

    NewWindow = Toplevel(master)
    NewWindow.title("New Window")

    Label(NewWindow, text="This is new window").pack()


Label.pack(pady=10)
btn = Button(master,
             text="click to open new window",
             command = openNewWindow)
btn.pack(pady=10)
mainloop()
