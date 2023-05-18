'''
Collect Info
Pawelski
5/17/2023
Python II
'''

import tkinter as tk
import os

# -- Global Variables --
path = "results.txt"

# -- Event Handlers --
def log_info():
    '''
    Writes the user's information to a file.
    '''
    global path
    name = name_entry.get()
    name_entry.delete("0", "end")
    address = address_entry.get()
    address_entry.delete("0", "end")
    city = city_entry.get()
    city_entry.delete("0", "end")
    state = state_entry.get()
    state_entry.delete("0", "end")
    zip_code = zip_entry.get()
    zip_entry.delete("0", "end")
    name_entry.focus_set()
    
    if os.path.exists(path):
        file = open(path, "a")
    else:
        file = open(path, "w")
    file.write(name + "\n")
    file.write(address + "\n")
    file.write(city + ", " + state + ", " + zip_code + "\n\n")
    file.close()

# -- GUI --
window = tk.Tk()
window.title("Collect Info")

name_frame = tk.Frame(window)
name_label = tk.Label(name_frame,
                      text="Name:",
                      font=("Myriad Pro", 20))
name_entry = tk.Entry(name_frame, font=("Myriad Pro", 20))
name_entry.pack(side=tk.RIGHT, padx=2, pady=2)
name_label.pack(side=tk.RIGHT, padx=2, pady=2)
name_frame.pack(fill=tk.X)

address_frame = tk.Frame(window)
address_label = tk.Label(address_frame,
                         text="Address:",
                         font=("Myriad Pro", 20))
address_entry = tk.Entry(address_frame, font=("Myriad Pro", 20))
address_entry.pack(side=tk.RIGHT, padx=2, pady=2)
address_label.pack(side=tk.RIGHT, padx=2, pady=2)
address_frame.pack(fill=tk.X)

city_frame = tk.Frame(window)
city_label = tk.Label(city_frame,
                      text="City:",
                      font=("Myriad Pro", 20))
city_entry = tk.Entry(city_frame, font=("Myriad Pro", 20))
city_entry.pack(side=tk.RIGHT, padx=2, pady=2)
city_label.pack(side=tk.RIGHT, padx=2, pady=2)
city_frame.pack(fill=tk.X)

state_frame = tk.Frame(window)
state_label = tk.Label(state_frame,
                       text="State:",
                       font=("Myriad Pro", 20))
state_entry = tk.Entry(state_frame, font=("Myriad Pro", 20))
state_entry.pack(side=tk.RIGHT, padx=2, pady=2)
state_label.pack(side=tk.RIGHT, padx=2, pady=2)
state_frame.pack(fill=tk.X)

zip_frame = tk.Frame(window)
zip_label = tk.Label(zip_frame,
                     text="Zip:",
                     font=("Myriad Pro", 20))
zip_entry = tk.Entry(zip_frame, font=("Myriad Pro", 20))
zip_entry.pack(side=tk.RIGHT, padx=2, pady=2)
zip_label.pack(side=tk.RIGHT, padx=2, pady=2)
zip_frame.pack(fill=tk.X)

log_button = tk.Button(window,
                       text="Log",
                       font=("Myriad Pro", 20),
                       height=1,
                       width=12,
                       command=log_info)
log_button.pack(padx=5, pady=5)

window.mainloop()