#!/usr/bin/python  
# -*- coding: utf-8 -*- 

###
#Loop Training 1
###
num = input('input number:')
if(num.isdigit()):
	num = int(num)
	
###
#Loop Training 2
###	
sum = 0	
for x in range(num):
	sum = sum + x
	if x%4 == 0:
		print('Sum:%02d,X:%02d' % (sum,x))
		
###
#Loop Training 3
###
total = 0
while (num > 0):
	if(num%2 == 0):
		total += num
		print('total:%03d,num:%03d' % (total,num))
	num -= 1

###
#Loop Training 4
###
K = 1
Array = [1,1]
while K < 20:
	Array.append((Array[K]+Array[K-1]))
	K += 1
	
	if(Array[K] > 2000):
		Array.pop(K)
		break;
	
print(Array)
	
###
#Loop Training 5
###
n = -1
Name = ('minard',123,'Mcdull',456,True,'WuShiwan')
for x in Name:

	n += 1
	#if(isinstance(Name[n], str) ):
	if(type(Name[n]) != str):
		continue

	print('Name[%d]:%s' % (n+1,Name[n]))
	
	
###
#Loop Training 6
###
'''
num = 0
while(1):
	num += 1
	print(num)
'''
