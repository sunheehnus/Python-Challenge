#!/usr/bin/python
import urllib2
import re
import sys
def buildContent():
	html = urllib2.urlopen(urllib2.Request("http://www.pythonchallenge.com/pc/def/equality.html")).read()
	contents = html.split("\n")
	startpos=0
	while not contents[startpos].startswith("<!--"):
		startpos += 1
	startpos += 1
	endpos = -1
	while not contents[endpos].startswith("-->"):
		endpos -= 1
	return "".join(contents[startpos:endpos])
def findTarget():
	return [x for x in re.findall('[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]',buildContent())] 
#return [x for x in re.findall('[A-Z]{3,}[a-z][A-Z]{3,}',buildContent()) if len(x)==7]
for i in findTarget():
	sys.stdout.write(i[4])
print
