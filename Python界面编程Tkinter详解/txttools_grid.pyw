#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
import hashlib
import time
import base64

LOG_LINE_NUM = 0


class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.textwidget = None

    def attach(self, Text_widget):
        self.textwidget = Text_widget

    def redraw(self, *args):
        '''redraw line numbers'''
        self.delete("all")

        i = self.textwidget.index("@0,0")
        while True:
            dline = self.textwidget.dlineinfo(i)
            if dline is None:
                break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2, y, anchor="nw", Text=linenum)
            i = self.textwidget.index("%s+1line" % i)


class CustomText(tk.Text):
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)

        # create a proxy for the underlying widget
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

    def _proxy(self, *args):
        # let the actual widget perform the requested action
        cmd = (self._orig,) + args
        result = self.tk.call(cmd)

        # generate an event if something was added or deleted,
        # or the cursor position changed
        if (args[0] in ("insert", "replace", "delete") or
            args[0:3] == ("mark", "set", "insert") or
            args[0:2] == ("xview", "moveto") or
            args[0:2] == ("xview", "scroll") or
            args[0:2] == ("yview", "moveto") or
            args[0:2] == ("yview", "scroll")
            ):
            self.event_generate("<<Change>>", when="tail")

        # return what the actual widget returned
        return result


class TextBoxExample(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = CustomText(self)
        self.vsb = tk.Scrollbar(orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.text.tag_configure("bigfont", font=("Helvetica", "24", "bold"))
        self.linenumbers = TextLineNumbers(self, width=30)
        self.linenumbers.attach(self.text)

        self.vsb.pack(side="right", fill="y")
        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="right", fill="both", expand=True)

        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)

    def _on_change(self, event):
        self.linenumbers.redraw()


class MY_GUI():
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

    # 设置窗口

    def set_init_window(self):
        self.init_window_name.title("文本处理工具_v1.2")  # 窗口名
        # self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('1140x650+10+10')
        # self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        # self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        # 标签
        self.init_data_label = tk.Label(self.init_window_name, text="明文数据")
        self.init_data_label.grid(row=0, column=2)
        self.action_button_label = tk.Label(self.init_window_name, text="方法")
        self.action_button_label.grid(row=0, column=67)
        self.result_data_label = tk.Label(self.init_window_name, text="编码数据")
        self.result_data_label.grid(row=0, column=89)
        self.log_label = tk.Label(self.init_window_name, text="日志")
        self.log_label.grid(row=37, column=0)
        # 文本框
        self.init_data_Text = TextBoxExample(
            self.init_window_name, width=67, height=35)  # 原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=35, columnspan=67)
        self.result_data_Text = TextBoxExample(
            self.init_window_name, width=67, height=35)  # 处理结果展示
        self.result_data_Text.grid(row=1, column=87, rowspan=35, columnspan=67)
        self.log_data_Text = TextBoxExample(
            self.init_window_name, width=154, height=9)  # 日志框
        self.log_data_Text.grid(row=37, column=2, columnspan=154)
        # 按钮
        self.str_trans_to_md5_button = tk.Button(self.init_window_name, text="字符串转MD5--->",
                                                 bg="lightblue", width=20, command=self.str_trans_to_md5)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=1, column=67, rowspan=1)
        self.str_trans_to_md5_button = tk.Button(self.init_window_name, text="字符串转BASE64--->",
                                                 bg="lightblue", width=20, command=self.str_trans_to_base64)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=2, column=67, rowspan=1)
        self.str_trans_to_md5_button = tk.Button(self.init_window_name, text="<---BASE64转字符串",
                                                 bg="lightblue", width=20, command=self.str_trans_to_md5)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=3, column=67, rowspan=1)
        self.str_trans_to_upper_button = tk.Button(
            self.init_window_name, text="字符串转大写--->", bg="lightblue", width=20, command=self.str_trans_to_base64)  # 调用内部方法  加()为直接调用
        self.str_trans_to_upper_button.grid(row=4, column=67, rowspan=1)
        self.str_trans_to_lower_button = tk.Button(
            self.init_window_name, text="字符串转小写--->", bg="lightblue", width=20, command=self.str_trans_to_base64)  # 调用内部方法  加()为直接调用
        self.str_trans_to_lower_button.grid(row=5, column=67, rowspan=1)

    # 功能函数

    def str_trans_to_md5(self):
        src = self.init_data_Text.get(
            1.0, tk.END).strip().replace("\n", "").encode()
        #print("src =",src)
        if src:
            try:
                myMd5 = hashlib.md5()
                myMd5.update(src)
                myMd5_Digest = myMd5.hexdigest()
                # print(myMd5_Digest)
                # 输出到界面
                self.result_data_Text.delete(1.0, tk.END)
                self.result_data_Text.insert(1.0, myMd5_Digest)
                self.write_log_to_Text("INFO:str_trans_to_md5 success")
            except:
                self.result_data_Text.delete(1.0, tk.END)
                self.result_data_Text.insert(1.0, "字符串转MD5失败")
        else:
            self.write_log_to_Text("ERROR:str_trans_to_md5 failed")

    def str_trans_to_base64(self):
        src = self.init_data_Text.get(
            1.0, tk.END).strip().replace("\n", "").encode()
        #print("src =",src)
        if src:
            try:
                myBase64_Digest = base64.b64encode(src)
                # print(myMd5_Digest)
                # 输出到界面
                self.result_data_Text.delete(1.0, tk.END)
                self.result_data_Text.insert(1.0, myBase64_Digest)
                self.write_log_to_Text("INFO:str_trans_to_base64 success")
            except:
                self.result_data_Text.delete(1.0, tk.END)
                self.result_data_Text.insert(1.0, "字符串转base64失败")
        else:
            self.write_log_to_Text("ERROR:str_trans_to_base64 failed")

    # 获取当前时间

    def get_current_time(self):
        current_time = time.strftime(
            '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return current_time

    # 日志动态打印
    def write_log_to_Text(self, logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) + " " + str(logmsg) + "\n"  # 换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(tk.END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0, 2.0)
            self.log_data_Text.insert(tk.END, logmsg_in)


def gui_start():
    init_window = tk.Tk()  # 实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()  # 父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()
