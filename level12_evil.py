#!/usr/bin/python
import urllib2
def visit_authorized_url(url,name,passwd):
	"""return the content a webpage which need to be authorized to visit"""
	password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
	password_mgr.add_password(None,url,name,passwd)
	handler = urllib2.HTTPBasicAuthHandler(password_mgr)
	opener = urllib2.build_opener(handler)
	urllib2.install_opener(opener)
	return urllib2.urlopen(urllib2.Request(url)).read()

content = visit_authorized_url('http://www.pythonchallenge.com/pc/return/evil2.gfx','huge','file')
for i in range(5):
	pic=content[i::5]
	f = open("%s%d"%("pic",i),"wb")
	f.write(pic)
	f.close()
print "Find the saved pics in the folder your python code is in."
