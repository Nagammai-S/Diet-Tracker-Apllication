from tkinter import *
from PIL import ImageTk, Image
import os
import tkinter.messagebox as tm
def diet2():
    top=Tk()
    top.geometry('1000x1000')
    img = ImageTk.PhotoImage(Image.open("food.jpg"))
    panel = Label(top, image = img)
    panel.pack()
    morning=Label(top,text="Food item",font=('bold',30),bg="#111010",fg="#E70935").place(x=30,y=50)
    morning=Label(top,text="Breakfast",font=('bold',30),bg="#111010",fg="#E70935").place(x=30,y=150)
    morning=Label(top,text="Eggs",font=('italic',20),bg="#111010",fg="#FFC300").place(x=30,y=200)
    morning=Label(top,text="Bread",font=('italic',20),bg="#111010",fg="#FFC300").place(x=300,y=200)
    morning=Label(top,text="Butter",font=('italic',20),bg="#111010",fg="#FFC300").place(x=30,y=250)
    morning=Label(top,text="Cheese slice",font=('italic',20),bg="#111010",fg="#FFC300").place(x=300,y=250)
    morning=Label(top,text="Lunch",font=('bold',30),bg="#111010",fg="#E70935").place(x=30,y=300)
    morning=Label(top,text="Chicken breast",font=('italic',20),bg="#111010",fg="#FFC300").place(x=30,y=350)
    morning=Label(top,text="Rice",font=('italic',20),bg="#111010",fg="#FFC300").place(x=300,y=350)
    morning=Label(top,text="Olive oli",font=('italic',20),bg="#111010",fg="#FFC300").place(x=30,y=400)
    morning=Label(top,text="Mixed frozen vegetables",font=('italic',20),bg="#111010",fg="#FFC300").place(x=300,y=400)
    morning=Label(top,text="Snacks",font=('bold',30),bg="#111010",fg="#E70935").place(x=30,y=450)
    morning=Label(top,text="Whey Protein",font=('italic',20),bg="#111010",fg="#FFC300").place(x=30,y=500)
    morning=Label(top,text="Apples",font=('italic',20),bg="#111010",fg="#FFC300").place(x=300,y=500)
    morning=Label(top,text="Dinner",font=('italic',30),bg="#111010",fg="#E70935").place(x=30,y=550)
    morning=Label(top,text="Greeny leafes",font=('italic',20),bg="#111010",fg="#FFC300").place(x=30,y=600)
    morning=Label(top,text="Ragi",font=('italic',20),bg="#111010",fg="#FFC300").place(x=300,y=600)
    morning=Label(top,text="Vegetable poha",font=('italic',20),bg="#111010",fg="#FFC300").place(x=30,y=650)
    morning=Label(top,text="Cereals",font=('italic',20),bg="#111010",fg="#FFC300").place(x=300,y=650)
    top.mainloop()
diet2()

    
    
    

    
    
