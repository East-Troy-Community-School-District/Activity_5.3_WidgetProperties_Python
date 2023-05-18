'''
Disappearing Buttons
Pawelski
5/15/2023
Python II
'''

import tkinter as tk

# -- Event Handlers --
def button1_click():
    '''
    Causes the first button to disappear and other reappear.
    '''
    button1.pack_forget()
    button2.pack(side=tk.RIGHT, padx=2, pady=2)
    button3.pack(side=tk.LEFT, padx=2, pady=2)
    button4.pack(side=tk.RIGHT, padx=2, pady=2)


def button2_click():
    '''
    Causes the second button to disappear and other reappear.
    '''
    button1.pack(side=tk.LEFT, padx=2, pady=2)
    button2.pack_forget()
    button3.pack(side=tk.LEFT, padx=2, pady=2)
    button4.pack(side=tk.RIGHT, padx=2, pady=2)


def button3_click():
    '''
    Causes the third button to disappear and other reappear.
    '''
    button1.pack(side=tk.LEFT, padx=2, pady=2)
    button2.pack(side=tk.RIGHT, padx=2, pady=2)
    button3.pack_forget()
    button4.pack(side=tk.RIGHT, padx=2, pady=2)


# Add the missing event handler here!

# -- GUI --
window = tk.Tk()
window.title("Positioning Buttons")

top_frame = tk.Frame(window)
button1 = tk.Button(top_frame, text="Button 1", command=button1_click)
button2 = tk.Button(top_frame, text="Button 2", command=button2_click)
button1.pack(side=tk.LEFT, padx=2, pady=2)
button2.pack(side=tk.RIGHT, padx=2, pady=2)
top_frame.pack(fill=tk.X)

bottom_frame = tk.Frame(window)
button3 = tk.Button(bottom_frame, text="Button 3", command=button3_click)
button4 = tk.Button(bottom_frame, text="Button 4")	# Update this line to call the event handler!
button3.pack(side=tk.LEFT, padx=2, pady=2)
button4.pack(side=tk.RIGHT, padx=2, pady=2)
bottom_frame.pack(fill=tk.X)

window.mainloop()