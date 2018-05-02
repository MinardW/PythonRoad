#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def trim(String):
	if(String[:1] == ' '):
		return trim(String[1:])
	if(String[-1:] == ' '):
		return trim(String[0:-1])
		
	return String
	
name = "   Wu Shi Wan   "	
Test = "13"
#print(TrimFun(name),Test)

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')