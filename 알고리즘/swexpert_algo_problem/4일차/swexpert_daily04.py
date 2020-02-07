import sys
sys.stdin=open("swexpert_daily04.txt",'r')

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    screw=list(map(int,input().split()))
    start=[]
    for ind,val in enumerate(screw):
        if screw.count(val)==1 and ind%2==0:
            start.append(screw[ind])
            start.append(screw[ind+1])
    while n>1:
        for ind,val in enumerate(screw):
            if start[-1]==val and ind%2==0:
                start.append(screw[ind])
                start.append(screw[ind+1])
        n-=1
    print('#{} '.format(tc),end='')
    for k in start:
        print(k,end=' ')
    print('')