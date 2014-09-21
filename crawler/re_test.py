#coding=utf-8
import re

def getpostnum(line):

	matchObj = re.search( r'<span class="j_post_num post_num">(.*?)</span>', line, re.M|re.I)

	if matchObj:
	   print "matchObj.group() : ", matchObj.group()
	   return matchObj.group(1)
	else:
	   return "No match!!"

def getrepnum(line):
	matchRep = re.findall(r'<div class="threadlist_rep_num" title="\xbb\xd8\xb8\xb4">(.*?)</div>', line, re.M|re.I)
	if matchRep:
		print "number of results : " ,len(matchRep)
		return matchRep
	else:
		return "No match!"

def gettitle(line):
	line.decode('gbk')
	matchTitle = re.findall(r'<a href=".*?" title=".*?" target="_blank" class="j_th_tit">(.*?)</a>', line, re.M|re.I)
	if matchTitle:
		print type(matchTitle)
		return matchTitle
	else:
		print "No match!!"