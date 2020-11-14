import tkinter as tk

def sel():
    #一个回调函数
    val = "Entry value is " + str(var.get())
    print(val)
    print("sel是一个",type(sel))

#Entry -个单行文本输入框。可以用来接受用户的输入,但是只能输入一行。 
#如果你只是想显示而不是编辑.那么应该使用标签。
#--w = tkinter.Entry(parent, option-value ... )
#需要注意-点， Entry与Lable和Button不同,其text属性是无效的。那么需要让Entry显示文字该如何操作。

root = tk.Tk()

var = tk.StringVar()
var.set("提示：这是一个单行输入框")

tk.Entry(root, textvariable=var).pack()
tk.Entry(root, show="*").pack()
tk.Checkbutton(root, text="跳舞", command=sel).pack()


root.mainloop() # GUI程序一定要有个主循环