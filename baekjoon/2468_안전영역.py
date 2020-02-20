import collections


#### 이건 bfs를 사용했다. 물이 잠기는 깊이 이상의 건물을 찾아내고, 그리고 그 무리의 개수를 찾아냈ㄷ.
#### 그런데 여러번 틀린 이유 중하나는 비가 하나도 안왔을때를 가정을 못했었다.
dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(x,y,num):
    q=collections.deque()
    q.append([x,y])
    visit[x][y]=1
    while q:
        ax,ay=q.popleft()
        for i in range(4):
            nx=ax+dx[i]
            ny=ay+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if arr[nx][ny]>num and visit[nx][ny]==0:
                    visit[nx][ny]=1
                    q.append([nx,ny])



N=int(input())
arr=[list(map(int,input().split())) for i in range(N)]
total=[]
max_ind=0
for k in range(0,100):
    visit=[[0]*N for i in range(N)]
    cnt=0
    for i in range(N):
        for j in range(N):
            if arr[i][j]>k and visit[i][j]==0:
                bfs(i,j,k)
                cnt+=1
    if cnt==0:
        break
    elif max_ind<=cnt:
        max_ind=cnt
print(max_ind)