import tkinter
from tkinter import *
from helpers import create_inputs, mySQL_connection, get_inputs
from employeepanel import EmployeePanel
from db.queries import *

e_ids = ['1', '2', '3']
e_pas = ['a', 'b', 'c']


class Sign():
    button_width = 25
    button_height = 7
    button_standard_size = ""

    def my_button(self, src, txt, command, width=button_width, height=button_height):
        return tkinter.Button(src, text=txt, width=width, height=height, command=command)

    def __init__(self, is_employee):

        self.login_container = None
        self.return_button = None
        self.login_counter = 0
        self.isRoot = None

        self.root = Tk()
        self.root.title("Sign in panel")
        self.is_employee = is_employee

        self.main_container = Frame(self.root)
        self.main_container.pack()

        if is_employee:
            self.for_employee()
        else:
            self.for_client()

    def reinitialize(self):
        self.root.destroy()
        Sign(self.is_employee)

    def for_employee(self):
        sign_up_button = self.my_button(self.main_container, txt="Log in", command=self.sign_in_employee)
        exit_button = self.my_button(self.main_container, txt="Exit", command=end)

        sign_up_button.grid(row=1, column=1)
        exit_button.grid(row=2, column=1)

    def for_client(self):

        sign_up_button = self.my_button(self.main_container, txt="Sign up", command=self.sign_up)
        sign_in_button = self.my_button(self.main_container, txt="Sign in", command=self.sign_in_client)
        exit_button = self.my_button(self.main_container, txt="Exit", command=end)
        self.return_button = self.my_button(self.root, txt="return", command=self.reinitialize)

        sign_up_button.grid(row=1, column=1)
        sign_in_button.grid(row=2, column=1)
        exit_button.grid(row=3, column=1)

        self.isRoot = True
        self.set_return_visible()

    def set_return_visible(self):
        if not self.isRoot:
            self.return_button.pack(side='bottom')
        else:
            self.return_button.pack_forget()

    def sign_in_client(self):
        self.isRoot = False
        self.set_return_visible()

        fields = ['pesel', 'password']
        data = dict()
        error_labels = dict()

        self.main_container.destroy()
        login_container = Frame(self.root)
        login_container.pack()

        self.root.title("Login Panel")

        inputs = create_inputs(fields, self.login_container, error_labels)

        def recover_password():
            if not get_inputs(inputs, data, error_labels):
                return
            print(data['pesel'])
            password = mySQL_connection(select_user_by_pesel_query + data['pesel'])[4]
            print(password)
            password_label = Label(self.login_container, text="Your password is: " + password)
            password_label.grid(row=3, column=2)

        def sign():
            if self.login_counter > 2:
                print("Zbyt wiele nieudanych prob logowania!")
                self.root.destroy()
            if not get_inputs(inputs, data, error_labels):
                return
            query = select_client_query + data['pesel']
            user = mySQL_connection(query)

            print(user)
            if user[2] == data['password']:
                print("Zalogowany jako:", data['pesel'])
                self.login_container.destroy()
            else:
                self.login_counter += 1
                print("Zly login lub haslo!")

        get_logged = self.my_button(self.login_container, txt="Log in", command=sign)
        retrieve_password_button = self.my_button(self.login_container, txt="Odzyskaj haslo", command=recover_password)
        retrieve_password_button.grid(row=4, column=1)

        get_logged.grid(row=4, column=2)

    def sign_in_employee(self):
        fields = ['id', 'password']

        data = dict()

        self.main_container.destroy()

        sign_in_container = Frame(self.root)
        sign_in_container.pack()
        self.root.title("Enter data")
        error_labels = dict()
        inputs = create_inputs(fields, sign_in_container, error_labels)

        def submit():

            if not get_inputs(inputs, data, error_labels):
                return

            user = mySQL_connection(select_employees_query + data['id'])
            if int(data['id']) == user[0] and data['password'] == user[3]:
                self.root.destroy()
                EmployeePanel(user)

            else:
                print("wrong")

        sub = Button(sign_in_container, text="Submit", padx=87, pady=40, command=submit)
        sub.grid(row=3, column=1)

    def sign_up(self):
        self.isRoot = False
        self.set_return_visible()

        fields = ["pesel", "name", "surname", "date", "password", "confirm_password"]
        data = dict()
        error_labels = dict()

        self.main_container.destroy()
        registration_panel = Frame(self.root)
        registration_panel.pack()

        self.root.title("Create an account")

        inputs = create_inputs(fields, registration_panel, error_labels)

        def check_is_pesel_valid():
            res = mySQL_connection(select_user_by_pesel_query + data['pesel'])
            return res is None and len(data['pesel']) == 11

        def create_user():
            if not get_inputs(inputs, data, error_labels):
                return
            date_of_birth = data['date']
            print(data['password'])
            print(data['confirm_password'])
            # ta sama zabawa; pesel musi miec 13 liter itd...
            if data['confirm_password'] == data['password'] and check_is_pesel_valid():
                query = insert_clients_query_part1 + '''
                 ('''  '\'' + data['pesel'] + '\'' + ',' + '\'' + data[
                    'password'] + '\'' + ',' + '\'' + \
                        data['name'] + '\'' + ',' + '\'' + data['surname'] + '\'' + ''', 0, 0, False,0,0,0)
                '''
                print(query)
                user = mySQL_connection(query, True)
                print("Pomyslnie utworzono konto, Witamy Cie:", data['name'], data['surname'], "\b!")

                registration_panel.destroy()
                self.sign_in_client()
            else:
                print("Wpisz jeszcze raz")

        get_created = Button(registration_panel, text="Create an Account", width=self.button_width,
                             height=self.button_height, command=create_user)
        get_created.grid(row=6, column=1)


def end():
    exit(1)
