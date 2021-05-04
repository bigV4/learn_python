import tkinter as tk
root = tk.Tk()
root.geometry('300x240')
b1 = tk.Scrollbar(root, cursor='spider')
b1.pack(side=tk.RIGHT, fill=tk.Y)

root.mainloop()
