#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#num1 = input('input first number:')
#num2 = input('input second number:')
#print(num1,'*',num2,'=',int(num1)*int(num2))


num = input('input your num:')

if(num.isdigit()):

	num = int(num)
	if num > 5:
	   print(num-5)
	   print(num-6)
	   print(num-7)
	else:
	   print(5-num)
else:
	print('num is string,{0}'.format(num))
	print('num is string,%s' % num)
	
num = ord('吴')
print(num)

name = chr(21556)
print(name)

name = 'minard'
age = 26
print('hello,everyone,my name is %s,age is %04x' % (name,age))

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])






