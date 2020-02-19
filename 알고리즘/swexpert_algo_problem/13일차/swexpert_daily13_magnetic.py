import sys
sys.stdin=open('magnetic.txt','r')

for tc in range(1,2):
    N=int(input())
    arr=[list(map(int,input().split())) for i in range(N)]
    t=50
    while t>0:
        for j in range(N):
            for i in range(N):
                if arr[i][j]==1:
                    break
                elif arr[i][j]==2:
                    arr[i][j]=0

        for j in range(N):
            for i in range(N-1,-1,-1):
                if arr[i][j]==2:
                    break
                elif arr[i][j]==1:
                    arr[i][j]=0
        t-=1
    cnt=0
    for j in range(N):
        temp=0
        tt=0
        for i in range(N):
            if temp==0:
                if arr[i][j]==0:
                    temp=arr[i][j]
            else:
                if arr[i][j]!=0 and temp!=arr[i][j] and tt==0:
                    tt=1
                    temp=arr[i][j]
                elif arr[i][j]!=temp and tt==1 and arr[i][j]!=0:
                    cnt+=1
                    tt=0
                    temp=arr[i][j]
        if temp!=0:
            cnt+=1


    print(cnt)