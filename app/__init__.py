from tkinter import *
from sign import Sign


class app:
    def __init__(self):
        self.root = Tk()
        self.root.title("Who you are?")  # glowny interfejs
        client_button = Button(self.root, text="I am a client", padx=77, pady=40, command=self.client_mode)
        employee_button = Button(self.root, text="I am an employee", padx=83, pady=40, command=self.employee_mode)

        client_button.grid(row=1, column=2)
        employee_button.grid(row=1, column=1)

    def client_mode(self):
        Sign(False)
        self.root.destroy()

    def employee_mode(self):
        Sign(True)
        self.root.destroy()


my_app = app()
my_app.root.mainloop()
