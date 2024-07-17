from tkinter import *
from PIL import ImageTk, Image
import os
import tkinter.messagebox as tm
def diet():
    top=Tk()
    top.geometry('1000x1200')
    top.config(bg="#5D6D7E")
    img = ImageTk.PhotoImage(Image.open("black.jpg"))
    panel = Label(top, image = img)
    panel.pack()
    morning=Label(top,text="Food item",font=('bold',30),fg="#DFFF00",bg="#34495E").place(x=30,y=50)
    morning=Label(top,text="Amount",font=('bold',30),fg="#DFFF00",bg="#34495E").place(x=300,y=50)
    dash=Label(top,text="--------------------------------------------------------------------------------------",fg="#5D6D7E",bg="#34495E").place(x=30,y=100)
    morning=Label(top,text="Early morning",font=('bold',30),fg="#DFFF00",bg="#34495E").place(x=30,y=150)
    morning=Label(top,text="Tepid water",font=('bold',30),fg="Aquamarine",bg="#34495E").place(x=30,y=200)
    morning=Label(top,text="2-3 glass",font=('bold',30),fg="Aquamarine",bg="#34495E").place(x=300,y=200)
    morning=Label(top,text="Sprouted",font=('bold',30),fg="Aquamarine",bg="#34495E").place(x=30,y=250)
    morning=Label(top,text="3 table spoon",fg="Aquamarine",font=('bold',30),bg="#34495E").place(x=300,y=250)
    morning=Label(top,text="Lemon tea",font=('bold',30),fg="Aquamarine",bg="#34495E").place(x=30,y=300)
    morning=Label(top,text="1 cup",font=('bold',30),fg="Aquamarine",bg="#34495E").place(x=300,y=300)
    morning=Label(top,text="Fiber biscuits",font=('bold',30),fg="Aquamarine",bg="#34495E").place(x=30,y=350)
    morning=Label(top,text="2",font=('bold',30),fg="Aquamarine",bg="#34495E").place(x=300,y=350)
    morning=Label(top,text="cucumber",font=('bold',30),fg="Aquamarine",bg="#34495E").place(x=30,y=400)
    morning=Label(top,text="1",font=('bold',30),fg="Aquamarine",bg="#34495E").place(x=300,y=400)
    morning=Label(top,text="Breakfast",font=('bold',30),fg="#DFFF00",bg="#34495E").place(x=30,y=450)
    morning=Label(top,text="roti",font=('bold',30),fg="Aquamarine",bg="#34495E").place(x=30,y=500)
    morning=Label(top,text="2",font=('bold',30),fg="Aquamarine",bg="#34495E").place(x=300,y=500)
    morning=Label(top,text="curd",font=('bold',30),fg="Aquamarine",bg="#34495E").place(x=30,y=550)
    morning=Label(top,text="1 cup",font=('bold',30),fg="Aquamarine",bg="#34495E").place(x=300,y=550)
    morning=Label(top,text="Vegetable",font=('bold',30),fg="Aquamarine",bg="#34495E").place(x=30,y=600)
    morning=Label(top,text="1 soup bowl",font=('bold',30),fg="Aquamarine",bg="#34495E").place(x=300,y=600)
    morning=Label(top,text="Mid morning",font=('bold',30),fg="#DFFF00",bg="#34495E").place(x=30,y=650)
    morning=Label(top,text="orange",font=('bold',30),fg="Aquamarine",bg="#34495E").place(x=30,y=700)
    morning=Label(top,text="1",font=('bold',30),fg="Aquamarine",bg="#34495E").place(x=300,y=700)
    morning=Label(top,text="Black berry",font=('bold',30),fg="Aquamarine",bg="#34495E").place(x=30,y=750)
    morning=Label(top,text="1 bowl",font=('bold',30),fg="Aquamarine",bg="#34495E").place(x=300,y=750)
    morning=Label(top,text="Lunch",font=('bold',30),fg="#DFFF00",bg="#34495E").place(x=30,y=800)
    morning=Label(top,text="Salad",font=('bold',30),fg="Aquamarine",bg="#34495E").place(x=30,y=850)
    morning=Label(top,text="1 medium bowl",font=('bold',30),fg="Aquamarine",bg="#34495E").place(x=300,y=850)
    morning=Label(top,text="veg gobhi",font=('bold',30),fg="Aquamarine",bg="#34495E").place(x=30,y=900)
    morning=Label(top,text="1 medium bowl",font=('bold',30),fg="Aquamarine",bg="#34495E").place(x=300,y=900)
    top.mainloop()
diet()

    
    
    

    
    
