'''
Funky Labels
Pawelski
5/17/2023
Python II
'''

import tkinter as tk

# -- GUI --
window = tk.Tk()
window.title("Funky Labels")
window.geometry("500x350+750+300")
window.config(bg="aquamarine")

photo = tk.PhotoImage(file="cat.png")
picture_label = tk.Label(window,
                         image=photo,
                         height=200,
                         width=200,
                         background="aquamarine")
picture_label.pack(padx=5, pady=5)

message_label = tk.Label(window,
                         text="It's beautiful!",
                         font=("Comic Sans", 32, "bold"),
                         anchor=tk.CENTER,
                         bg="burlywood",
                         fg="lightcoral",
                         relief=tk.RAISED,
                         height=2,
                         width=15)
message_label.pack(padx=5, pady=5)

# Add your label here!

window.mainloop()