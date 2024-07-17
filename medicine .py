from tkinter import *
from PIL import ImageTk, Image
import os
import mysql.connector
import tkinter.messagebox as tm

def insert_rows():
    for i in medicinedetailentry.curselection():
        print(i)
        print(medicinedetailentry.get(i))
        medicinedetail_info=medicinedetailentry.get(i)
    level_info=levelvar.get()
    
    yearsoftreatment_info=yearsoftreatmentvar.get()
    
    if(patientName.get()=="" or level_info=="" or medicinedetail_info=="" or yearsoftreatment_info==0):
       tm.showerror("Error","Please Enter all the  Details!!!!")
    else:
       mydb=mysql.connector.connect(
         host='localhost',
         user='root',
         passwd='',
         database='nagammai'
       )
       mycursor=mydb.cursor()
    
       #sql='INSERT INTO login(level,medicinedetails,yearsoftreatment)VALUES(%s,%s,%s)'
       sql="update diet set level='{}',medicinedetails='{}', yearsoftreatment='{}' where name='{}'"
       #val=(level_info,medicinedetail_info,yearsoftreatment_info)
       val=sql.format(level_info,medicinedetail_info,yearsoftreatment_info,patientName.get())
       mycursor.execute(val)
       mydb.commit()
       tm.showinfo("Modify","Patient Details updated successfully!!!!!!")
       if(medicinedetail_info=='BP'):
         import Chart1
       if(medicinedetail_info=='SUGAR'):
         import Chart2
       if(medicinedetail_info=='THYROID'):
         import Chart3
    
top=Tk()
top.geometry('1000x500')
top.config(bg='#DB8AF1')
global medicinedetail_info
global patientName
global levelvar
global medicinedetailvar
global yearsoftreatmentvar
global patiententry
global levelentry
global medicinedetailentry
global yearsoftreatmententry
patientName=StringVar()
levelvar=StringVar()
medicinedetailvar=StringVar()
yearsoftreatmentvar=IntVar()

img = ImageTk.PhotoImage(Image.open("fd.jpg"))
panel = Label(top, image = img)
panel.pack()
heading=Label(top,text="MEDICAL CONDITION",font=('ALGERIAN',32),bg='black',fg='#EDF506').place(x=400,y=30)

patientLabel=Label(top,text="Name",font=('ALGERIAN',30),bg="#0F0F01",fg="#FFC300").place(x=240,y=90)
level=Label(top,text="Level",font=('ALGERIAN',30),bg="#0F0F01",fg="#FFC300").place(x=240,y=150)
medicinedetails=Label(top,text="Medicine Details",font=('ALGERIAN',30),bg="#0F0F01",fg="#FFC300").place(x=240,y=210)
yearsoftreatment=Label(top,text="Years of Treatment",font=('ALGERIAN',30),bg="#0F0F01",fg="#FFC300").place(x=240,y=320)
 
patiententry=Entry(top,textvariable=patientName,font=('bold',20),bg="#F4F6F7").place(x=690,y=90)
levelentry=Entry(top,textvariable=levelvar,font=('bold',20),bg="#F4F6F7").place(x=690,y=150)
 
#medicinedetailentry=Entry(top,textvariable=medicinedetailvar,font=('bold',20),bg="#F4F6F7").place(x=600,y=210)
medicinedetailentry = Listbox(top, height = 4, 
                  width = 23, 
                  bg = "yellow",
                  activestyle = 'dotbox', 
                  font = "bold",
                  fg = "red")
medicinedetailentry.insert(1, "Prinivil")
medicinedetailentry.insert(2, "Levot")
medicinedetailentry.insert(3, "Glyclazide")
medicinedetailentry.place(x=690,y=210)


yearsoftreatmententry=Entry(top,textvariable=yearsoftreatmentvar,font=('bold',20),bg="#F4F6F7",width=14).place(x=690,y=320)
 
sbmitbtn=Button(top,text="UPDATE",command=insert_rows,font=('ALGERIAN',17),bg="#69ED0E",fg="#C0392B").place(x=500,y=380)
#details()




    
    
