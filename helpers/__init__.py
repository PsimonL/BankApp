from tkinter import *
from tkcalendar import DateEntry
from mysql.connector import connect, Error
from dotenv import load_dotenv

import os

load_dotenv()


def create_inputs(inputs, parent, error_labels):
    created_inputs = dict()
    created_input_error_labels = dict()
    for i in range(0, len(inputs)):
        field_name = inputs[i]
        error_label_name = inputs[i]


        field = locals()[field_name] = ''

        error_labels[error_label_name] = ''
        error_label = locals()[error_label_name] = ''

        field_container = Frame(parent)

        field_label = Label(field_container, text=field_name.capitalize())
        error_label = Label(field_container, text=field_name.capitalize() + " required!")
        error_labels[error_label_name]=error_label

        if field_name == 'date':
            field = DateEntry(field_container, width=35, borderwidth=5)
        else:
            field = Entry(field_container, width=35, borderwidth=5)

        field_container.grid(row=i, column=0, columnspan=3, padx=10, pady=10)
        field_label.grid(row=1)
        field.grid(row=2)
        error_label.grid_forget()

        created_inputs[field_name] = field
    return created_inputs


def con(query="select * from clients", is_update=False, is_multi=False):
    try:
        with connect(
                host=os.getenv("HOST"),
                user=os.getenv("USER"),
                password=os.getenv("PASSWORD"),
                database=os.getenv("DATABASE")
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                if is_update:
                    connection.commit()
                elif (is_multi):
                    res = cursor.fetchall()
                    for el in res:
                        print(el)
                    return res
                else:
                    for el in cursor:
                        print(el)
                        return el


    except Error as e:
        print(e)


def get_inputs(inputs, data, error_labels):
    is_all_fields_filled=True
    for key in inputs:
        if len(inputs[key].get()) == 0:
            error_labels[key].grid()
            is_all_fields_filled=False
        else:
            error_labels[key].grid_forget()
            input = inputs[key].get()
            data[key] = input
    return is_all_fields_filled
