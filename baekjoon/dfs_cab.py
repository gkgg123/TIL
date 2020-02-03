dx=[1,-1,0,0]
dy=[0,0,1,-1]
def dfs(x,y,_cnt):
    dist[x][y]=_cnt

    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<N and 0<=ny<M:
            if arr[nx][ny] and dist[nx][ny]==-1:
                dfs(nx,ny,_cnt)




t=int(input())
for _ in range(t):
    M,N,K=map(int,input().split())
    arr=[[0 for col in range(M)] for row in range(N)]
    dist=[[-1 for col in range(M)] for row in range(N)]
    for _ in range(K):
        y,x=map(int,input().split())
        arr[x][y]=1
    
    cnt=0

    for i in range(N):
        for j in range(M):
            if arr[i][j]==1 and dist[i][j]==-1:
                cnt+=1
                dfs(i,j,cnt)
    print(cnt)

    