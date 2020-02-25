import collections
import sys
sys.stdin=open('bridge2.txt','r')
dx=[-1,1,0,0]
dy=[0,0,1,-1]

def bfs(x,y,number):
    q=collections.deque()
    q.append([x,y])
    visited[x][y]=1
    arr[x][y]=number
    while q:
        ax,ay=q.popleft()
        for i in range(4):
            nx=ax+dx[i]
            ny=ay+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if arr[nx][ny]==1 and visited[nx][ny]==0:
                    q.append([nx,ny])
                    arr[nx][ny]=number
                    visited[nx][ny]=1

def find_min_distance(land_number):
    dist=[[-1]*M for _ in range(N)]
    q=collections.deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j]==land_number:
                dist[i][j]=0
                q.append([i,j])

    while q:
        x,y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if dist[nx][ny]:
                    distance=1
                    while True:
                        nx=nx+dx[i]
                        ny=ny+dy[i]
                        if nx<0 or nx>=N or ny<0 or ny>=M:
                            break
                        if dist[nx][ny]==0:
                            break
                        if 0<=nx<N and 0<=ny<M:
                            if arr[nx][ny]>0 and arr[nx][ny]!=land_number:
                                if distance>1:
                         
                                    min_distance[arr[nx][ny]][land_number]=min(min_distance[arr[nx][ny]][land_number],distance)
                                    min_distance[land_number][arr[nx][ny]]=min(min_distance[land_number][arr[nx][ny]],distance)
                                break
                        
                        
                        distance+=1





N,M=list(map(int,input().split()))

island=1
arr=[list(map(int,input().split())) for i in range(N)]
visited=[[0]*M for i in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j]==1 and visited[i][j]==0:
            bfs(i,j,island)
            island+=1

min_distance=[[99999]*(island) for _ in range(island)]
for i in range(1,island):
    find_min_distance(i)

total_list=[]
for i in range(island):
    for j in range(island):
        if min_distance[i][j]!=99999:
            total_list.append([i,j,min_distance[i][j]])
total_list.sort(key= lambda x : x[2])

conneted_list=[0]*island
conneted_list[0]=1
conneted_list[1]=1

result=0
while sum(conneted_list)!=island:
    for total in total_list:
        start =total[0]
        end = total[1]
        value=total[2]
        if conneted_list[start] or conneted_list[end]:
            if conneted_list[start] and conneted_list[end]:
                continue
            else:
                conneted_list[start]=1
                conneted_list[end]=1
                result+=value
                break
    else:
        result=-1
        break

print(result)

