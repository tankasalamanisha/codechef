#!/usr/bin/env python

n=int(input())
sum=0
result=[]
for i in range(n):
	a,b=input().split()
	sum=int(a)+int(b)
	result.append(sum)
for j in result:
	print(j)
