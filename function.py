#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def Func(a,b,x):
	if(x == 1):
		print('{0}+{1}={2}'.format(a,b,a+b))
	elif(x == 2):
		print('{0}/{1}={2}'.format(a,b,a/b))
	elif(x == 3):
		print('{0}*{1}={2}'.format(a,b,a*b))
	elif(x == 4):
		print('{0}-{1}={2}'.format(a,b,a-b))
	else:
		print('Input Invaild,No Output!')
		
	return a&b,a|b
	
def Result(a,b,c):#ax²+bx+c = 0
	first1 = abs(-b) + math.sqrt(b*b - 4*a*c)
	first2 = abs(-b) - math.sqrt(b*b - 4*a*c)
	
	second = 2*a;
	
	return first1/second,first2/second
		
while(1):
	num1 = input('input first num:')
	num2 = input('input seocnd num:')
	deal = input('input oprator:')
	
	if(int(deal) == 0):
		break;
	
	S = Func(int(num1),int(num2),int(deal))
	
	print('Return Vlaue:{0},{1}'.format(S[0],S[1]))
	
	print(Result(int(num1),int(num2),int(deal)))
	