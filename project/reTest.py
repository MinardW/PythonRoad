#!python
import re

file = open('test.html','r')
fileContent = file.read()

photoRe = re.compile(r'https://.*.png')
#photoRe = re.compile(r'title-(\w)*')
photoUrl = photoRe.search(fileContent)
print(photoUrl.group())

pl = re.findall(r'https://.*.png',fileContent)

for n in range(len(pl)):
	print(pl[n])

