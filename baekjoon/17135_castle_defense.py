import itertools
from copy import deepcopy
import collections

### 완전 탐색을 통해, 궁수가 공격하는 적의 수를 구해주었다.
### 함수는 크게 4가지이다.
### 먼저, 한번 궁수들잉 공격한뒤에 한턴이 지났을때 전체 field들을 한칸씩 내려주는 작업을 하는 move 함수
### 두번째는 궁수들의 위치들에 맡게 field에 값을 넣어주고, 궁수들의 위치를 이중리스트로 return해주는 set_Archer 함수
### 세번째는 궁수들이 공격하고, 적을 공격하면 해당 위치의 값을 0으로 바꿔주는 attack 함수
### 마지막으로 궁수들이 제일 먼저 공격할 적 위치를 찾아내는 bfs 함수이다.,



dx=[1,-1,0,0]
dy=[0,0,-1,1]


def move():
    field.pop(N-1)  ### N번째에는 궁수들이 있으므로, N-1번째의 칸이 적들이 있을 마지막 칸이므로 없애준다.
    field.insert(0,[0]*M)  ### 그리고 제일 첫번째에 0을 넣어주면 전체 칸이 한칸씩 내려온것과 같이 구현해줄수 있다.

def set_Archer(team):
    for j in team:
        field[N][j]=2            ### 해당 궁수들이 있는 자리를 2로 바꿔주고, 궁수들의 index들을 2중 리스트로 반환해주었다.
    return [[N, j] for j in team]

def attack(team):
    global visited_cnt

    attack_list=set()  ### 궁수들이 중복된 위치를 공격할 수 있으므로, 그걸 자연적으로 막아주기 위해 중복이 허용되지않는 set을 사용했다.
                        ### set을 쓸때 주의해야할 점은, set에 list형태를 저장할 수 없으므로, tuple형태로 저장해야한다는 것이다.
    
    for k in team:   ### 우리는 궁수들의 숫자만큼 공격을 할 것이고, 공격이 가능한지를 bfs를 통해 구해낼것이다.
        visited_cnt+=1  ## 한번 궁수들을 이용해 공격할때마다, visited_cnt를 1씩 증가시켜주었다. 이것은 visited를 초기화하는 하는 작업을 줄이기 위해 추가한 것이다.

        temp=bfs(k[0],k[1])
        if temp:            ## 만약에 bfs에서 리턴된 튜플에 값이 있다면, attack_list에 추가를 해준다. 만약에 이작업을 안해주면, 
            attack_list.add(temp) ## set은 빈 튜플이라는 원소가 있는 것을 판별하여, 밑의 for문을 돌다가 index error가 날 수 있다.
    
    for t in attack_list:       ## 처치한 적들의 위치의 값을 0으로 바꿔주는 작업이다.
        field[t[0]][t[1]]=0
    return len(attack_list)    ## 처치한 적은 곧 attack_list의 길이와 같으므로 그 길이를 반환해준다.


