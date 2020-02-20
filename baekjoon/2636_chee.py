import collections
dx=[1,-1,0,0]
dy=[0,0,1,-1]
### cbfs는 최초에 공기에 누출된 곳을 -1로 바꿔주는 함수 ####
def cbfs():
    q=collections.deque()
    q.append([0,0])
    arr[0][0]=-1
    visited[0][0]=0
    while q:
        x,y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if arr[nx][ny]==0 and visited[nx][ny]==-1:
                    q.append([nx,ny])
                    arr[nx][ny]=-1
                    visited[nx][ny]=0

#### ccbfs는 치즈가 녹아서 생긴 공간부터 새로 공기에 누출된 범위를 -1로 바꿔주는 함수####
def ccbfs(x,y):
    q=collections.deque()
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
    cnt=0
    for t in range(4):
        nx=x+dx[t]
        ny=y+dy[t]
        if 0<=nx<N and 0<=ny<M:
            if arr[nx][ny]==-1:
                cnt+=1
    if cnt:
        total.append([x,y])


### 기본 풀이 방법 ###
### 4면이 무조건 공기에 누출되어 있으므로, 0,0 부터 시작해서 처음에 공기에 누출된 부분을 전부 -1로 바꿔주었다.
### 그리고 치즈의 위치를 찾아 4면에 -1이 존재할시 공기에 누출된거이니 사라질 치즈로 판정하였고, 그거의 개수를 세워줬다.
### 그리고 사라질 치즈의 위치를 저장하여, 해당 행렬 값을 -1로 바꿔주었고, 거기서부터 다시 bfs를 하여 공기에 누출된
### 것을 다시 판정해주었다.
### 그리고 마지막으로 사라지고 난뒤에 다 없어졌을때를 체크하므로 전체 측정된 시간에서 -1 을 해줬다.
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
        arr[k[0]][k[1]]=-1
    ches_hour+=1
    for k in total:
        ccbfs(k[0],k[1])
    if ches_cnt==0:
        result.append(ches_hour-1)
        result.append(pre)
        break

print(result[0])
print(result[1])


