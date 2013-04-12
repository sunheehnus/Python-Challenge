#!/usr/bin/python
import sys
import urllib2
def buildContent():
    html = urllib2.urlopen(urllib2.Request("http://www.pythonchallenge.com/pc/def/ocr.html")).read()
    contents = html.split("\n")

    startpos=0
    while not contents[startpos].startswith("<!--"):
        startpos += 1
    startpos += 1
    while not contents[startpos].startswith("<!--"):
        startpos += 1
    startpos += 1
    
    endpos = -1
    while not contents[endpos].startswith("-->"):
        endpos -= 1
    return contents[startpos:endpos]
def buildDict(contents):
    dictory = {}
    for eachline in contents:
        for eachchar in eachline:
            if eachchar in dictory.keys():
                dictory[eachchar]+=1
            else:
                dictory[eachchar]=1
    return dictory
def buildRarechararray(dictory):
    rarechararray=[]
    for key in dictory.keys():
        if dictory[key] < 10:
            rarechararray.append(key)
    return rarechararray

content=buildContent()
dictory=buildDict(content)
rarechararray=buildRarechararray(dictory)

for eachline in content:
    for eachchar in eachline:
        if eachchar in rarechararray:
            sys.stdout.write(eachchar)
print 
