import tkinter as tk
i = 0 
def sel():
    global i 
    i = i + 1
    #一个回调函数
    s1 = str(my_string.get())
    print("Entry value is " + s1)
    s2 = str(ticked_yes.get())
    print("Checkbutton value is " + s2)
    s3 = str(group_choice.get())
    print("Radiobutton value is " + s3)
    s4 = str(volume.get())
    print("Scale value is " + s4)
    print("sel是一个",type(sel))
    quote = "[%d]  Entry:%s,\tCheckbutton:%s,\tRadiobutton:%s,\tScale:%s\n"%(i,s1,s2,s3,s4)
    print(quote)
    T.insert(tk.END,quote)

#Scale -个滑块控件。用于在一个范围内，拖动他改变值的大小。例如音量条。 
#

root = tk.Tk()
# 为了响应特定小控件的值的变化, Tkinter提供了自己的变量类,它们可以用来跟踪这些小控件的值。
#字符串型
my_string = tk.StringVar()
my_string.set("提示信息")
my_string2 = tk.StringVar()

#布尔型
ticked_yes = tk.BooleanVar()

#整形
group_choice = tk.IntVar()

#浮点型
volume = tk.DoubleVar()

#将变量类与控件关联
tk.Entry(root, textvariable=my_string).pack()
tk.Checkbutton(root, text="选我" , variable=ticked_yes).pack()
tk.Radiobutton(root, text="点我1", value=1, variable=group_choice).pack()
tk.Radiobutton(root, text="点我2", value=2, variable=group_choice).pack()
tk.Radiobutton(root, text="点我3", value=3, variable=group_choice).pack()
tk.Scale(root, label="音量", variable=volume).pack()

tk.Button(root,text="按钮",command=sel).pack()
T = tk.Text(root,height=5, width=100)
T.pack()





root.mainloop() # GUI程序一定要有个主循环