#!/usr/bin/python
import urllib2
import cPickle
import sys
f=urllib2.urlopen(urllib2.Request("http://www.pythonchallenge.com/pc/def/banner.p"))
for eacharr in  cPickle.load(f):
	for eachitem in eacharr:
		sys.stdout.write(eachitem[0]*eachitem[1])
	print
