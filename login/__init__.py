from tkinter import *
from helpers import create_inputs, con
from login_employee import *


def get_inputs(inputs, data):
    for key in inputs:
        input = inputs[key].get()
        inputs[key].delete(0, END)
        data[key] = input


class Sign():
    login_counter = 0
    isLogged = False

    def reinitialize(self):
        self.root.destroy()
        self = Sign()

    def __init__(self):
        self.root = Tk()
        self.root.title("Bank")  # glowny interfejs

        self.main_container = Frame(self.root)
        self.main_container.pack()
        c_u = Button(self.main_container, text="Stworz konto", padx=77, pady=40, command=self.sign_up)
        l_in = Button(self.main_container, text="Zaloguj sie", padx=83, pady=40, command=self.log_in)
        ex = Button(self.main_container, text="Wyjdz z aplikacji", padx=68, pady=40, command=end)

        c_u.grid(row=1, column=1)
        l_in.grid(row=2, column=1)
        ex.grid(row=3, column=1)

        self.return_button = Button(self.root, text="return", padx=33, pady=10, command=self.reinitialize)
        self.isRoot = True
        self.set_return_visible()

    def set_return_visible(self):
        if not self.isRoot:
            self.return_button.pack(side='bottom')
        else:
            self.return_button.pack_forget()

    def log_in(self):
        self.isRoot = False
        self.set_return_visible()

        if self.isLogged:
            pass
        fields = ['pesel', 'password']
        data = dict()

        self.main_container.destroy()
        login_container = Frame(self.root)
        login_container.pack()

        self.root.title("Login Panel")

        inputs = create_inputs(fields, login_container)

        def log():
            if self.login_counter > 2:
                print("Zbyt wiele nieudanych prob logowania!")
                self.root.destroy()
            get_inputs(inputs, data)
            query = 'Select * from clients where clients.pesel=' + data['pesel']
            user = con(query)
            print(query)
            print(user)
            if user[2] == data['password']:
                print("Zalogowany jako:", data['pesel'])
                login_container.destroy()
            else:
                self.login_counter += 1
                print("Zly login lub haslo!")

        get_logged = Button(login_container, text="Log in", padx=65, pady=50, command=log)

        get_logged.grid(row=4, column=1)

    def recover_password(self) -> None:  # void()
        pass

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

        def create_user():
            get_inputs(inputs, data)
            date_of_birth = data['date']
            print(data['password'])
            print(data['confirm_password'])
            # ta sama zabawa; pesel musi miec 13 liter itd...
            if data['confirm_password'] == data['password'] and len(data['pesel']) == 11:
                query = '''
                INSERT INTO `clients` ( `pesel`, `password`, `name`, `surname`, `balance`, `accountNumber`,`confirmed`) 
                VALUES ('''  '\'' + data['pesel'] + '\'' + ',' + '\'' + data['password'] + '\'' + ',' + '\'' + data[
                    'name'] + '\'' + ',' + '\'' + data[
                            'surname'] + '\'' + ''', 0, 0, False)
                '''

                user = con(query, True)
                print("Pomyslnie utworzono konto, Witamy Cie:", data['name'], data['surname'], "\b!")
                registration_panel.destroy()
                self.log_in()
            else:
                print("Wpisz jeszcze raz")

        get_created = Button(registration_panel, text="Create an Account", padx=65, pady=50, command=create_user)
        get_created.grid(row=6, column=1)


def end():
    exit(1)
