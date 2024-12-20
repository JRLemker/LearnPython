import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from ttkbootstrap.constants import *

def start_action():
    print("Start button pressed")

def stop_action():
    print("Stop button pressed")

# Create the main window
root = tk.Tk()
root.geometry("800x600")

# Apply the ttkbootstrap style
style = Style()

# Center the grid within the main window
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Create and place the width label and entry
width_label = ttk.Label(root, text="Width:")
width_label.grid(row=0, column=0, padx=10, pady=10)

width_entry = ttk.Entry(root)
width_entry.grid(row=0, column=1, padx=10, pady=10)

# Create and place the feed label and spinbox
feed_label = ttk.Label(root, text="Feed:")
feed_label.grid(row=1, column=0, padx=10, pady=10)

feed_spinbox = ttk.Spinbox(root, from_=0, to=100, increment=1)
feed_spinbox.grid(row=1, column=1, padx=10, pady=10)

# Create and place the start button (green)
start_button = ttk.Button(root, text="Start", command=start_action, bootstyle="success")
start_button.grid(row=2, column=0, padx=10, pady=20)

# Create and place the stop button (red)
stop_button = ttk.Button(root, text="Stop", command=stop_action, bootstyle="danger")
stop_button.grid(row=2, column=1, padx=10, pady=20)

# Run the application
root.mainloop()
