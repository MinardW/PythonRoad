import os
import sys

#输入一个文件的具体路径
#输入一个需要查找该根目录下的文件类型(.txt/.py/....)

def help():
	print('Function Dec:Find the file of the specified type.')
	print('*1.Input the absolute path of a file.')
	print('*2.Input the file type to be searched for.\n')
	print('Remark:If you not input second para,default get file type of first para.')

#path = 'C:\\DriveKey\\EULA.doc'
#P143
#列出一个文件的根目录下所有文件,并得到文件容量
if(len(sys.argv) < 2):
	print("invaild input.")
	help()
	sys.exit()
	
for p in os.listdir(os.path.dirname(sys.argv[1])):
	fileType = ''

	if(len(sys.argv) == 2):
		fileType = '.'+os.path.basename(sys.argv[1]).split('.')[1]
	else:
		fileType = sys.argv[2]
		
	if(fileType in p):
		filePath = os.path.join(os.path.dirname(sys.argv[1]),p)
		print(filePath)
	
	#print(os.path.join(os.path.dirname(path),p),end="")
	#print( (' Size:%d byte' % os.path.getsize(os.path.join(os.path.dirname(path),p))).center(30))
	
	
	
	