# -*- coding:utf-8 -*-
from os import path
from subprocess import Popen, PIPE
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename


def Upgrade():
    fm2.pack(expand=YES)


def Openf():
    # fm2.destroy()
    fm2.pack_forget()  # 删除fm2
    if True == path.exists('C:\\Program Files (x86)\\'):
        initdir = 'C:\\Program Files (x86)\\'
    else:
        initdir = 'C:\\Program Files\\'
    file_path = askopenfilename(title='Select the diagnostic instrument .exe file', filetypes=[
                                ('EXE', '*.exe'), ('All Files', '*')], initialdir=initdir)  # 打开文件选择框
    Popen(file_path, shell=True, stdin=PIPE,
          stdout=PIPE, stderr=PIPE)  # 新建管道，执行exe文件


if __name__ == '__main__':
    root = Tk()
    root.title('FileDown')
    # root.iconbitmap('i.ico')
    # root.resizable(0,0)
    mw, mh = root.maxsize()
    root.geometry('360x150+%d+%d' % ((mw-360)/2, (mh-150)/2))  # 窗口居中

    # 创建一个下拉列表
    # number = StringVar()#窗体自带的文本，新建一个值
    numberChosen = ttk.Combobox(root, width=40)
    comboxlist = ['1', '2', '3']
    numberChosen['values'] = comboxlist  # 设置下拉列表的值
    numberChosen.pack(side=TOP, expand=YES)  # 设置其在界面中出现的位置
    numberChosen["state"] = "readonly"
    numberChosen.set("Please choose diagnostic instrument")
    numberChosen.bind("<<ComboboxSelected>>")  # 绑定事件

    fm1 = Frame(root)

    OpenB = Button(fm1, text="Open", fg='green', activeforeground='yellow',
                   command=Openf).pack(side=LEFT, expand=YES)  # 创建按钮
    CancelB = Button(fm1, text="Cancel", fg='green', activeforeground='yellow',
                     command=root.quit) .pack(side=LEFT, expand=YES)  # 创建按钮
    UpgradeB = Button(fm1, text="Upgrade", fg='green', activeforeground='yellow',
                      command=Upgrade) .pack(side=LEFT, expand=YES)  # 创建按钮
    # B.pack()
    fm1.pack(ipadx=20, expand=YES)

    fm2 = Frame(root)

    t = Text(fm2, state='normal')
    t.focus_set()
    s = Scrollbar(fm2)
    s.pack(side=RIGHT, fill=Y)  # 设置滚动条
    t.pack(side=RIGHT, fill=Y)
    s.config(command=t.yview)
    t.config(yscrollcommand=s.set)
    # fm2.pack()
    root.update()
    root.mainloop()
