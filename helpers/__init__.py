from tkinter import *
from tkcalendar import DateEntry
from mysql.connector import connect, Error


def create_inputs(inputs, parent):
    created_inputs = dict()
    for i in range(0, len(inputs)):
        field_name = inputs[i]

        created_inputs[field_name] = ''
        field = locals()[field_name] = ''

        field_container = Frame(parent)
        field_label = Label(field_container, text=field_name.capitalize())
        if field_name == 'date':
            field = DateEntry(field_container, width=35, borderwidth=5)
        else:
            field = Entry(field_container, width=35, borderwidth=5)

        field_container.grid(row=i, column=0, columnspan=3, padx=10, pady=10)
        field_label.pack(side="top")
        field.pack(side='bottom')

        created_inputs[field_name] = field
    return created_inputs


def con(query="describe clients",is_update=False):
    try:
        with connect(
                host="sql11.freemysqlhosting.net",
                user="sql11461517",
                password="Z9nGjqHb1r",
                database="sql11461517"
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                if is_update:
                    connection.commit()
                else:
                    for el in cursor:
                        return el

    except Error as e:
        print(e)
