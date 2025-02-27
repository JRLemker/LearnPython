import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk



def convert():
    mile_input = entry_int.get()
    km_output = mile_input*1.61
    output_string.set(km_output)

#window
#window = tk.Tk()
window = ttk.Window(themename='journal')
window.title('Demo')
window.geometry('300x150')

#title
title_label = ttk.Label(master=window, text='Miles to Kilometers', font='Calibri 24 bold')
title_label.pack()

#input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text='Convert', command=convert) #pass the function with command=convert and
#dont call the function with command=convert() since the call function is done by the button
entry.pack(side='left',padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

#output field
output_string = tk.StringVar()
output_label = ttk.Label(master=window,
                         text='Output',
                         font='Calibri 18 bold',
                         textvariable=output_string) #adding textvariable overwrites the text= so it can update dynamically
output_label.pack(pady=5)

#run
window.mainloop()