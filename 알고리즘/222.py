# a=list(map(int,input().split()))
# print(a)

import sys

T=int(input())
numbers=list(map(int,sys.stdin.readline().split()))
loca=[]
loca.append(numbers[0])
temp=0
for i in numbers[1:]:
    for ind,val in enumerate(loca):
        if val>i and i not in loca:
            loca[ind]=i
            temp=0
        elif val<i and i not in loca:
            temp=i
    if temp>0:
        loca.append(temp)
    temp=0
print((len(loca)))