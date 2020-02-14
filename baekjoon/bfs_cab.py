import collections
import sys

sys.stdin=open('cab.txt','r')
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def bfs(n):
    que=collections.deque()
    que.append(n)
    while que:
        t=que.popleft()
        ax=t//1000000
        ay=t%1000000
        for i in range(4):
            nx=ax+dx[i]
            ny=ay+dy[i]
            if 0<=nx<M and 0<=ny<N:
                if arr[nx][ny]==1 and visit[nx][ny]==-1:
                    que.append(1000000*nx+ny)
                    visit[nx][ny]=0
    return


T=int(input())
    
for tc in range(1,T+1):
    N,M,K=list(map(int,input().split()))
    arr=[[0 for j in range(N)] for i in range(M)]
    visit=[[-1]*N for i in range(M)]
    
    for _ in range(K):
        y,x=list(map(int,input().split()))
        arr[x][y]=1
    cnt=0
    for i in range(M):
        for j in range(N):
            if arr[i][j]==1 and visit[i][j]==-1:
                cnt+=1
                visit[i][j]=0
                bfs(i*1000000+j)
    print(cnt)
    
