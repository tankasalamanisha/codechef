"""
https://www.codechef.com/problems/FLOW006
Program to print sum of the digits of input number
"""
#!/usr/bin/env python

n=int(input())
ls=[]

for i in range(n):
	sum=0
	k=int(input())
	while(k!=0):
		sum=sum+int(k%10)
		k=k/10
	ls.append(sum)
for j in ls:
	print(j)
