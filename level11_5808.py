#!/usr/bin/python
import Image,ImageDraw
import urllib2
import StringIO
import sys

def visit_authorized_url(url,name,passwd):
	"""return the content a webpage which need to be authorized to visit"""
	password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
	password_mgr.add_password(None,url,name,passwd)
	handler = urllib2.HTTPBasicAuthHandler(password_mgr)
	opener = urllib2.build_opener(handler)
	urllib2.install_opener(opener)
	return urllib2.urlopen(urllib2.Request(url)).read()

picstr = visit_authorized_url('http://www.pythonchallenge.com/pc/return/cave.jpg','huge','file')
img = Image.open(StringIO.StringIO(picstr))
p=img.load()

for i in range(0,img.size[0]):
	for j in range(0,img.size[1]):
		if (i&1)^(j&1) == 1:
			p[i,j]=(0,0,0)

img.show()
