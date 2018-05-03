
import time
import pyperclip

#获取当前的分钟
#minute = int(time.strftime('%M',time.localtime(time.time())))

while( int(time.strftime('%M',time.localtime(time.time()))) % 2 == 0):
	file = open('pasteLog.log','a')
	file.write(pyperclip.paste()+'\n')
	