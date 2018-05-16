#导入tkinter
from tkinter import *
#定义的方法 监听键盘事件
# def printkey(event):
#     print('你按下了: ' + event.char)
def move(event):
    global x,y
    if(event.char == 'd' or event.char=='D'):
        x += 1
        cube(x,y)
    elif(event.char=='w' or event.char=='W'):
        y -= 1
        cube(x, y)
    elif (event.char == 'a' or event.char == 'A'):
        x -= 1
        cube(x, y)
    elif (event.char == 's' or event.char == 'S'):
        y += 1
        cube(x, y)
def cube(x,y):
    ca.create_rectangle(128+x,89+y,138+x,99+y, fill='red')
#实例化tk
root = Tk()
#给输入框绑定按键监听事件<Key>为监听任何按键 <Key-x>监听其它键盘，如大写的A<Key-A>、回车<Key-Return>
root.attributes("-alpha", 1)#窗口透明度100%
x,y=0,0
ca = Canvas(root,bg='black')
ca.create_rectangle(128,89,138,99, fill='red')
root.bind('<Key>',move)
ca.pack()
root.mainloop()
