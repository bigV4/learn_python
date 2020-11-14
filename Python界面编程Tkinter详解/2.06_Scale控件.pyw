import tkinter as tk

def sel():
    #一个回调函数
    val = "Entry value is " + str(var.get())
    print(val)
    print("sel是一个",type(sel))

#Scale -个滑块控件。用于在一个范围内，拖动他改变值的大小。例如音量条。 
#

root = tk.Tk()

var = tk.IntVar()


tk.Scale(root, orient='horizonta', variable=var, from_=0, to=100, tickinterval=50, length=200).pack()
tk.Scale(root, orient='vertical', variable=var, from_=0, to=100, tickinterval=50, length=200).pack()


root.mainloop() # GUI程序一定要有个主循环