# -*- coding:utf-8 -*-
from tkinter import *
 
class radiobutton:
    def __init__(self):
        root = Tk()
        root.title("单选框")  # 设置窗口标题
        root.geometry("650x600")  # 设置窗口大小 注意：是x 不是*
        '''单选框样式'''
        # 指定Radiobutton的事件处理函数
        iv_command = IntVar()
        self.rb_function_Label = Label(root, text='关联函数：')
        self.rb_function = Radiobutton(root, text='执行函数', command=self.function1, variable=iv_command)
        # 单选框默认选择
        iv_default = IntVar()
        self.rb_default_Label = Label(root, text='默认选择：')
        self.rb_default1 = Radiobutton(root, text='单选框1', value=1, variable=iv_default)
        self.rb_default2 = Radiobutton(root, text='单选框2', value=2, variable=iv_default)
        iv_default.set(1)
        # 单选框样式
        iv_style = IntVar()
        self.rb_style_Label = Label(root, text='显示边框样式：')
        self.rb_style1 = Radiobutton(root, text='边框平坦', value=1, variable=iv_style, relief=FLAT)
        self.rb_style2 = Radiobutton(root, text='边框凹陷', value=2, variable=iv_style, relief=SUNKEN)
        self.rb_style3 = Radiobutton(root, text='边框凸起', value=3, variable=iv_style, relief=RAISED)
        self.rb_style4 = Radiobutton(root, text='边框压线', value=4, variable=iv_style, relief=GROOVE)
        self.rb_style5 = Radiobutton(root, text='边框脊线', value=5, variable=iv_style, relief=RIDGE)
        # 单选框高度，height='高度'，wideth='宽度'，单选框的高度和宽度必须和边框样式一起使用才有效果
        iv_xy = IntVar()
        self.rb_xy_Label = Label(root, text='单选框边框xy：')
        self.rb_height = Radiobutton(root, text='边框高度', value=1, variable=iv_xy, relief=RAISED, height=2)
        self.rb_wideth = Radiobutton(root, text='边框高度', value=2, variable=iv_xy, relief=RAISED, width=16)
        # 单选框边框大小，bd='边框大小'，单选框的边框效果必须和边框样式一起使用才有效果
        iv_border = IntVar()
        self.rb_border_Label = Label(root, text='单选框边框大小：')
        self.rb_border = Radiobutton(root, text='边框大小', variable=iv_border, relief=RAISED, bd=5)
        # 鼠标点击到单选框后改变颜色，activebackground='背景色'，activeforeground='前景色'
        iv_click_colour = IntVar()
        self.rb_click_colour_Label = Label(root, text='鼠标点击颜色：')
        self.rb_click_colour1 = Radiobutton(root, text='前景色', value=1, variable=iv_click_colour,
                                            activebackground='blue')
        self.rb_click_colour2 = Radiobutton(root, text='背景色', value=2, variable=iv_click_colour,
                                            activeforeground='blue')
 
        # 单选框颜色，bg='背景色', fg='前景色'
        iv_colour = IntVar()
        self.rb_colour_Label = Label(root, text='单选框颜色：')
        self.rb_colour1 = Radiobutton(root, text='前景色', value=1, variable=iv_colour, bg='blue')
        self.rb_colour2 = Radiobutton(root, text='背景色', value=2, variable=iv_colour, fg='blue')
        # 单选框文字字体格式， font=('字体', 字号, 'bold/italic/underline/overstrike')
        iv_font = IntVar()
        self.rb_font_Label = Label(root, text='显示边框样式：')
        self.rb_font1 = Radiobutton(root, text='软体雅黑/12/重打印', value=1, variable=iv_font,
                                    font=('软体雅黑', 10, 'overstrike'))
        self.rb_font2 = Radiobutton(root, text='宋体/12/斜体', value=2, variable=iv_font, font=('宋体', 10, 'italic'))
        self.rb_font3 = Radiobutton(root, text='黑体/12/加粗', value=3, variable=iv_font, font=('黑体', 10, 'bold'))
        self.rb_font4 = Radiobutton(root, text='楷体/12/下划线', value=4, variable=iv_font,
                                    font=('楷体', 10, 'underline'))
 
        # 单选框图片设置，image=图片变量。图片必须以变量的形式赋值给image，图片必须是gif格式。
        iv_image = IntVar()
        self.rb_image_Label = Label(root, text='单选框图片：')
        gif = PhotoImage(file="1.gif")
        self.rb_image = Radiobutton(root, variable=iv_image, image=gif)
        # 单选框文字对齐方式，可选项包括LEFT, RIGHT, CENTER
        iv_aligning = IntVar()
        self.rb_aligning_Label = Label(root, text='文字对齐方式：')
        self.rb_aligning1 = Radiobutton(root, text='左对齐\n文字左侧对齐', value=1, variable=iv_aligning, justify=LEFT)
        self.rb_aligning2 = Radiobutton(root, text='居中对齐\n文字居中对齐', value=2, variable=iv_aligning, justify=CENTER)
        self.rb_aligning3 = Radiobutton(root, text='右对齐\n文字右侧对齐', value=3, variable=iv_aligning, justify=RIGHT)
        # 单选框达到限制字符后换行显示
        iv_linefeed = IntVar()
        self.rb_linefeed_Label = Label(root, text='文字换行显示：')
        self.rb_linefeed = Radiobutton(root, text='1234567890', variable=iv_linefeed, wraplength=30)
        # 下划线。取值就是带下划线的字符串索引，为 0 时，第一个字符带下划线，为 1 时，第两个字符带下划线，以此类推
        iv_underline = IntVar()
        self.rb_underline_Label = Label(root, text='文字标下划线：')
        self.rb_underline = Radiobutton(root, text='12345', variable=iv_underline, underline=2)
        # 单选框状态
        iv_status = IntVar()
        self.rb_status_Label = Label(root, text='按钮状态：')
        self.rb_disabled = Radiobutton(root, text='禁用状态', value=1, variable=iv_status)
        self.rb_disabled.config(state=DISABLED)
        self.rb_usual = Radiobutton(root, text='普通状态', value=2, variable=iv_status)
        self.rb_usual.config(state=NORMAL)
        self.rb_active = Radiobutton(root, text='活跃状态', value=3, variable=iv_status)
        self.rb_active.config(state=ACTIVE)
 
        '''grid布局'''
        self.rb_function_Label.grid(row=1, column=0, sticky='E')
        self.rb_function.grid(row=1, column=1, sticky='W')
        self.rb_default_Label.grid(row=2, column=0, sticky='E')
        self.rb_default1.grid(row=2, column=1, sticky='W')
        self.rb_default2.grid(row=2, column=2, sticky='W')
        self.rb_style1.grid(row=2, column=3, sticky='W')
        self.rb_style_Label.grid(row=3, column=0, sticky='E')
        self.rb_style1.grid(row=3, column=1, sticky='W')
        self.rb_style2.grid(row=3, column=2, sticky='W')
        self.rb_style3.grid(row=3, column=3, sticky='W')
        self.rb_style4.grid(row=3, column=4, sticky='W')
        self.rb_style5.grid(row=3, column=5, sticky='W')
        self.rb_xy_Label.grid(row=4, column=0, sticky='E')
        self.rb_height.grid(row=4, column=1, sticky='W')
        self.rb_wideth.grid(row=4, column=2, columnspan=2, sticky='W')
        self.rb_border_Label.grid(row=5, column=0, sticky='E')
        self.rb_border.grid(row=5, column=1, sticky='W')
        self.rb_click_colour_Label.grid(row=6, column=0, sticky='E')
        self.rb_click_colour1.grid(row=6, column=1, sticky='W')
        self.rb_click_colour2.grid(row=6, column=2, sticky='W')
        self.rb_colour_Label.grid(row=7, column=0, sticky='E')
        self.rb_colour1.grid(row=7, column=1, sticky='W')
        self.rb_colour2.grid(row=7, column=2, sticky='W')
        self.rb_font_Label.grid(row=8, column=0, rowspan=2, sticky='E')
        self.rb_font1.grid(row=8, column=1, columnspan=2, sticky='W')
        self.rb_font2.grid(row=8, column=3, columnspan=2, sticky='W')
        self.rb_font3.grid(row=9, column=1, columnspan=2, sticky='W')
        self.rb_font4.grid(row=9, column=3, columnspan=2, sticky='W')
        self.rb_image_Label.grid(row=10, column=0, sticky='E')
        self.rb_image.grid(row=10, column=1, columnspan=3, sticky='W')
        self.rb_aligning_Label.grid(row=11, column=0, sticky='E')
        self.rb_aligning1.grid(row=11, column=1, sticky='W')
        self.rb_aligning2.grid(row=11, column=2, sticky='W')
        self.rb_aligning3.grid(row=11, column=3, sticky='W')
        self.rb_linefeed_Label.grid(row=12, column=0, sticky='E')
        self.rb_linefeed.grid(row=12, column=1, sticky='W')
        self.rb_underline_Label.grid(row=13, column=0, sticky='E')
        self.rb_underline.grid(row=13, column=1, sticky='W')
        self.rb_status_Label.grid(row=14, column=0, sticky='E')
        self.rb_disabled.grid(row=14, column=1, sticky='W')
        self.rb_usual.grid(row=14, column=2, sticky='W')
        self.rb_active.grid(row=14, column=3, sticky='W')
        root.mainloop()
 
    def function1(self):
        print('选中function1')
 
 
if __name__ == '__main__':
    radiobutton()
