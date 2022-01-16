from tkinter import *
from tkcalendar import DateEntry
from mysql.connector import connect, Error
from dotenv import load_dotenv

import os

load_dotenv()
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


def con(query="select * from clients", is_update=False,is_multi=False):

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
                elif(is_multi):
                    res=cursor.fetchall()
                    for el in res:
                        print(el)
                    return res
                else:
                    for el in cursor:
                        print(el)
                        return el


    except Error as e:
        print(e)
def get_inputs(inputs, data):
    for key in inputs:
        input = inputs[key].get()
        inputs[key].delete(0, END)
        data[key] = input