import sys
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y,cnt):
    global max_number
    if cnt>max_number:
        max_number=cnt
    visited[x][y]=True
    go_to=[]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if arr[nx][ny]=='L' and visited[nx][ny]==False:
                go_to.append([nx,ny])
    for i in go_to:
        visited[i[0]][i[1]]=True
    for k in go_to:
        dfs(k[0],k[1],cnt+1)

N,M=list(map(int,sys.stdin.readline().split()))
arr=[list(sys.stdin.readline()) for i in range(N)]
max_number=0
for i in range(N):
    for j in range(M):
        if arr[i][j]=='L':
            visited=[[False]*M for i in range(N)]
            dfs(i,j,0)
            
print(max_number)