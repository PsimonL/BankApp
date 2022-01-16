from tkinter import *
from helpers import con, create_inputs, get_inputs


class EmployeePanel():

    def __init__(self, user):
        self.user = user
        self.emp_panel = Tk()
        self.emp_panel.title("Employee panel")
        self.var = IntVar()
        self.var2 = IntVar()
        self.text="Applications"
        self.applicationContainer=Frame(self.emp_panel)
        self.label=Label(self.emp_panel,text=self.text)

        c = Checkbutton(self.emp_panel, text="Approve application", variable=self.var,
                        command=self.employee_approved)
        c2 = Checkbutton(self.emp_panel, text="Reject application", variable=self.var2,
                         command=self.employee_rejected)
        c.deselect()
        c2.deselect()
        c.pack(side="top")
        c.pack()
        c2.pack()

    def submit(self):
        if len(self.users)==0:
            self.text="No applications"


    def employee_approved(self):
        print("YES")


    def employee_rejected(self,pesel):
        con("UPDATE clients SET hidden = 'mary.patterson@classicmodelcars.com'WHERE employeeNumber ="+ pesel,True)

    def create_applications_list(self):
        created_applications = dict()
        containers=[]
        for i in range(0, len(self.user)):
            name = self.user[i][2]
            surname = self.user[i][3]

            application=Frame(self.applicationContainer)
            application.grid(row=i, column=1)
            name_label=Label(application,text=name+surname)
            name_label.pack(side="left")
            containers.insert(application)



def end():
    exit(1)
