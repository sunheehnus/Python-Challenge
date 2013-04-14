#!/usr/bin/python
#encoding=utf-8
#line15,16 本来有错误，一直做不出来
#应该是从网页读取的数据里'\x'表示为'\\x','\'字符不再表达转意的意思,而是表达自身是一个'\'
#在读取的字符串后面加上.decode('string_escape')即可完成转换
import urllib2
import re
import bz2
html = urllib2.urlopen(urllib2.Request("http://www.pythonchallenge.com/pc/def/integrity.html")).read().split("\n")
for unline in html:
	if re.match('un: ',unline):
		break
for pwline in html:
	if re.match('pw: ',pwline):
		break
un = re.match('.*\'(.*)\'',unline).groups()[0]
pw = re.match('.*\'(.*)\'',pwline).groups()[0]
print "usrname: ",bz2.decompress(un.decode('string_escape'))
print "password:",bz2.decompress(pw.decode('string_escape'))
