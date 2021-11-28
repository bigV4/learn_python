import tkinter as tk

root = tk.Tk()
Frame1 = tk.Frame(root)

tk.Label(Frame1, text="Pack布局的side和fill").pack()
tk.Button(Frame1, text="LEFT1,Y").pack(side=tk.LEFT, fill=tk.Y)
tk.Button(Frame1, text="TOP1,X").pack(side=tk.TOP, fill=tk.X)
tk.Button(Frame1, text="RIGHT1,Y").pack(side=tk.RIGHT, fill=tk.Y)
tk.Button(Frame1, text="TOP2,BOTH").pack(side=tk.TOP, fill=tk.BOTH)
tk.Button(Frame1, text="TOP3,").pack(side=tk.TOP)
tk.Button(Frame1, text="TOP4,").pack()
tk.Button(Frame1, text="RIGHT2,NONE").pack(side=tk.RIGHT, fill=tk.NONE)

Frame2 = tk.Frame(root)
tk.Label(Frame2, text="Pack布局的拉手效果布局，使用了expand").pack()
tk.Button(Frame2, text="A").pack(side=tk.LEFT, expand=1)
tk.Button(Frame2, text="B").pack(side=tk.LEFT, expand=1, fill=tk.X)
tk.Button(Frame2, text="C").pack(side=tk.LEFT, expand=1)

Frame3 = tk.Frame(root)
tk.Label(Frame3, text="Pack布局，没有expand，都挤在一起").pack()
tk.Button(Frame3, text="A").pack(side=tk.LEFT)
tk.Button(Frame3, text="B").pack(side=tk.LEFT, fill=tk.X)
tk.Button(Frame3, text="C").pack(side=tk.LEFT)

Frame4 = tk.Frame(root)
letter = ['A', 'B', 'C']
tk.Label(Frame4, text="Pack布局的例子").pack()
for i in letter:
    tk.Label(Frame4, text=i, relief='groove').pack(fill='both', expand=True)
for i in letter:
    tk.Label(Frame4, text=i+" left", relief='groove').pack(
        side='left', fill='both', expand=True)
for i in letter:
    tk.Label(Frame4, text=i+" bottom", relief='groove').pack(
        side='bottom', fill='both', expand=True)
for i in letter:
    tk.Label(Frame4, text=i+" right", relief='groove').pack(
        side='right', fill='both', expand=True)

# 需注意，顶部框架不会展开，也不会填充X或Y方向
Frame1.pack(expand=1, fill='both')
Frame2.pack(expand=1, fill='both')
Frame3.pack(expand=1, fill='both')
Frame4.pack(expand=1, fill='both')

tk.Label(root, text="Pack 布局的 expand").pack()
tk.Button(root, text="我不扩展").pack()
tk.Button(root, text="我不向x方向填充，但我扩展expand").pack(expand=1)
tk.Button(root, text="我向x方向填充fill，并且扩展expand").pack(fill=tk.X, expand=1)
tk.Label(root, text="[*] expand对应的是要求但未使用的空间").pack(expand=1)
tk.Label(root, text="[*] fill对应的是要求并已使用的空间，将所有要求的空间占满").pack(fill=tk.X)

root.mainloop()
