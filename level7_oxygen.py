#!/usr/bin/python
import Image
import sys
import urllib2
import StringIO
im = Image.open(StringIO.StringIO(urllib2.urlopen(urllib2.Request("http://www.pythonchallenge.com/pc/def/oxygen.png")).read()))
graypixcnts = []
for y in range(0,im.size[1]):
	cnt=0
	for x in range(0,im.size[0]):
		pixel = im.getpixel((x,y))
		if pixel[0] == pixel[1] == pixel[2]:
			cnt += 1
	graypixcnts.append(cnt)
graypixcnt = max(graypixcnts)
for y in range(0,im.size[1]):
	if graypixcnts[y] != graypixcnt:
		continue
	for x in range(0,im.size[0]):
		pixel = im.getpixel((x,y))
		if pixel[0] == pixel[1] == pixel[2]:
			sys.stdout.write(chr(pixel[0]))
	print
print 
print
print
for ASCII in [105,110,116,101,103,114,105,116,121]:
	sys.stdout.write(chr(ASCII))
print
