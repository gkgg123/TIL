dx=[1,0]
dy=[0,1]


def dfs(x,y,sum_total):
    global total_min

    if x==N-1 and y==N-1:
        if sum_total<total_min:
            total_min=sum_total
            return
    if sum_total>=total_min:
        return
    else:
    
        for i in range(2):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if visited[nx][ny]==0:
                    visited[nx][ny]=1
                    dfs(nx,ny,sum_total+arr[nx][ny])
                    visited[nx][ny]=0


T=int(input())


for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    total_min=9999999
    visited=[[0]*N for _ in range(N)]
    visited[0][0]=1
    dfs(0,0,arr[0][0])
    print('#{} {}'.format(tc,total_min))