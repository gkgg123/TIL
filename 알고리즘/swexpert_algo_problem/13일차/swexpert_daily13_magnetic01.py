import sys
sys.stdin=open('magnetic.txt','r')

for tc in range(1,2):

    N=int(input())
    arr=[list(map(int,input().split())) for i in range(N)]
    cnt=0
    for j in range(100):
        t=0
        for i in range(100):
            if arr[i][j]==1:
                t=1
            elif arr[i][j]==2 and t==1:
                t=0
                cnt+=1
    print(cnt)
