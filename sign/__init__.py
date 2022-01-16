import tkinter
from tkinter import *
from helpers import create_inputs, con, get_inputs
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
        self = Sign(self.is_employee)

    def for_employee(self):
        sign_up_button = self.my_button(self.main_container, txt="Log in", command=self.sign_in_employee)
        exit_button = self.my_button(self.main_container, txt="Exit", command=end)

        sign_up_button.grid(row=1, column=1)
        exit_button.grid(row=2, column=1)

    def for_client(self):

        sign_up_button = self.my_button(self.main_container, txt="Stworz konto", command=self.sign_up)
        sign_in_button = self.my_button(self.main_container, txt="Zaloguj sie", command=self.sign_in_client)
        exit_button = self.my_button(self.main_container, txt="Wyjdz z aplikacji", command=end)
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

        self.main_container.destroy()
        self.login_container = Frame(self.root)
        self.login_container.pack()

        self.root.title("Login Panel")

        inputs = create_inputs(fields, self.login_container)

        def recover_password():
            get_inputs(inputs, data)
            print(data['pesel'])
            password = con(select_user_by_pesel_query_part1 + data['pesel'])[4]
            print(password)
            password_label = Label(self.login_container, text="Your password is: " + password)
            password_label.grid(row=3, column=2)

        def log():
            if self.login_counter > 2:
                print("Zbyt wiele nieudanych prob logowania!")
                self.root.destroy()
            get_inputs(inputs, data)
            query = select_client_query + data['pesel']
            user = con(query)

            print(user)
            if user[2] == data['password']:
                print("Zalogowany jako:", data['pesel'])
                self.login_container.destroy()
            else:
                self.login_counter += 1
                print("Zly login lub haslo!")

        get_logged = self.my_button(self.login_container, txt="Log in", command=log)
        retrieve_password_button = self.my_button(self.login_container, txt="Odzyskaj haslo", command=recover_password)
        retrieve_password_button.grid(row=4, column=1)

        get_logged.grid(row=4, column=2)

    def sign_in_employee(self):

        self.root.destroy()

        login_panel = Tk()
        login_panel.title("Enter data")

        def submit():
            data = dict()
            get_inputs(inputs, data)
            user = con(select_unconfirmed_clients_query, False, True)

            for i in range(len(e_ids)):
                if data['Employee_ID'] == e_ids[i] and data['Password'] == e_pas[i]:
                    print("You are successfully logged!\nWelcome employee", e_ids[i])

                    b = EmployeePanel(user)

            login_panel.destroy()

        fields = ["Employee_ID", "Password"]
        inputs = create_inputs(fields, login_panel)

        sub = Button(login_panel, text="Submit", padx=87, pady=40, command=submit)
        sub.grid(row=3, column=1)

    def sign_up(self):
        self.isRoot = False
        self.set_return_visible()
        fields = ["pesel", "name", "surname", "date", "password", "confirm_password"]
        data = dict()

        self.main_container.destroy()
        registration_panel = Frame(self.root)
        registration_panel.pack()

        self.root.title("Create an account")

        inputs = create_inputs(fields, registration_panel)

        def check_is_pesel_valid():
            res=con(select_user_by_pesel_query_part1+ data['pesel'])
            return res is None and len(data['pesel']) == 11

        def create_user():
            get_inputs(inputs, data)
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
                user = con(query, True)
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
