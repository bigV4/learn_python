import tkinter as tk

def onclick():
    #一个回调函数
    print("我被电击了")
    print("onclick是一个",type(onclick))


button_b =tk.Button(root, text="这是一个按钮", command=onclick)#这里的onclick是一个<class 'function'>,函数名称，不写括号
button_b.pack() # 把按钮放到主画板上

root.mainloop() # GUI程序一定要有个主循环