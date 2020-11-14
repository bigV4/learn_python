import tkinter as tk #内置库
from PIL import Image,ImageTk #

def onclick():
    #一个回调函数
    print("我被电击了")
    print("onclick是一个",type(onclick))

root =tk.Tk() #“画板”----根窗口

#-组件“标签”Lable是一个标签组件。主要用来实现显示功能，可以显示文字和图片
#-- l = tkinter.Label(parent, option=value ....)参数说明
##--parent: 代表承载该按钮的父容器。
##--option: 可选项，即该按钮的可设置的属性。这些选项的可设置的属性。这些按钮可以用“键=值”的形式设置，并以逗号分隔
tk.Label(root, text="我是标签").pack()
tk.Label(root, bitmap="error").pack()

##Python内置了10中位图，可以直接使用，设置bitmap属性即可。
tk.Label(root, bitmap="gray75").pack()
tk.Label(root, bitmap="gray50").pack()
tk.Label(root, bitmap="gray25").pack()
tk.Label(root, bitmap="gray12").pack()
tk.Label(root, bitmap="hourglass").pack()
tk.Label(root, bitmap="info").pack()
tk.Label(root, bitmap="questhead").pack()
tk.Label(root, bitmap="question").pack()
tk.Label(root, bitmap="warning").pack()

##Python中image属性仅支持gif\pgm\ppm格式，bitmap支持xbm格式。
##image属性与bitmap属性只能设置一个，同时设置则image优先。
bmp = tk.BitmapImage(file="logo.xbm")
photo_gif = tk.PhotoImage(file="gifs-on-cli.gif")
#tk.Label(root, bitmap=bmp).pack()
tk.Label(root, image=photo_gif).pack()
'''
如需显示其他格式图片.则需要做一些特别处理,要用到Python的图像处理库一PIL库 ,但是PIL不支
持Python3 ,且该库过于陈旧,不建议使用,这里可以选择其替代方案, Pllow库函数使用方法与PIL
相同。首先去网上下载并安装Pillow库
'''
image = Image.open('001.jpeg')
photo = ImageTk.PhotoImage(image)
tk.Label(root, image=photo).pack()

root.mainloop() # GUI程序一定要有个主循环