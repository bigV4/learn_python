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

    def attach(self, text_widget):
        self.textwidget = text_widget

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
            self.create_text(2, y, anchor="nw", text=linenum)
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
        #result = self.tk.call(cmd)
        # tkinter already has a default binding for cut and paste. What's probably happening is that your binding is firing and then the built-in binding is firing
        try:
            result = self.tk.call(cmd)
        except Exception:
            return None

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


class TextWithLineNum(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = CustomText(self)
        self.vsb = tk.Scrollbar(self, orient="vertical",
                                command=self.text.yview, cursor='spider')
        self.text.configure(yscrollcommand=self.vsb.set)
        self.linenumbers = TextLineNumbers(self, width=30)
        self.linenumbers.attach(self.text)

        self.vsb.pack(side="right", fill="y")
        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="right", fill="both", expand=True)

        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)

    def _on_change(self, event):
        self.linenumbers.redraw()


# 功能函数字符串算MD5值
def str2md5(textlist):
    src = textlist[0].get(1.0, tk.END).strip().replace("\n", "").encode()
    # print("src =",src)
    if src:
        try:
            my_md5 = hashlib.md5()
            my_md5.update(src)
            my_md5_digest = my_md5.hexdigest()
            # print(my_md5_digest)
            # 输出到界面
            textlist[1].delete(1.0, tk.END)
            textlist[1].insert(1.0, my_md5_digest)
        except Exception as e:
            textlist[1].delete(1.0, tk.END)
            textlist[1].insert(1.0, "字符串转MD5失败")
    else:
        textlist[1].insert("ERROR:str_trans_to_md5 failed")


# 功能函数字符串算BASE64编码
def str2base64(textlist):
    src = textlist[0].get(1.0, tk.END).strip().replace("\n", "").encode()
    # print("src =",src)
    if src:
        try:
            mybase64_digest = base64.b64encode(src)
            # print(my_md5_digest)
            # 输出到界面
            textlist[1].delete(1.0, tk.END)
            textlist[1].insert(1.0, mybase64_digest)
        except Exception as e:
            textlist[1].delete(1.0, tk.END)
            textlist[1].insert(1.0, "字符串转base64失败")
    else:
        textlist[1].insert("ERROR:str_trans_to_base64 failed")


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
        self.log_data_Text.insert(END, logmsg_in)
        LOG_LINE_NUM = LOG_LINE_NUM + 1
    else:
        self.log_data_Text.delete(1.0, 2.0)
        self.log_data_Text.insert(END, logmsg_in)


if __name__ == '__main__':
    root = tk.Tk()  # “画板”----根窗口
    root.title("文本处理工具_v1.3")  # 在这里修改窗口的标题
    # 设置数据
    var_list = []
    for i in range(0, 3):
        var_list.append(tk.StringVar())

    # 设置窗口
    frame1 = tk.Frame(root)
    frame2 = tk.Frame(root)
    frame3 = tk.Frame(frame1)
    frame4 = tk.Frame(frame1)
    frame5 = tk.Frame(frame1)

    # 标签
    encoded_data_label = tk.Label(frame3, text="编码数据")
    function_label = tk.Label(frame4, text="方法")
    decoded_data_label = tk.Label(frame5, text="明文数据")

    # 文本框
    textlist = []
    encoded_data_text = TextWithLineNum(
        frame3, relief="groove", borderwidth=3)  # 编码数据录入框
    decoded_data_text = TextWithLineNum(
        frame5, relief="groove", borderwidth=3)  # 解码数据录入框
    log_data_Text = TextWithLineNum(
        frame2, relief="groove", borderwidth=3)  # 日志框
    textlist.append(encoded_data_text.text)
    textlist.append(decoded_data_text.text)
    textlist.append(log_data_Text.text)

    # 按钮
    str2md5_button = tk.Button(
        frame4, text="字符串转MD5--->", bg="lightblue", command=lambda: str2md5(textlist))  # 调用方法  加()为直接调用

    str2base64_button = tk.Button(
        frame4, text="字符串转BASE64--->", bg="lightblue", command=lambda: str2base64(textlist))  # 调用方法  加()为直接调用

    str2upper_button = tk.Button(
        frame4, text="字符串转大写--->", bg="lightblue")  # 调用内部方法  加()为直接调用
    str2lower_button = tk.Button(
        frame4, text="字符串转小写--->", bg="lightblue")  # 调用内部方法  加()为直接调用

    # 布局
    frame1.pack()
    frame2.pack(expand=1, fill="x")
    log_data_Text.pack(expand=1, fill="x")
    frame3.pack(side=tk.LEFT, expand=1, fill="y")
    encoded_data_label.pack()
    encoded_data_text.pack(expand=1, fill="y")
    frame4.pack(side=tk.LEFT)
    function_label.pack()
    str2md5_button.pack()
    str2base64_button.pack()
    str2upper_button.pack()
    str2lower_button.pack()
    frame5.pack(side=tk.LEFT, expand=1, fill="y")
    decoded_data_label.pack()
    decoded_data_text.pack(expand=1, fill="y")

    # 开始循环
    root.mainloop()
