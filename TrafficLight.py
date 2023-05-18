'''
Traffic Light
Pawelski
5/16/2023
Python II
'''

import tkinter as tk

# -- Global Variables --
green_on = False
yellow_on = False
red_on = True

# -- Event Handlers --
def change_light():
    '''
    Changes the light to the next color.
    '''
    global green_on, yellow_on, red_on
    if green_on:
        # Switches to yellow
        green_frame.config(bg="green4")
        yellow_frame.config(bg="yellow2")
        green_on = False
        yellow_on = True
    elif yellow_on:
        # Switches to red
        yellow_frame.config(bg="yellow4")
        red_frame.config(bg="red2")
        yellow_on = False
        red_on = True
    else:
        # Switches to green
        red_frame.config(bg="red4")
        green_frame.config(bg="green2")
        red_on = False
        green_on = True
    window.after(1000, change_light)

# -- GUI --
window = tk.Tk()
window.title("Traffic Light")
window.geometry("150x450")
window.after(1000, change_light)

red_frame = tk.Frame(window, bg='red2', height=150, width=150)
red_frame.pack()
yellow_frame = tk.Frame(window, bg='yellow4', height=150, width=150)
yellow_frame.pack()
green_frame = tk.Frame(window, bg='green4', height=150, width=150)
green_frame.pack()

window.mainloop()