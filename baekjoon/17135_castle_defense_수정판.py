import itertools
from copy import deepcopy
import collections
dx=[-1,0,0]
dy=[0,-1,1]
### 기본적으로 수정전이랑 비슷하지만, 몇몇 부분이 바뀌었다.
### 이 문제는 어차피 아래에서 위로 올라가면서 탐색을 하는거이기 때문에, (dx=1, dy=0) 아래쪽 방향을 탐색할 필요가 없기 때문에 빼주었다. 
### 그리고 완전 탐색을 하다보니, 사정거리 D를 넘어가서도 계속 탐색을 해서, 시간이 오래걸리는 문제점을 해결했다.

def move():
    field.pop(N-1)
    field.insert(0,[0]*M)

def set_Archer(team):
    for j in team:
        field[N][j]=2
    return [[N, j] for j in team]

def attack(team):
    global visited_cnt
    attack_list=set()
    
    for k in team:
        visited_cnt+=1
        temp=bfs(k[0],k[1])
        if temp:
            attack_list.add(temp)
    for t in attack_list:
        field[t[0]][t[1]]=0
    return len(attack_list)


def bfs(x,y):
    global D
    q=collections.deque()
    q.append([x,y])
    visited[x][y]=visited_cnt
    result=[]
    distance_cnt=0 ## 우리가 얼마만큼의 거리를 탐색했는지 확인 해줄려고 넣은 변수이다.
    while q:
        for _ in range(len(q)): ## 이건 같은거리만큼 탐색을 해주기 위해 for문을 추가해준것이다. 이 for문이 한번 끝날때마다 1만큼 떨어진 거리를 추가로 검색을 완료한것을 나타낸다.
            ax,ay=q.popleft()
            for i in range(3):
                nx=ax+dx[i]
                ny=ay+dy[i]
                if 0<=nx<N+1 and 0<=ny<M:
                    if field[nx][ny]!=1 and visited[nx][ny]<visited_cnt:
                        q.append([nx,ny])
                        visited[nx][ny]=visited_cnt
                    elif field[nx][ny]==1 and visited[nx][ny]<visited_cnt:
                        visited[nx][ny]=visited_cnt
                        q.append([nx,ny])
                        distance=abs(nx-x)+abs(ny-y)
                        if distance<=D:
                            if result:
                                if result[2]>distance:
                                    result[0]=nx
                                    result[1]=ny
                                    result[2]=distance
                                elif result[2]==distance:
                                    if result[1]>ny:
                                        result[0]=nx
                                        result[1]=ny
                                        result[2]=distance                        
                            else:
                                result.append(nx)
                                result.append(ny)
                                result.append(distance)
        distance_cnt+=1

        if result:  ## 짧은거리부터 탐색을 하는 것이므로, 그때 result가 존재한다면 값을 return 해주었다.
            return tuple(result[0:-1])
        if distance_cnt==D: ## 사정거리 D이상의 위치의 적을 탐색해봤자, 어차피 공격을 하지 못하니 
            if result:      ## 그때 result 값이 있으면 반환해주고 없으면 그냥 아무것도 반환을 안해주었다.
                return tuple(result[0:-1])


    
N,M,D=list(map(int,input().split()))
arr=[list(map(int,input().split())) for i in range(N)]
arr.append([0]*M)

visited=[[-1]*M for i in range(N+1)]
Archer_collect=itertools.combinations(range(M),3)
max_attack=0
visited_cnt=0
for Archer_list in Archer_collect:
    field=deepcopy(arr)
    Archer_index=set_Archer(Archer_list)
    enemy=0
    for i in range(N):
        enemy+=attack(Archer_index)
        move()

    if enemy>max_attack:
        max_attack=enemy

            
print(max_attack)

