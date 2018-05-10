import os

path = 'C:\\DriveKey\\EULA.doc'
#P143
#列出一个文件的根目录下所有文件,并得到文件容量
for p in os.listdir(os.path.dirname(path)):
	print(os.path.join(os.path.dirname(path),p),end="")
	print( (' Size:%d byte' % os.path.getsize(os.path.join(os.path.dirname(path),p))).center(30))
	