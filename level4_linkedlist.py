#!/usr/bin/python
import urllib2
base="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nextnothing="12345"
for i in range(0,400):
	nextnothing = urllib2.urlopen(urllib2.Request(base+nextnothing)).read().split(" ")[-1]
	print nextnothing
