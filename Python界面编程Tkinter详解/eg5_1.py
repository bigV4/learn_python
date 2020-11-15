#https://www.bookstack.cn/books/sjtu-cs902-courseware
import tkinter as tk

def canvasFunc(event):
    if c.itemcget(t,"text") == "Hello!": 
        c.itemconfig(t,text="Goodbye!")
    else:
        c.itemconfig(t,text="Hello!")
def textFunc(event):
    if c.itemcget(t,"fill") != "white": 
        c.itemconfig(t,fill="white")
    else:
        c.itemconfig(t,fill="black")
root = tk.Tk()
c = tk.Canvas(root,width=300,height=200,bg='white') 
c.pack()
t = c.create_text(150,100,text="Hello!") 
c.bind("<Button-1>",canvasFunc) #利用画布的 bind()方法将画布对象 c 与鼠标左键点击事件”“进行了绑定
c.tag_bind(t,"<Button-3>",textFunc) #利用画布的 tag_bind()方法将画布对象 c 上的图形项（文本）t 与鼠标右键点击事件”“进行了绑定
root.mainloop()