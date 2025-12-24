import tkinter as tk
r = tk.Tk()
r.title ('Counting Seconds')
buttom = tk.Buttom(r, text='stop', width=25, command=r.destroy)
buttom.pack()
r.mainloop()
