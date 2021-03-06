import sys
import collections
import copy
dx=[-1,1,0,0]
dy=[0,0,1,-1]
def bfs(kx,ky,tt):
    global min_num
    global max_num
    q=collections.deque()
    q.append([kx,ky])
    visited[kx][ky]=True
    total=[]
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if min_num<=abs(arr[nx][ny]-arr[x][y])<=max_num and visited[nx][ny]==False:
                    tt=1
                    q.append([nx,ny])
                    total.append([nx,ny])
                    visited[nx][ny]=True
    if tt==1:
        total.append([kx,ky])
    return total





N,min_num,max_num=list(map(int,sys.stdin.readline().split()))

arr=[list(map(int,sys.stdin.readline().split())) for i in range(N)]
move=0
while True:
    cnt=0
    visited=[[False]*N for _ in range(N)]
    arr_temp=copy.deepcopy(arr)
    for i in range(N):
        for j in range(N):
            if visited[i][j]==False:
                temp=bfs(i,j,0)
                # print(temp)
                if temp:
                    temp_sum=0
                    for mat in temp:
                        temp_sum+=arr[mat[0]][mat[1]]
                    avg=temp_sum//len(temp)
                    for mat in temp:
                        arr_temp[mat[0]][mat[1]]=avg
                    cnt+=1
    if cnt:
        move+=1
        arr=arr_temp
    else:
        break


print(move)
