#!/usr/bin/python
def nextitem(currentnum):
	currentnum = str(currentnum)
	nextnum = ""
	start = 0
	end = 0
	while end < len(currentnum):
		while end < len(currentnum) and currentnum[end]==currentnum[start]:
			end += 1
		nextnum += str(end-start)+currentnum[start]
		start = end
	return nextnum
item = nextitem(1)
for i in range(0,29):
	item = nextitem(item)
print len(item)
