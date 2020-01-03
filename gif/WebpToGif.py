#coding:gbk
import os,sys
from PIL import Image

im = Image.open(sys.argv[1])
im.save('New.gif', 'gif', save_all=True)
