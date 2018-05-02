'''
height1 = input('input your height:')
weight1 = input('input your weight:')

height = int(height1)
weight = int(weight1)
	
BMI = weight / (height*height)

print('BMI指数:%0.1f ' % BMI)
if(BMI < 18.5):
	print('过轻')
elif( (BMI >= 18.5) and (BMI <25)):
	print('正常')
elif( (BMI >= 25) and (BMI <28)):
	print('过重')
elif( (BMI >= 28) and (BMI <32)):
	print('肥胖')
else:
	print('严重肥胖')
	
'''

print(list(range(1,100,2)))

for x in range(1,10):
	for y in range(1,10):
		if(y <= x):
			print('%d*%d=%02d ' % (x,y,x*y),end='')
		if(x == y):
			print('')