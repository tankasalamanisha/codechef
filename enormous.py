#!/usr/bin/env python

n,k= input().split()
n=int(n)
k=int(k)
flag=0
for i in range(n):
	a=int(input())
	#print(a)
	if(a%k==0):
		flag+=1
print("{} {}".format(n,k))
print(" {}".format(flag))
