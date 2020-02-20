import collections
#### 단지 번호 붙이기는 bfs를 이용했다. 그러면서 했던것은 bfs를 하면서 단지의 수를 구해주었다.
#### 그리고 그걸 sort() 해주었고, 그리고 난뒤에 저장된 리스트의 길이를 먼저 출력하고, 단지의 수를 출력하였다.
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def bfs(x,y):
    q=collections.deque()
    q.append([x,y])
    visit[x][y]=1
    cnt=1
    while q:
        ax,ay=q.popleft()
        for k in range(4):
            nx=ax+dx[k]
            ny=ay+dy[k]
            if 0<=nx<N and 0<=ny<N:
                if arr[nx][ny]==1 and visit[nx][ny]==0:
                    visit[nx][ny]=1
                    q.append([nx,ny])
                    cnt+=1
    total.append(cnt)



N=int(input())
arr=[list(map(int,list(input()))) for i in range(N)]
visit=[[0]*N for i in range(N)]
total=[]
for i in range(N):
    for j in range(N):
        if arr[i][j]==1 and visit[i][j]==0:
            bfs(i,j)
total.sort()

print(len(total))
for kk in total:
    print(kk)

