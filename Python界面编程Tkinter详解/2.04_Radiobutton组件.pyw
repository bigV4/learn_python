import tkinter as tk

def sel():
    #一个回调函数
    val = "Radiobutton value is " + str(var.get())
    print(val)
    print("sel是一个",type(sel))

#Radiobutton -个单选框组件。主要给用户提供单个选项的选中功能。
#w = tkinter.Radiobutton(parent，option. ...)
#deselect()方法： 清除单选按钮的状态
#flash()方法： 在激活状态颜色和正常颜色之间闪烁几次单选按钮,但保持它开始时的状态。
#invoke()方法： 可以调用此方法来获得与用户单击单选按钮以更改其状态时发生的操作相同的操作
#select()方法： 设置单选按钮为选中。
#toggle()方法： 反选。当前被选中,则调用之后变为未选中,反之则为选中。

root = tk.Tk()

#创建整型交量。用于绑定，相同的整型变量是为同一组
var = tk.IntVar()

tk.Radiobutton(root, text="男性", variable=var, value=1, command=sel).pack()
tk.Radiobutton(root, text="女性", variable=var, value=2, command=sel).pack()
tk.Radiobutton(root, text="中性", variable=var, value=3, command=sel).pack()


root.mainloop() # GUI程序一定要有个主循环