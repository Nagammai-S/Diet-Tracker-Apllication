from tkinter import *
from PIL import ImageTk, Image
import os
import mysql.connector
import tkinter.messagebox as tm
class Diet:
 def __init__(self,root):
    self.f=Frame(root,height=800,width=1000)
    self.f.pack()

    self.namevar=StringVar()
    self.agevar=IntVar()
    self.condvar=StringVar()
    self.weightvar=IntVar()
    self.heightvar=IntVar()
    self.bloodgroupvar=StringVar()
    self.img = ImageTk.PhotoImage(Image.open("bg1.jpg"))

    
    self.panel = Label(self.f, image = self.img)
    self.panel.pack(fill = BOTH, expand = True)

    self.heading=Label(self.f,text="DIET CHART TRACKER",font=('ALGERIAN',32),bg='#3b4645',fg='#EDF506').place(x=600,y=30)  
    self.name=Label(self.f,text="NAME",font=('ALGERIAN',28),bg='#3b4645',fg='#EDF506').place(x=500,y=100)
    self.age=Label(self.f,text="AGE",font=('ALGERIAN',28),bg='#3b4645',fg='#EDF506').place(x=500,y=180)
    self.cond=Label(self.f,text="CONDITION",font=('ALGERIAN',28),bg='#3b4645',fg='#EDF506').place(x=500,y=260)
    self.weight=Label(self.f,text="WEIGHT",font=('ALGERIAN',28),bg='#3b4645',fg='#EDF506').place(x=500,y=340)
    self.height=Label(self.f,text="HEIGHT",font=('ALGERIAN',28),bg='#3b4645',fg='#EDF506').place(x=500,y=420)
    self.bloodgroup=Label(self.f,text="BLOOD_GROUP",font=('ALGERIAN',25),bg='#3b4645',fg='#EDF506').place(x=500,y=500)
    self.nameentry=Entry(self.f,textvariable=self.namevar,font=('bold',28)).place(x=760,y=100) 
    self.ageentry=Entry(self.f,textvariable=self.agevar,font=('bold',28)).place(x=760,y=180)
    self.condentry=Entry(self.f,textvariable=self.condvar,font=('bold',28),width=19).place(x=760,y=260)
    self.weightentry=Entry(self.f,textvariable=self.weightvar,font=('bold',28)).place(x=760,y=340)
    self.heightentry=Entry(self.f,textvariable=self.heightvar,font=('bold',28)).place(x=760,y=420)
    self.bloodgroupentry=Entry(self.f,textvariable=self.bloodgroupvar,font=('bold',28),width=17).place(x=760,y=500)
    self.sbmitbtn=Button(self.f,text="SUBMIT",command=self.insert_rows,font=('ALGERIAN',20),relief=RAISED,bg="#EDF506",fg='#3b4645').place(x=700,y=600)
 def insert_rows(self):
  
  name_info=self.namevar.get()
  age_info=self.agevar.get()
  cond_info=self.condvar.get()
  weight_info=self.weightvar.get()
  height_info=self.heightvar.get()
  bloodgroup_info=self.bloodgroupvar.get()
  if(name_info=='' or age_info==0 or cond_info==''or weight_info==0 or height_info==0 or bloodgroup_info==''):
     tm.showerror("Error","Please Enter all the  Details!!!!")
  else:
     mydb=mysql.connector.connect(
       host='localhost',
       user='root',
       passwd='',
       database='nagammai'
      )
     mycursor=mydb.cursor()
     sql='INSERT INTO diet(name,age,cond,weight,height,bloodgroup)VALUES(%s,%s,%s,%s,%s,%s)'
     val=(name_info,age_info,cond_info,weight_info,height_info,bloodgroup_info)
     mycursor.execute(sql,val)
     mydb.commit()
     tm.showinfo("info","Patient Details registered successfully!!!!!!")

root=Tk()
d=Diet(root)
root.mainloop()




