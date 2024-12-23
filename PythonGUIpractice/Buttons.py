import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Buttons')
window.geometry('600x400')


# Button
def button_func():
    print('a basic button')


button_string = tk.StringVar(value='A button with string var')
button = ttk.Button(window, text='Simple Button', command=button_func, textvariable=button_string)
button.pack()

# Checkbox, no attribute for .get(), must use variable
check_var = tk.IntVar(value=10)  # setting value to onvalue designated below
check1 = ttk.Checkbutton(window, text='checkbox 1', command=lambda: print(check_var.get()), variable=check_var,
                        onvalue=10, offvalue=5)  # the print function is returning a string unless use intVar
check1.pack()


check2 = ttk.Checkbutton(window, text='Checkbox 2', onvalue=1, offvalue=0, command=lambda : check_var.set(5)) #command set variable to offvalue for checkbox 1
check2.pack()


# radio buttons
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(window, text='Radiobutton 1', value='radio 1', variable=radio_var,
                         command=lambda: print(radio_var.get()))
radio1.pack()
radio2 = ttk.Radiobutton(window, text='Radiobutton 2', value=2, variable=radio_var, command=lambda: print(radio_var.get()))  # each needs a unique value, doesnt matter what
radio2.pack()

# run
window.mainloop()
