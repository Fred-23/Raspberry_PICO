from tkinter import *
from tkinter import ttk
panel= Tk()
frm = ttk.Frame(panel, padding = 100)
frm.grid()
ttk==.Label(frm, text="Fred Oscilloscope").pack(side="top")
#ttk.Label(frm, text="Fred Oscilloscope").grid(column=0, row=0)
#ttk.Button(frm, text="Quit", command=panel.destroy).grid(column=300, row=300)
ttk.Button(frm, text="Quit", command=panel.destroy).pack(side="bottom")
panel.mainloop()
#ttk.colorchooser.askcolor()