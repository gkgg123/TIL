import collections
dx=[1,-1,0,0]
dy=[0,0,1,-1]

def cbfs(x=0,y=0):
    q=collections.deque()
    arr[x][y]=-1
    q.append([x,y])
    while q:
        ax,ay=q.popleft()
        for i in range(4):
            nx=ax+dx[i]
            ny=ay+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if arr[nx][ny]==0 and visited[nx][ny]==-1:
                    q.append([nx,ny])
                    arr[nx][ny]=-1
                    visited[nx][ny]=0


### 주변에 공기가 인접해있는지 확인하는 함수#####
def cheese(x,y):
    for t in range(4):
        nx=x+dx[t]
        ny=y+dy[t]
        if 0<=nx<N and 0<=ny<M:
            if arr[nx][ny]==-1:
                total.append([x,y])
                return


N,M=list(map(int,input().split()))
result=[]
arr=[list(map(int,input().split())) for i in range(N)]
pre=0
ches_cnt=0
ches_hour=0
visited=[[-1]*M for i in range(N)]
cbfs()

while True:
    total=[]
    pre=ches_cnt
    ches_cnt=0
    for i in range(N):
        for j in range(M):
            if arr[i][j]==1:
                cheese(i,j)
                ches_cnt+=1
    for k in total:
        cbfs(k[0],k[1])
    ches_hour+=1
        
    if ches_cnt==0:
        result.append(ches_hour-1)
        result.append(pre)
        break

print(result[0])
print(result[1])