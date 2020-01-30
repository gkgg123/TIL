import sys
sys.stdin=open("buildng_swexpert_1day.txt",'r')
for i in range(1,11):
    le=int(input())
    building=list(map(int,input().split()))
    temp=[]
    total=[]
    for i in range(2,le-2):
        if building[i]>building[i-1] and building[i]>building[i-2] and building[i]>building[i+1] and building[i]>building[i+2]:
            temp=[building[i-1],building[i-2],building[i+1],building[i+2]]
            total.append(building[i]-max(temp))
        temp=[]
    print(sum(total))