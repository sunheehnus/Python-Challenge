#!/usr/bin/python
import Image,ImageDraw
import urllib2
import StringIO
import re

def visit_authorized_url(url,name,passwd):
	"""return the content a webpage which need to be authorized to visit"""
	password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
	password_mgr.add_password(None,url,name,passwd)
	handler = urllib2.HTTPBasicAuthHandler(password_mgr)
	opener = urllib2.build_opener(handler)
	urllib2.install_opener(opener)
	return urllib2.urlopen(urllib2.Request(url)).read()

html = visit_authorized_url('http://www.pythonchallenge.com/pc/return/good.html','huge','file')
picstr = visit_authorized_url('http://www.pythonchallenge.com/pc/return/good.jpg','huge','file')

first,second=map(eval,re.search(r'first:(.*)second:(.*)-->',html.replace('\n',' ')).groups())

img = Image.open(StringIO.StringIO(picstr))
draw = ImageDraw.Draw(img)

p1=(first[0],first[1])
for i in range(1,len(first)/2):
    p2=(first[2*i],first[2*i+1])
    draw.line((p1,p2),fill=255)
    p1=p2

p1=(second[0],second[1])
for i in range(1,len(second)/2):
    p2=(second[2*i],second[2*i+1])
    draw.line((p1,p2),fill=255)
    p1=p2
img.show()
