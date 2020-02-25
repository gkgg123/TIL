## 이 문제는 bfs로 풀었다. bfs로 돌면서 조건에 만족하는 위치들을 total에 저장해놓고 return 해줬다.
## 만약에 조건을 만족하는 것이 없으면 total이 빈리스트이기 때문에 밑의 값을 변화시키는 조건문에 들어가지 못한다.
## 그리고 어차피 한번 방문한곳은 다른 곳에서 조사하지 못하므로 deepcopy로 원본데이터를 복사해서 할 필요없이 바로 값을 변화시켜도 상관없다.


import sys
import collections
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
    if tt==1: ### 한번이라도 조건을 만족한게 있으면 tt가 1이 되서 제일 처음 위치의 index를 추가해주었다.
        total.append([kx,ky])
    return total





N,min_num,max_num=list(map(int,sys.stdin.readline().split()))

arr=[list(map(int,sys.stdin.readline().split())) for i in range(N)]
move=0
while True:
    cnt=0
    visited=[[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j]==False:
                temp=bfs(i,j,0)
                if temp: ### 값을 변화시키는 조건문###
                    temp_sum=0
                    for mat in temp:
                        temp_sum+=arr[mat[0]][mat[1]]
                    avg=temp_sum//len(temp)
                    for mat in temp:
                        arr[mat[0]][mat[1]]=avg
                    cnt+=1
    if cnt:
        move+=1
        ### 한번이라도 값을 변화시키는 조건문에 들어온적이 있으면, 인구이동이 발생한것이므로 move를 1개씩 올려주었다.
    
    else:
        ### 그리고 한번도 값을 변화시킨적이 없으면 cnt=0이므로 이쪽에 들어와 while문을 빠져나간다.
        break


print(move)
