#已初步掌握Python3语法，本课程以Python3语法为基础
#GUI编程的三个核心问题
#--1、屏幕上应县是那些组建？认识组件的形态
#--2、组件应该放在哪里？学习组件布局
#--3、组件如何交互？组件中的事件
#Tkinter8.5参考手册手册http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
#Tkinter 8.5 reference: a GUI for Python https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html
import tkinter as tk

def onclick():
    #一个回调函数
    print("我被电击了")
    print("onclick是一个",type(onclick))

root =tk.Tk() #“画板”----根窗口

label_l = tk.Label(root, text="这是一个标签")
label_l.pack() # 把标签放到主画板上

button_b =tk.Button(root, text="这是一个按钮", command=onclick)#这里的onclick是一个<class 'function'>,函数名称，不写括号
button_b.pack() # 把按钮放到主画板上

root.mainloop() # GUI程序一定要有个主循环