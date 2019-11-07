import tkinter as tk
import time


def countDown(countdown):
    '''start countdown 10 seconds before new year starts'''
    lbl.config(bg='yellow')
    for k in range(int(countdown), -1, -1):
        lbl["text"] = k
        time.sleep(1)
        root.update()  # Tk needs this after sleep()
    lbl.config(bg='red')
    lbl["text"] = "IT's GAME TIME!!!!!!!"


root = tk.Tk()
label_font = ('helvetica', 40)
lbl = tk.Label(font=label_font)
lbl.pack(fill='both', expand=1)
countDown(5)
root.mainloop()
