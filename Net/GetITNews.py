#!Python 3.0
# -- code UTF-8 --
import bs4
import webbrowser as web
import os
import sys
import requests as res
import re
import logging as log
log.basicConfig(level=log.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')
#log.disable(logging.DEBUG)

ITLink = 'https://news.cnblogs.com'
COUNT_MAX = 3

def ReContent(text):
	regex = re.compile('(\d){6}')
	match = regex.search(text)
	
	log.debug('file title:'+match.group())
	return match.group()

def SearchResult(Num):
		r = res.get(str(ITLink))
		r.raise_for_status()
		soup = bs4.BeautifulSoup(r.text,"html.parser")
		
		#寻找所有具有CSS类t的元素中的<a>元素
		link = soup.select('.news_entry a')
		#link = soup.select('h3[class="t"]')
		if(len(link) > Num):
			return link[:Num]
			
		return link

num = COUNT_MAX
if(len(sys.argv) > 1):

	log.debug('para : '+sys.argv[1])

	if(sys.argv[1].isdecimal()):
		num = int(sys.argv[1])

Reslinks = SearchResult(num)
if(Reslinks == None):
	print('No Result')

if(False == os.path.exists(os.getcwd()+'\\ITNews')):
	log.debug('make new dir(ITNews)')
	os.mkdir('ITNews')
	
for link in Reslinks:
	log.debug('href : '+link.get('href'))
	filename = ReContent(link.get('href'))
	if(os.path.exists(os.getcwd()+'\\ITNews\\'+filename+'.html')):
		log.debug('already exist '+filename+'.html')
		continue
	
	file = open('ITNews/'+filename+'.html','w',encoding='UTF-8')
	filecontent = res.get(ITLink+link.get('href'))
	file.write(filecontent.text)
	file.close()
	
	#web.open(ITLink+link.get('href'))