def bfs(x,y):
    global D
    q=collections.deque()
    q.append([x,y])
    visited[x][y]=visited_cnt  ### visited 리스트의 값을 visited_cnt로 바꿔준다. 만약 첫번째 궁수가 들어왔을때 visited의 값의 최대값은 -1이다.
                               ### 두번째 궁수가 왔을때의 visited_cnt의 값은 2이고, visited 리스트의 최대값은 1일것이다.
                               ### 이렇듯 visited의 리스트 값이 visited_cnt보다 작다면 새로운 궁수가 들어왔을때 방문하지 않은 곳이므로,
                               ### 매번 visited를 초기화하는 불필요한 작업을 줄일 수있다.

    result=[]                  ### result는 궁수가 처치한 적의 x,y 값과 거리르 저장하기 위해서 만들어놨다.
  
  
    while q:
        ax,ay=q.popleft()
        for i in range(4):
            nx=ax+dx[i]
            ny=ay+dy[i]
            if 0<=nx<N+1 and 0<=ny<M:
                if field[nx][ny]!=1 and visited[nx][ny]<visited_cnt: ## 만약에 적이 없거나 궁수가 있는 위치이면서, 방문을 하지않은 곳이면, 
                    q.append([nx,ny])                                ## 그냥 q에 위치만 추가하고, visited의 값을 변화시켜준다.
                    visited[nx][ny]=visited_cnt


                elif field[nx][ny]==1 and visited[nx][ny]<visited_cnt:  ## 만약에 적이 있고, 우리가 방문하지않은 위치이면, 먼저 visited 값을 변화시키고
                    visited[nx][ny]=visited_cnt                         ## q에 위치를 추가시켜준다.
                    q.append([nx,ny])

                    distance=abs(nx-x)+abs(ny-y)                       ## 궁수와 적과의 거리를 구해주고, 거리가 사정거리보다 짧다면 result에 저장하는 작업을 한다.
                    
                    if distance<=D:
                        if result:                                      ## result에 기존의 값이 존재한다면, 다음과 같은 작업을 시행한다.
                            if result[2]>distance:                      ## 먼저 result에 있는 값보다 지금 구한 distance가 짧다면, result에 있는 값을 새로운 값으로 바꿔준다.
                                result[0]=nx
                                result[1]=ny
                                result[2]=distance

                            elif result[2]==distance:                   ## 만약에 기존의 result에 있는 distance와 지금 구한 distance가 같다면,
                                if result[1]>ny:                        ## result의 y축 값과 지금의 ny와 비교를 하여, ny가 더 작다면
                                    result[0]=nx                        ## 새로운 값으로 바꿔준다.
                                    result[1]=ny
                                    result[2]=distance                        
                        else:
                            result.append(nx)                           ## result에 아무값도 저장되어 있지않다면 처음으로 나온것이므로, 값을 추가해준다.
                            result.append(ny)
                            result.append(distance)

    return tuple(result[0:-1])  ## 우리가 원하는것은 적의 위치이므로 제일 마지막 값인 Distance를 제외하고 return 해준다.


    
N,M,D=list(map(int,input().split()))                 
arr=[list(map(int,input().split())) for i in range(N)]
arr.append([0]*M)  ### 궁수들이 있을 위치를 위해 젱리 마지막 칸에 0으로 초기화 된 리스트들을 넣어준다.

visited=[[-1]*M for i in range(N+1)]  ### 그리고 우리가 bfs를 할때 중복으로 방문하지 않게 하기 위하여, visted 리스트를 만들어줬다.

Archer_collect=itertools.combinations(range(M),3) ### Combination을 통해 궁수들의 위치를 정해줬는데 어차피 궁수들은 제일 마지막행인 N행에 있으므로, 열값들만 돌려주었다.

max_attack=0

visited_cnt=0  ## 이거는 visited 함수를 계속 초기화하면 시간이 걸릴것 같아서, visited를 몇번 이용했는지를 카운트를 해서, 초기화를 안해도 할 수 있게 구현을 했다.

for Archer_list in Archer_collect:

    field=deepcopy(arr)   ### 우리는 모든 경우의 수에 대해 전부 구해봐야하므로, 원본값에서 deepcopy를 해와 for문 안에서 쓰겠다.

    Archer_index=set_Archer(Archer_list)  ### 궁수들의 위치들을 [[a1,a2],[a1,a3],[a1,a4]] 형식으로 이중리스트로 받아왔다.
    
    enemy=0
    for i in range(N):   ### 우리는 1번의 타임당 행렬이 1칸씩 내려오므로 우리에게 총 N번의 시간이 주어진것으므로, N번을 시행했다.
        
        enemy+=attack(Archer_index) ### attack 함수를 통해 궁수들이 처치한 적들의 수를 구해 enemy에 더해주었다.

        move() ### 한턴의 공격이 끝나면 1칸씩 내려주는 작업을 했다.

    if enemy>max_attack:  ## 조합의 한 경우에 대해서 구해진 적이 끝나면 max_attack값과 비교화여 바꿔준다.
        max_attack=enemy

            
print(max_attack)

