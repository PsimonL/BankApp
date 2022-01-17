from tkinter import *
from db.queries import *
from helpers import mySQL_connection, create_inputs, get_inputs


class ClientPanel():
    def __init__(self, user):
        self.user = user
        self.emp_panel = Tk()
        self.emp_panel.title("Client panel")

        self.client_container = Frame(self.emp_panel)
        self.client_container.pack()

        self.account_applications_container = Frame(self.client_container)
        self.account_applications_container.grid(row=0)

        wallet = mySQL_connection("select * from wallets where accountNumber=" + str(user[0]))
        currency = mySQL_connection("select * from currencies where id=" + str(wallet[4]))

        self.value_of_wallet = str(float(currency[2]) * float(wallet[2]))
        currency_name = currency[1].upper()

        welcome_text = "Welcome " + user[3] + " " + user[4]
        wallet_text = "Value " + self.value_of_wallet + currency_name

        welcome_label = Label(self.client_container, text=welcome_text)
        welcome_label.grid(row=0, column=0)

        self.wallet_label = Label(self.client_container, text=wallet_text)
        self.wallet_label.grid(row=1, column=0)
        self.client_container.grid_rowconfigure(1, minsize=55)

        self.transfer_button = Button(self.client_container, text="start a money transfer", command=self.transfer_money)
        self.transfer_button.grid(row=2)
        self.fields = ['account', 'value']
        self.error_labels = dict()
        self.data = dict()

        self.transfer_error_label = Label(self.client_container, text="You cannot transfer more than you have")
        self.self_transfer_error_label = Label(self.client_container, text="You cannot transfer money to yourself")

    def transfer_money(self):
        def submit_transfer():
            if not get_inputs(inputs, self.data, self.error_labels):
                return
            if float(self.data['value']) > float(self.value_of_wallet):
                self.transfer_error_label.grid(row=6)
                return
            if str(self.data['account']) == str(self.user[0]):
                self.self_transfer_error_label.grid(row=7)
                return

            clients_wallet_value = str(float(self.value_of_wallet) - float(self.data['value']))
            receipient_initial_wallet = mySQL_connection(select_wallet_by_account_query + self.data['account'])[2]
            recipient_wallet_value = str(receipient_initial_wallet + float(self.data['value']))

            mySQL_connection(
                "UPDATE wallets SET value =" + recipient_wallet_value + " WHERE accountNumber =" + self.data[
                    'account'],
                True)
            mySQL_connection(
                "UPDATE wallets SET value =" + clients_wallet_value + " WHERE accountNumber =" + str(
                    self.user[0]),
                True)
            self.reinitialize()

        self.transfer_button.grid_forget()
        inputs = create_inputs(self.fields, self.client_container, self.error_labels)

        submit_transfer_button = Button(self.client_container, text="transfer!!!", command=submit_transfer)
        submit_transfer_button.grid(row=3)

    def reinitialize(self):
        self.emp_panel.destroy()
        ClientPanel(self.user)


def end():
    exit(1)
