import tkinter as tk

root = tk.Tk()
Frame1 = tk.Frame(root)

tk.Button(Frame1, text="A1", bg="red").pack(side=tk.TOP, fill=tk.X)
tk.Button(Frame1, text="A2").pack(side=tk.LEFT, fill=tk.X)
tk.Button(Frame1, text="A3").pack(side=tk.LEFT, fill=tk.X)
tk.Button(Frame1, text="B1").pack(side=tk.RIGHT, fill=tk.X)
tk.Button(Frame1, text="B2").pack(side=tk.TOP)
Frame1.pack()

root.mainloop()
