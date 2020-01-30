import sys
sys.stdin=open("buildng_swexpert_1day.txt",'r')
for j in range(1,11):
    le=int(input())
    b=list(map(int,input().split()))
    temp=0
    total=[]
    for i in range(2,le-2):
        temp=b[i]-max([b[i-2],b[i-1],b[i+1],b[i+2]])
        if temp>0:
            total.append(temp)
        temp=0
    print('#{} {}'.format(j,sum(total)))