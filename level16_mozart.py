#!/usr/bin/python
import Image  
import StringIO
import urllib2
def visit_authorized_url(url,name,passwd):
	"""return the content a webpage which need to be authorized to visit"""
	password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
	password_mgr.add_password(None,url,name,passwd)
	handler = urllib2.HTTPBasicAuthHandler(password_mgr)
	opener = urllib2.build_opener(handler)
	urllib2.install_opener(opener)
	return urllib2.urlopen(urllib2.Request(url)).read()

picstr = visit_authorized_url('http://www.pythonchallenge.com/pc/return/mozart.gif','huge','file')	
img = Image.open(StringIO.StringIO(picstr))  
for h in range(0,img.size[1]):  
	line = [img.getpixel((w,h)) for w in range(img.size[0])]  
	pos = line.index(195)
	line = line[pos:]+line[:pos]
	for w in range(img.size[0]):
		img.putpixel((w,h),line[i])
img.show()
