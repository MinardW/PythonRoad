
Name = ('Minard','Mcdull','Wushiwan',123,'Wu')
grade = {'Minard':82,'Mcdull':95,'Wu':69}

for x in Name:
	if x in grade:
		print(x,grade.get(x))
		if(grade.get(x) < 80):
			grade.pop(x)
		
print('Len:{0},All Data:{1}'.format(len(grade),grade))