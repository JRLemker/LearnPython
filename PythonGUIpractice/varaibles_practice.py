import tkinter as tk
from tkinter import ttk

#create two entyr fields and one label, they should all be connected via a stringvar, st a start value of 'test'

#window
window = tk.Tk()
window.title('Practice')

#variables
variable = tk.StringVar(value='Test')

#label
label = ttk.Label(master=window, textvariable=variable)
label.pack()

#entries
entry1 = tk.Entry(master=window, textvariable=variable)
entry1.pack()

entry2 = tk.Entry(master=window, textvariable=variable)
entry2.pack()

#run
window.mainloop()
