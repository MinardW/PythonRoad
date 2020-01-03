import random as rd

RedBoal = []
BlueBoal = []
BlueFirst = 0

def GetRedBoal():
	for i in range(6):
		if(len(RedBoal) == 0):
			RedBoal.insert(len(RedBoal),rd.randint(1,33))
		else:
			isFlag = True
			while True:
				temp = rd.randint(1,33)
				#print(AllBoal)
				if temp in RedBoal:
					continue
				else:
					RedBoal.insert(len(RedBoal),temp)
					break
					
	RedBoal.sort()
	print('红:',RedBoal)
						
def GetBlueBoal():

	global BlueFirst

	BlueFirst = rd.randint(1,16)
	BlueBoal.insert(len(BlueBoal),BlueFirst)
	while True:
		temp = rd.randint(1,16)
		#print(blueBoal,temp)
		if temp in BlueBoal:
			if temp != 9:
				#BlueBoal.insert(len(AllBoal),temp)
				print('蓝: [',BlueFirst,'|',temp,']')
				break
		else:
			BlueBoal.insert(len(BlueBoal),temp)
	
GetRedBoal()
GetBlueBoal()

#print('比较器:https://www.78500.cn/tool/ssqdb.html')