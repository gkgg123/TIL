import collections

### 보물섬은 모든 경우에 대해서 bfs를 했다.
### 그리고 깊이를 측정해놓고 그리고 맥스값을 찾아주었다.
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def bfs(x,y):
    q=collections.deque()
    q.append([x,y])
    visited=[[0]*M for i in range(N)]
    visited[x][y]=1
    max_value=0
    while q:
        ax,ay=q.popleft()
        for i in range(4):
            nx=ax+dx[i]
            ny=ay+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if arr[nx][ny]=='L' and visited[nx][ny]==0:
                    q.append([nx,ny])
                    visited[nx][ny]=visited[ax][ay]+1
                    if visited[nx][ny]>max_value:
                        max_value=visited[nx][ny]
    return max_value
    



N,M=list(map(int,input().split()))

arr=[list(input()) for i in range(N)]

result=0
for i in range(N):
    for j in range(M):
        if arr[i][j]=='L':
           b = bfs(i,j)
           if b>result:
               result=b
print(result-1)