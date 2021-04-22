#!usr/bin/env python
def sort(t,l):
    for i in range(t):
        for j in range(t-i-1):
            if(l[j]>l[j+1]):
                l[j],l[j+1]=l[j+1],l[j]
    for k in l:
        print(k)

t=int(input())
l=[]
for i in range(t):
    N=int(input())
    l.append(N)

sort(t,l)
