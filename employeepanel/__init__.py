from tkinter import *
from helpers import mySQL_connection
from db.queries import *
from helpers import create_inputs, mySQL_connection, get_inputs


class EmployeePanel():

    def __init__(self, user):
        self.user = user
        self.emp_panel = Tk()
        self.emp_panel.title("Employee panel")

        self.employee_container = Frame(self.emp_panel)
        self.employee_container.pack()

        self.account_applications_container = Frame(self.employee_container)
        self.account_applications_container.grid(row=1)

        self.loans_applications_container = Frame(self.employee_container)
        self.loans_applications_container.grid(row=2)

        self.deposits_applications_container = Frame(self.employee_container)
        self.deposits_applications_container.grid(row=3)

        welcome_text = "Welcome " + user[2] + " " + user[1]

        welcome_label = Label(self.employee_container, text=welcome_text)
        welcome_label.grid(row=0, column=0)
        self.create_account_application_list()

    def reinitialize(self):
        self.emp_panel.destroy()
        EmployeePanel(self.user)

    def no_applications_notification(self):
        no_applications_label = Label(self.account_applications_container, text="No applications.\n Congartulation!!!")
        self.account_applications_container.pack_forget()
        no_applications_label.pack(side="bottom")

    def employee_approved(self, type, application, id=0):
        if type == "account":
            mySQL_connection(confirm_client_account_query + application.pesel, True)
            self.reinitialize()

    def employee_rejected(self, type, application, id=0):
        if type == "account":
            mySQL_connection(reject_client_account_query + application.pesel, True)
            self.reinitialize()

    def create_account_application_list(self):
        applications = mySQL_connection(select_unconfirmed_clients_query, False, True)
        applications_pesels = []
        application_id = 0
        if len(applications) == 0:
            self.no_applications_notification()
            return
        for appl in applications:
            application_row = application_id + 2
            self.account_applications_container.grid_rowconfigure(application_row, minsize=45)
            application = Frame(self.account_applications_container)
            application.grid(row=application_row, column=0)
            application.grid_columnconfigure(0, minsize=120)
            application.pesel = appl[1]
            name_label = Label(application, text=appl[3] + " " + appl[4])
            name_label.grid(row=application_row, column=0)

            pesel_label = Label(application, text=appl[1])
            pesel_label.grid(row=application_row, column=1)

            approve_button = Button(application, text="Approve application",
                                    command=lambda bound_appl=application: self.employee_approved("account",
                                                                                                  bound_appl))
            reject_button = Button(application, text="Reject application",
                                   command=lambda bound_appl=application: self.employee_rejected("account", bound_appl))

            approve_button.grid(row=application_row, column=2)
            reject_button.grid(row=application_row, column=3)
            application_id += 1


def end():
    exit(1)
