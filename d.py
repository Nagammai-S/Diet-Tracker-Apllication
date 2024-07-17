from tkinter import *
import sqlite3
import pyttsx3

# connection to database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# window
class Application:
    def __init__(self, master):
        self.master = master
        self.x = 0
        
        # heading
        self.heading = Label(master, text="Appointments", font=('arial 30 bold'), fg='green')
        self.heading.place(x=450, y=0)

        # total patients label
        self.total_label = Label(master, text="Total Patients:", font=('arial 20 bold'))
        self.total_label.place(x=10, y=60)

        # button to delete patient
        self.delete_button = Button(master, text="Delete Appointment", width=25, height=2, bg='red', command=self.delete_appointment)
        self.delete_button.place(x=400, y=650)

        # button to change patients
        self.next_button = Button(master, text="Next Patient", width=25, height=2, bg='steelblue', command=self.next_patient)
        self.next_button.place(x=650, y=650)

        # button to quit
        self.quit_button = Button(master, text="Quit", width=10, height=1, bg='grey', command=master.quit)
        self.quit_button.place(x=575, y=700)

        # empty text labels to later config
        self.n = Label(master, text="", font=('arial 200 bold'))
        self.n.place(x=500, y=100)

        self.pname = Label(master, text="", font=('arial 80 bold'))
        self.pname.place(x=300, y=400)

        self.total_patients = Label(master, text="", font=('arial 20 bold'))
        self.total_patients.place(x=220, y=60)

        # initialize the patient list
        self.number = []
        self.patients = []
        self.load_appointments()

    # function to load appointments from database
    def load_appointments(self):
        self.number.clear()
        self.patients.clear()
        sql = "SELECT * FROM appointments"
        res = c.execute(sql)
        for r in res:
            ids = r[0]
            name = r[1]
            self.number.append(ids)
            self.patients.append(name)
        self.total_patients.config(text=str(len(self.number)))

    # function to delete the current patient's appointment
    def delete_appointment(self):
        if self.number:
            current_patient_id = self.number[self.x]
            c.execute("DELETE FROM appointments WHERE id=?", (current_patient_id,))
            conn.commit()
            self.load_appointments()
            if self.x >= len(self.number):
                self.x = 0
            self.display_patient()

    # function to show the next patient
    def next_patient(self):
        if self.number:
            self.x = (self.x + 1) % len(self.number)
            self.display_patient()

    # function to display patient details
    def display_patient(self):
        if self.number:
            self.n.config(text=str(self.number[self.x]))
            self.pname.config(text=str(self.patients[self.x]))
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            rate = engine.getProperty('rate')
            engine.setProperty('rate', rate - 50)
            engine.say('Patient number ' + str(self.number[self.x]) + " " + str(self.patients[self.x]))
            engine.runAndWait()

root = Tk()
b = Application(root)
root.geometry("1500x1500")
root.resizable(False, False)
root.mainloop()
