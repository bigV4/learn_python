#https://www.bookstack.cn/read/sjtu-cs902-courseware/08994ae313e28ddb.md
from sys import version_info
if version_info.major == 2:
    from Tkinter import *
else:
    from tkinter import *

'''
算法： 
创建窗口和画布；
在画布上绘制太阳、地球和月球，以及地球的绕日椭圆轨道； 
设置地球和月球的当前位置；
进入动画循环： 
    旋转 0.01p；
    计算地球和月球的新位置； 
    移动地球和月球到新位置 
    更新地球和月球的当前位置； 
    停顿一会
'''

from math import sin,cos,pi 
from time import sleep
def main():
    root = Tk()
    c = Canvas(root,width=300,height=200,bg='white') 
    c.pack()
    orbit = c.create_oval(50,50,250,150)
    sun = c.create_oval(110,85,140,115,fill='red') 
    earth = c.create_oval(245,95,255,105,fill='blue') 
    moon = c.create_oval(265,98,270,103)
    eX = 250 # earth's X
    eY = 100 # earth's Y
    m2eX = 20 # moon's X relative to earth 
    m2eY = 0 # moon's Y relative to earth 
    t = 0
    while True:
        t = t + 0.01*pi
        new_eX = 150 + 100 * cos(t) 
        new_eY = 100 - 50 * sin(t) 
        new_m2eX = 20 * cos(12*t) 
        new_m2eY = -15 * sin(12*t)
        edx = new_eX - eX 
        edy = new_eY - eY
        mdx = new_m2eX - m2eX 
        mdy = new_m2eY - m2eY
        c.move(earth,edx,edy) 
        c.move(moon,mdx+edx,mdy+edy) 
        c.update()
        eX = new_eX 
        eY = new_eY
        m2eX = new_m2eX 
        m2eY = new_m2eY
        sleep(0.04)
main()