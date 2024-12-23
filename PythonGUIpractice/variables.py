import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set('button pressed')

#window
window = tk.Tk()
window.title('Tkinter Variables')

#tkinter variable
string_var = tk.StringVar(value="start value")


#widgets
lable = ttk.Label(master=window, text = 'label', textvariable=string_var) #remeber textvariable overwrites text
lable.pack()

entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()

entry2 = ttk.Entry(master=window, textvariable=string_var)
entry2.pack()

button = ttk.Button(master=window, text='button', command=button_func)
button.pack()




#run
window.mainloop()