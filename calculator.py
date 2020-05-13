from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math

root = Tk()
root.title('Калькулятор')

buttons = [
'7', '8', '9', '+', '*',
'4', '5', '6', '-', '/',
'1', '2', '3',  '=', 'xⁿ',
'0', '.', '±',  'C', '√x',
'(', ')',  '1/x', 'История']

history = []

row_id = 1
col_id = 0
for button in buttons:
    cmd = lambda x=button: calc(x)
    ttk.Button(root, text=button, command=cmd, width=10).grid(row=row_id, column=col_id)
    col_id += 1
    if col_id > 4:
        col_id = 0
        row_id += 1

calc_entry = Entry(root, width=50)
calc_entry.grid(row=0, column=0, columnspan=4)


def calc(key):
    if key == '=':
        symbols = '0123456789*/()-+.'
        if calc_entry.get()[0] not in symbols:
            messagebox.showerror('Ошибка', 'Проверьте правильность введенных данных.')
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, '=' + str(result))
            history.append(f'{calc_entry.get()}\n')
        except:
            messagebox.showerror('Ошибка', 'Проверьте правильность введенных данных.')
    elif key == 'C':
        calc_entry.delete(0, END)
    elif key == '±':
        if '=' in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == '-':
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, '-')
        except IndexError:
            pass
    elif key == 'xⁿ':
        calc_entry.insert(END, '**')
    elif key == '(':
        calc_entry.insert(END, '(')
    elif key == ')':
        calc_entry.insert(END, ')')
    elif key == '√x':
        calc_entry.insert(END, '=' + str(math.sqrt(int(calc_entry.get()))))
    elif key == '1/x':
        calc_entry.insert(END, '=' + str(1/int(calc_entry.get())))
    elif key == 'История':
        messagebox.showinfo('История вычислений', ''.join(history))
    else:
        if '=' in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)

root.mainloop()