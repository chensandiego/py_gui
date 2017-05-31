import tkinter as tk
from tkinter import ttk

win=tk.Tk()


win.title('python gui')

#add a label
a_label=ttk.Label(win,text="A lable")
a_label.grid(column=0,row=0)


#button click event
def click_me():
    action.configure(text="** i have been clicked**")
    a_label.configure(foreground='red')
    a_label.configure(text='A red lable')

#add a button
action=ttk.Button(win,text="click me",command=click_me)
action.grid(column=1,row=0)

#sart the gui





win.mainloop()
