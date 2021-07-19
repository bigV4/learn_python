import tkinter as tk
root = tk.Tk()
# root.geometry('300x240')
colours = ['red', 'green', 'orange', 'white', 'yellow', 'blue']

tk.Label(root, text="测试").pack(fill=tk.X)
F1 = tk.Frame(root)
F1.pack(fill=tk.X)
r = 0
for c in colours:
    tk.Label(F1, text=c, relief=tk.RIDGE, width=15).grid(row=r, column=0)
    tk.Entry(F1, bg=c, relief=tk.SUNKEN, width=10).grid(row=r, column=1)
    r = r + 1

root.mainloop()
