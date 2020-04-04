from collections import deque
import sys
sys.stdin=open('5120.txt','r')


T=int(input())
for tc in range(1,T+1):
    N,M,K=map(int,input().split())

    que=deque()
    arr=list(map(int,input().split()))
    que.extend(arr)
    ind=0
    while K:
        if ind+M<N:
            ind=ind+M
            temp=que[ind]+que[ind-1]
            que.insert(ind,temp)
            N+=1
        elif ind+M==N:
            ind=ind+M
            temp=que[ind-1]+que[0]
            que.append(temp)
            N+=1
        else:
            ind=ind+M-N
            temp=que[ind]+que[ind-1]
            que.insert(ind,temp)
            N+=1
        K-=1
    print('#{} '.format(tc),end='')
    if len(que)<10:
        while que:
            print(que.pop(),end=' ')
    else:
        for i in range(10):
            print(que.pop(),end=' ')
    print('')



