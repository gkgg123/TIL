import collections

dx=[-1,1,0,0]
dy=[0,0,1,-1]
U,D,R,L=0,2,4,8
tunnel=[
    [0],
    [U,D,R,L],
    [U,D],
    [R,L],
    [U,R],
    [D,R],
    [D,L],
    [U,L]
]
def bfs(x,y):
    global visited_cnt
    global L
    q=collections.deque()
    q.append([x,y])
    total_cnt=1
    visited[x][y]=visited_cnt
    while q:
        if visited_cnt==L:
            return total_cnt
        for _ in range(len(q)):
            ax,ay=q.popleft()
            dire=tunnel[arr[ax][ay]]
            for t in dire:
                for k in range(4):
                    if t&1<<k:
                        nx=ax+dx[k]
                        ny=ay+dy[k]
                        if 0<=nx<N and 0<=ny<M:
                            if visited[nx][ny]==-1 and arr[nx][ny]>0:
                                if k==0:
                                    if 2 in tunnel[arr[nx][ny]]:
                                        q.append([nx,ny])
                                        visited[nx][ny]=visited_cnt+1
                                        total_cnt+=1
                                elif k==1:
                                    if 1 in tunnel[arr[nx][ny]]:
                                        q.append([nx,ny])
                                        visited[nx][ny]=visited_cnt+1
                                        total_cnt+=1
                                elif k==2:
                                    if 8 in tunnel[arr[nx][ny]]:
                                        q.append([nx,ny])
                                        visited[nx][ny]=visited_cnt+1
                                        total_cnt+=1
                                else:
                                    if 4 in tunnel[arr[nx][ny]]:
                                        q.append([nx,ny])
                                        visited[nx][ny]=visited_cnt+1
                                        total_cnt+=1
        visited_cnt+=1
        

    return total_cnt





T=int(input())

for tc in range(1,T+1):
    N,M,R,C,L=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    visited=[[-1]*M for _ in range(N)]
    visited_cnt=1
    result=bfs(R,C)

    print('#{} {}'.format(tc,result))