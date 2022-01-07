from tkinter import *
from helpers import create_inputs

e_ids = ['1', '2', '3']
e_pas = ['a', 'b', 'c']


def get_inputs(inputs, data):
    for key in inputs:
        input = inputs[key].get()
        inputs[key].delete(0, END)
        data[key] = input


class Log():

    def __init__(self):
        self.root = Tk()
        self.root.title("Employee panel")  # glowny interfejs

        self.main_container = Frame(self.root)
        self.main_container.pack()

        l_in = Button(self.main_container, text="Log in", padx=83, pady=40, command=self.log_in)
        ex = Button(self.main_container, text="Exit", padx=68, pady=40, command=end)

        l_in.grid(row=1, column=1)
        ex.grid(row=2, column=1)

    def log_in(self):

        self.root.destroy()

        login_panel = Tk()
        login_panel.title("Enter data")

        def submit():
            data = dict()
            get_inputs(inputs, data)

            for i in range(len(e_ids)):
                if data['Employee_ID'] == e_ids[i]:
                    if data['Password'] == e_pas[i]:
                        print("You are successfully logged!\nWelcome employee", e_ids[i])

                        class Emp_Panel():

                            def __init__(self):

                                self.emp_panel = Tk()
                                self.emp_panel.title("Employee panel")
                                self.var = IntVar()
                                self.var2 = IntVar()

                                c = Checkbutton(self.emp_panel, text="Approve application", variable=self.var, command=self.application_approved)
                                c2 = Checkbutton(self.emp_panel, text="Reject application", variable=self.var2, command=self.application_rejected)
                                c.deselect()
                                c2.deselect()
                                c.pack()
                                c2.pack()

                            def reinitialize(self):
                                self.emp_panel.destroy()
                                self = Emp_Panel()

                            def application_approved(self):
                            #laczenie z serwerem potem wniosek znika i reinicjalizacja
                                print("YES")
                                self.reinitialize()

                            def application_rejected(self):
                                print("NO")
                                self.reinitialize()

                        b = Emp_Panel()

            login_panel.destroy()

        fields = ["Employee_ID", "Password"]
        inputs = create_inputs(fields, login_panel)

        sub = Button(login_panel, text="Submit", padx=87, pady=40, command=submit)
        sub.grid(row=3, column=1)


def end():
    exit(1)

a = Log()
a.root.mainloop()