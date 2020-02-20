import collections

dx=[1,-1,0,0]
dy=[0,0,1,-1]
#### 빙하 문제는 bfs를 사용하였다. bfs를 사용하여, 빙산 무리의 개수를 구해주었다. 그래서 그게 1개일때에만
#### melt 함수를 썼다. melt함수는 돌아가면서 빙하주변의 0의 개수를 세서 그만큼을 빼주는 역할을 했다.
#### 무한 반복을 하면서 빙산무리의 개수가 2개이상이면, break하여 time을 알려주었다.
#### 만약 빙하무리의 개수가 0개가 되는 경우는 무리가 1개로 끝났을떄이다.
#### 그래서 그때는 time을 0으로 초기화 해주었다.
#### 처음엔 deepcopy를 써서 시간이 많이 걸렸다.
#### 그러나 melt 함수를 쓰면서 해당 인덱스와 녹아드는 양을 저장했다.
#### 그리고 저장된 정보를 통해 원래 배열의 값을 변환시켜주었다.


def icebfs(x,y):
    q=collections.deque()
    q.append([x,y])
    visited[x][y]=1
    while q:
        ax,ay=q.popleft()
        for i in range(4):
            nx=ax+dx[i]
            ny=ay+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if arr[nx][ny]!=0 and visited[nx][ny]==0:
                    q.append([nx,ny])
                    visited[nx][ny]=1
    

def melt(x,y):
    cnt=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if arr[nx][ny]==0:
                cnt+=1
    k=[x,y,cnt]
    return k

N,M=list(map(int,input().split()))



arr=[list(map(int,input().split())) for i in range(N)]

time=0
while True:
    cnt=0
    meltdown=[]
    visited=[[0]*M for i in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j]!=0 and visited[i][j]==0:
                cnt+=1
                icebfs(i,j)
    if cnt==1:
        for i in range(N):
            for j in range(M):
                if arr[i][j]!=0:
                    meltdown.append(melt(i,j))
        for i in meltdown:
            if arr[i[0]][i[1]]>=i[2]:
                arr[i[0]][i[1]]-=i[2]
            else:
                arr[i[0]][i[1]]=0
        time+=1
    elif cnt==0:
        time=0
        break
    else:
        break
print(time)
        