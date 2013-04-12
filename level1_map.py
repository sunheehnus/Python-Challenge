#!/usr/bin/python
import urllib2
startLower=ord("a")
startUpper=ord("A")
endLower=ord("z")
endUpper=ord("Z")

def Shiftby2(c):
    if c.isalpha():
        if startLower <= ord(c) <= endLower:
            if ord(c)+2 > endLower:
                return chr(startLower+ord(c)+2-endLower-1)
            else:
                return chr(ord(c)+2)
        else:
            if ord(c)+2 > endUpper:
                return chr(startUpper+ord(c)+2-endUpper-1)
            else:
                return chr(ord(c)+2)
    else:
        return c
html = urllib2.urlopen(urllib2.Request("http://www.pythonchallenge.com/pc/def/map.html")).read()
for eachline in html.split("\n"):
    if eachline.startswith("g fmnc"):
        targetline = eachline
resultline=""
for eachchar in targetline:
    resultline += Shiftby2(eachchar)
print resultline
