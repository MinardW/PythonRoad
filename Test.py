import random
 
L = [] 
n = 1000
while(n > 0):
	n -= 1
	L.append(random.randint(0,2))

N = [0,0,0]
for x in L:
	if(x == 0):
		N[0] += 1
	elif(x == 1):
		N[1] += 1
	else:
		N[2] += 1
	
print(N)