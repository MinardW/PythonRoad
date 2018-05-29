import logging
logging.basicConfig(filename = 'Log.txt',level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.DEBUG)

def calNum(Num):

	logging.debug('Num = '+str(Num))
	
	if(Num == 1):
		return 1;
	else:
		return Num * calNum(Num - 1)

while(1):	
	try:
		N = int(input('input a number:'))
	except:
		print('Input Invalid.')
		continue
	
		logging.DEBUG('Input num is '+str(N))
		
	if(N == 0):
		logging.debug('Exit Flag.')
		break;
	else:
		print('Result = '+str(calNum(N)))
		
	