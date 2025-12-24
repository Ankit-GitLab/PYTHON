from tkinter import *

master = Tk()

# Labels
Label(master, text='First Name').grid(row=0)
Label(master, text='Last Name').grid(row=1)

# Entry boxes
e1 = Entry(master)
e2 = Entry(master)

# Position entries
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

mainloop()
