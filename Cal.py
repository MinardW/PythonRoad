#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
import tkinter as tk
import tkinter.messagebox

root=tk.Tk()
root.title('简易计算器')
root.geometry('300x400')
root.resizable(width=False, height=False) #宽不可变, 高可变,默认为True

frame_root = Frame(root)  
frame1 = Frame(frame_root)  
frame2 = Frame(frame_root) 

Content = Entry(frame1, bd=3, width=22, textvariable='请输入内容...')
Content.pack()
	
value1 = 0
value2 = 0	
	
def InputValue(Value):

	global value1
	global value2

	if Value == 99:
		Content.delete(0, END)
	elif Value == '+':
		value1 = Content.get()
		Content.delete(0, END)
	elif Value == '=':
		value2 = Content.get()
		#tk.messagebox.showwarning(title='Hi', message=value2)
		Content.delete(0, END)
		Content.insert(0,int(value1)+int(value2))
	else:
		Content.insert( len(Content.get()),Value)

Num1 = Button(frame2,text="1",command = lambda:InputValue(Value = 1),width=3,height=1)
Num1.grid(row=1,column=0,padx=10, pady=5)

Num2 = Button(frame2,text="2",command = lambda:InputValue(Value = 2),width=3,height=1)
Num2.grid(row=1,column=1,padx=10, pady=5)

Num3 = Button(frame2,text="3",command = lambda:InputValue(Value = 3),width=3,height=1)
Num3.grid(row=1,column=2,padx=10, pady=5)

Jia = Button(frame2,text="+",command = lambda:InputValue(Value = '+'),width=3,height=1)
Jia.grid(row=1,column=3,padx=10, pady=5)

Num4 = Button(frame2,text="4",command = lambda:InputValue(Value = 4),width=3,height=1)
Num4.grid(row=2,column=0,padx=10, pady=5)

Num5 = Button(frame2,text="5",command = lambda:InputValue(Value = 5),width=3,height=1)
Num5.grid(row=2,column=1,padx=10, pady=5)

Num6 = Button(frame2,text="6",command = lambda:InputValue(Value = 6),width=3,height=1)
Num6.grid(row=2,column=2,padx=10, pady=5)

Cha = Button(frame2,text="-",command = lambda:InputValue(Value = '-'),width=3,height=1)
Cha.grid(row=2,column=3,padx=10, pady=5)

Num7 = Button(frame2,text="7",command = lambda:InputValue(Value = 7),width=3,height=1)
Num7.grid(row=3,column=0,padx=10, pady=5)

Num8 = Button(frame2,text="8",command = lambda:InputValue(Value = 8),width=3,height=1)
Num8.grid(row=3,column=1,padx=10, pady=5)

Num9 = Button(frame2,text="9",command = lambda:InputValue(Value = 9),width=3,height=1)
Num9.grid(row=3,column=2,padx=10, pady=5)

Mul = Button(frame2,text="*",command = lambda:InputValue(Value = '*'),width=3,height=1)
Mul.grid(row=3,column=3,padx=10, pady=5)

Num0 = Button(frame2,text="0",command = lambda:InputValue(Value = 0),width=3,height=1)
Num0.grid(row=4,column=0,padx=10, pady=5)

Kong = Button(frame2,text="清空",command = lambda:InputValue(Value = 99),width=3,height=1)
Kong.grid(row=4,column=1,padx=10, pady=5)

Res = Button(frame2,text="=",command = lambda:InputValue(Value = '='),width=3,height=1)
Res.grid(row=4,column=2,padx=10, pady=5)

Did = Button(frame2,text="/",command = lambda:InputValue(Value = '/'),width=3,height=1)
Did.grid(row=4,column=3,padx=10, pady=5)

frame1.pack()
frame2.pack()
frame_root.pack()

root.mainloop();