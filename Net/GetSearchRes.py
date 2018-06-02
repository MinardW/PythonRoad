#!Python 3.0
# -- code UTF-8 --
import bs4
import webbrowser as web
import os
import sys
import requests as res

SEARCH = 'http://www.baidu.com/s?wd='

def SearchResult(KeyWord):
		r = res.get(str(SEARCH)+KeyWord)
		r.raise_for_status()
		soup = bs4.BeautifulSoup(r.text,"html.parser")
		
		#寻找所有具有CSS类t的元素中的<a>元素
		link = soup.select('.t a')
		#link = soup.select('h3[class="t"]')
		if(len(link) > 3):
			return link[:3]
			
		return link
	
if(len(sys.argv) < 2):
	print('Para is invalid!')
	sys.exit()
	
Reslinks = SearchResult(sys.argv[1])
if(Reslinks == None):
	print('No Result')

for link in Reslinks:
	print(link.get('href'))
	web.open(link.get('href'))
