#!usr/bin/env python
def factorial(num):
    fact=1
    while(num!=0):
        if(num==0):
            return 1
        elif(num==1):
            return 1
        else:
            fact=num*factorial(num-1)
            return fact
r=int(input())
factl=[]
for i in range(r):
    num=int(input())
    factl.append(factorial(num))
for j in factl:
    print(j)
