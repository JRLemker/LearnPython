import tkinter as tk
from tkinter import ttk


def button_function():
    #print("A button was pressed")

    #get content of entry
    #print(entry.get())
    entry_text = entry.get()

    #update the label
    #label.configure(text = 'some other text')
    label['text']= entry_text
    entry['state'] = 'disabled'
    print(label.configure())

def hello():
    print('hello')
    label['text'] = 'some text'
    entry['state'] = 'enabled'

#create the window
window = tk.Tk()
#window.attributes('-fullscreen',True)
window.title('Window and Widgets')
window.geometry('800x800')

#ttk label widgets
label = ttk.Label(master=window, text='this is a test')
label.pack()

#create tk text widgets
tk.Text(master=window).pack()

#ttk entry - single line entry
entry = ttk.Entry(master=window)
entry.pack()

#ttk button
button = ttk.Button(master=window,text='Button', command=button_function)
button.pack()


#exercise
#add text label and button with function that prints hello
#label says "my label" and be between the entry widget and the button

exercise = ttk.Frame(master=window)
text = ttk.Label(master=exercise,text='My Label')
text.pack()
exercise_button = ttk.Button(master=exercise,text='Exercise Button', command=hello)
exercise_button.pack()
#also could do
exercise_button2 = ttk.Button(master=exercise,text='Exercise Button 2', command= lambda: print('hello'))
exercise_button2.pack()
exercise.pack(pady=10)



#run
window.mainloop()