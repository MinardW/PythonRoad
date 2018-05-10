#!python3

import sys,pyperclip


print(len(sys.argv))
l = sys.argv
print(l)

'''
n = 0
for x in sys.argv:
	print(sys.argv[n])
	n += 1


Content = pyperclip.paste()
Text = Content.split('\n')

for n in range(len(Text)):
	Text[n] = '* '+Text[n]

#Text = '\n'.join(Text)	
	
pyperclip.copy(str(Text))
'''