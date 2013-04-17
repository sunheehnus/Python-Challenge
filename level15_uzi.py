#!/usr/bin/python
from datetime import date
from calendar import isleap
yearlist=[]
for i in range(10):
	year = 106 + i*10
	if isleap(year):
		if date(year,1,1).isoweekday()==4:
			yearlist.append(year)
for i in range(100):
	year = 1006+i*10
	if isleap(year):
		if date(year,1,1).isoweekday()==4:
			yearlist.append(year)
print yearlist[-2]
print "*"*40
print "mozart was born in 1756.1.27."
