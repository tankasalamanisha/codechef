"""
Program to test if a is divisible by b in a number of test cases T
"""
#!/usr/bin/env python
T=int(input())

j=[]

for i in range(T):
	a,b=input().split()
	result=int(a)%int(b)
	j.append(result)
for k in j:
	print(k)
