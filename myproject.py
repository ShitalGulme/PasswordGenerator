import random
from tkinter import *

def createor():

    character= "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*_"

    password_length=int(length_Box.get())

    password=random.sample(character,password_length)
    passwordField.insert(0,password)
root=Tk()
root.config(bg='blue')
Font=('arial',12,'bold')
passwordLabel=Label(root,text='password Generator',font=('times new roman',20,'bold'))
passwordLabel.grid(pady=10)
lengthLabel=Label(root,text='Password Length',font=Font,bg='gray24',fg='white')
lengthLabel.grid()
length_Box=Spinbox(root,from_=4,to=15,width=5,font=Font)
length_Box.grid(pady=4)
createButton=Button(root,text='Create',font=Font, command=createor)
createButton.grid()
passwordField=Entry(root,width=20,bd=2,font=Font)
passwordField.grid()
root.mainloop()
