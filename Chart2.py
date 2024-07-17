from tkinter import *
from PIL import ImageTk, Image
import os
import tkinter.messagebox as tm
def diet1():
    top=Tk()
    top.geometry('970x790')
    top.config(bg="#50ABE7")
    morning=Label(top,text="DIABETES DIET PLAN",font=('bold',30),bg="#50ABE7").place(x=280,y=50)
    morning=Label(top,text="Foods to be included",font=('bold',30),bg="#50ABE7").place(x=80,y=120)
    morning=Label(top,text="Foods to be avoided",font=('bold',30),bg="#50ABE7").place(x=500,y=120)
    dash=Label(top,text="--------------------------------------------------------------------------------------------------------------",bg="#50ABE7").place(x=150,y=160)
    morning=Label(top,text="Whole grain",font=('italic',20),bg="#50ABE7").place(x=80,y=200)
    morning=Label(top,text="Refined sugars",font=('italic',20),bg="#50ABE7").place(x=500,y=200)
    morning=Label(top,text="Walnuts",font=('italic',20),bg="#50ABE7").place(x=80,y=240)
    morning=Label(top,text="Instant Cereals",font=('italic',20),bg="#50ABE7").place(x=500,y=240)
    morning=Label(top,text="Pulses and Legumes",font=('italic',20),bg="#50ABE7").place(x=80,y=280)
    morning=Label(top,text="Cooked roots",font=('italic',20),bg="#50ABE7").place(x=500,y=280)
    morning=Label(top,text="Vegetables",font=('italic',20),bg="#50ABE7").place(x=80,y=320)
    morning=Label(top,text="Mango and Banana",font=('italic',20),bg="#50ABE7").place(x=500,y=320)
    morning=Label(top,text="Green leaf vegetables",font=('italic',20),bg="#50ABE7").place(x=80,y=360)
    morning=Label(top,text="Sodium rich foods",font=('italic',20),bg="#50ABE7").place(x=500,y=360)
    morning=Label(top,text="Egg white",font=('italic',20),bg="#50ABE7").place(x=80,y=420)
    morning=Label(top,text="Red meat",font=('italic',20),bg="#50ABE7").place(x=500,y=420)
    img = ImageTk.PhotoImage(Image.open("diab.jpg"))
    panel = Label(top, image = img)
    panel.place(x=80,y=400)
    top.mainloop()
diet1()

 
