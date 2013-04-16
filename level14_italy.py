#!/usr/bin/python
import Image
import urllib2
import StringIO

def visit_authorized_url(url,name,passwd):
	"""return the content a webpage which need to be authorized to visit"""
	password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
	password_mgr.add_password(None,url,name,passwd)
	handler = urllib2.HTTPBasicAuthHandler(password_mgr)
	opener = urllib2.build_opener(handler)
	urllib2.install_opener(opener)
	return urllib2.urlopen(urllib2.Request(url)).read()

def walkaround(level,length,p,pixarr):
	cur=0
	for i in range(level-1,level+length-1):
		p[level-1,i]=pixarr[cur]
		cur += 1
	for i in range(level,level+length-1):
		p[i,level+length-2]=pixarr[cur]
		cur += 1
	for i in range(level+length-3,level-2,-1):
		p[level+length-2,i]=pixarr[cur]
		cur += 1
	for i in range(level+length-4,level-2,-1):
		p[i,level-1]=pixarr[cur]
		cur += 1



picstr = visit_authorized_url('http://www.pythonchallenge.com/pc/return/wire.png','huge','file')
img = Image.open(StringIO.StringIO(picstr))

final_img = Image.new("RGB",(100,100))
p=final_img.load()

pixlist=[]
for i in range(img.size[0]):
	pixlist.append(img.getpixel((i,0)))

length = [x*2*4-4 for x in range(50,0,-1)]
pos=[0]+length
for i in range(1,len(pos)):
	pos[i]=pos[i-1]+pos[i]

for i in range(1,51):
	walkaround(i,100-(i-1)*2,p,pixlist[pos[i-1]:pos[i]])
final_img.show()
