#coding=utf-8
import urllib2
import urllib
import get_html
import re_test

url = 'http://tieba.baidu.com/f'

values = {'kw':'saber'}
page = get_html.gethtml(url,values)#获得页面html源代码
#print type(page)
numOfPost = re_test.getpostnum(page)#按照正则表达式提取
print 'number of post = ', numOfPost
repNum = re_test.getrepnum(page)
print repNum
repNum = [int(x) for x in repNum]
print repNum
titleList = re_test.gettitle(page)
print len(titleList)
topList = {}

if len(titleList)==len(repNum):
	for i in range(0,len(repNum)):
		topList[repNum[i]]=titleList[i]

# for reply, title in topList.items():
# 	print "%d : %s" % (reply,title)

sortedtopList = sorted(topList.iteritems(),key=lambda sortedtopList:sortedtopList[0],reverse=True)
f = file("topList.txt",'w+')
for i in range(0,len(sortedtopList)):
	print "%d : %s" % (sortedtopList[i][0],sortedtopList[i][1])
	f.write("%d : %s\n" % (sortedtopList[i][0],sortedtopList[i][1]))
