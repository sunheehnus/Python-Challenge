#!/usr/bin/python
import zipfile
import sys
import re
nextfile = "90052"
z=zipfile.ZipFile("channel.zip")
while True:
	sys.stdout.write(z.getinfo(nextfile+".txt").comment)
	content=z.read(nextfile+".txt")
	nextfilecontent = re.match("Next nothing is ([0-9]+)",content)
	if nextfilecontent!=None:
		nextfile = nextfilecontent.groups()[0]
	else:
		break
