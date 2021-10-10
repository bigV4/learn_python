import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
cur = filedialog.askopenfilenames(
    filetypes=[('text files', '.txt'), ('pythonfiles', ('.py', '.pyw'))])
if cur:
    print(cur)
else:
    print('你没有选择任何文件')
