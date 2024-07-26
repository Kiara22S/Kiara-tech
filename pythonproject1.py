import tkinter as tk
from math import *


def evaluate_expression(event=None):
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


def insert_text(text):
    entry.insert(tk.END, text)


def clear_entry():
    entry.delete(0, tk.END)


root = tk.Tk()
root.title("Scientific Calculator")


entry = tk.Entry(root, width=30, font=('Arial', 18), borderwidth=5)
entry.grid(row=0, column=0, columnspan=5)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0), ('sin', 5, 1), ('cos', 5, 2), ('tan', 5, 3),
    ('log', 6, 0), ('ln', 6, 1), ('sqrt', 6, 2), ('^', 6, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18),
                       command=lambda t=text: insert_text(t) if t != '=' else evaluate_expression())
    button.grid(row=row, column=col)


clear_button = tk.Button(root, text='C', width=5, height=2, font=('Arial', 18), command=clear_entry)
clear_button.grid(row=5, column=0)

equals_button = tk.Button(root, text='=', width=5, height=2, font=('Arial', 18), command=evaluate_expression)
equals_button.grid(row=4, column=3)


root.bind('<Return>', evaluate_expression)


root.mainloop()

