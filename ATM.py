#!/usr/bin/env python

x,y=input().split()

x=int(x)

y=float(y)

if(x>=y):
	print(y)
else:
	if(x%5==0):
		y=y-float(x)-0.50
		print(y)
