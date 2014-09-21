import urllib
import urllib2

def gethtml(url,values):
	data = urllib.urlencode(values)
	print data
	full_url = url +'?' + data
	req = urllib2.Request(full_url, data)
	response = urllib2.urlopen(req)
	print response.geturl()
	the_page = response.read()
	f = file('newpage.html','w')
	f.write(the_page)
	f.close()
	#unicodePage = the_page.decode("gbk")
	return the_page