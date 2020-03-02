import collections
### 기본적으로 BFS를 이용해서 풀었고, 내가 다음에 가고 싶은 위치와 내가 있는 현재 위치가 연결되어있는지만 확인해주면 되는 문제이다.
### 나는 dx,dy를 up down right left 순으로 했는데
### 이 문제는 별다른 list를 안 만들고 연결되었는지 판별하고 싶으면
### up right down left 처럼 (위,아래),(오른쪽,왼쪽) 을 두칸씩 떨어트려놓으면 별다른 list를 안 만들고도 판별이 가능하다.

dx=[-1,1,0,0]
dy=[0,0,1,-1]
U,D,R,L=0,1,2,3 ### UP DOWN RIGHT LEFT에 맞는 index를 찾아주기 위하여, 각각을 index를 설정해 주었다.

### Tunnel 모양을 각 방향에 따라 만들어 주었다.
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

############## 이 부분이 다음의 터널과 현재 터널이 이어져있는지 확인해주기 위해 만들어 준 index 이다.
## 만약 현재 터널에서 UP을 가면 위의 터널은 DOWN을 가지고 있어야 이어진다.
##                  DOWN을 가면 아래 터널은 UP을 가지고 있어야 이어진다.
##                  Right을 가면 오른쪽  터널은 LEFT를 가지고 있어야 이어진다.
##                  LEFT으로 가면 왼쪽 터널은 Right를 가지고 있어야 이어진다.
## 이걸 index로 생각해보면
## 현재터널 다음터널##
##  0     -> 1
##  1     -> 0
##  2     -> 3
##  3     -> 4
## 로 설정해주면 이어져 있는지 판별할수 있다.
test=[1,0,3,2]
############# 추가 설명 ###
## 이 문제는 제가 순서를 U,D,R,L로 해서 이렇게 복잡하게 하지만
## 만약 U,R,D,L 식으로 저장을 해놨으면
### (index+2)%4 로 판별을 하면 쉽게 될수 있다.


def bfs(x,y):
    global visited_cnt
    global L
    q=collections.deque()
    q.append([x,y])
    total_cnt=1  ### 이거는 죄수가 있을수 있는 모든 장소를 세어주기 위해 만들어준 변수이다.
    visited[x][y]=True  ## 한번 방문한곳은 True롤 바꿔주었다.
    while q:
        if visited_cnt==L:   ### 만약에 죄수가 움직인 시간이 L이 되었다면, 이 while문을 그만두고, total_cnt를 반환해주었다.
            return total_cnt
        for _ in range(len(q)):  ### 이거는 한번 같은위체엇 판별할수 있는걸 다 판별 하기 위해서, q의 길이만큼 for문을 돌렸다.
            ax,ay=q.popleft()
            dire=tunnel[arr[ax][ay]]  ### 현재 위치에서의 움직일수 방향을 tunnel 리스트를 통해 뽑아냈다.
            for t in dire:               
                nx=ax+dx[t] ### 그리고 Tuunel리스트로 뽑아낸 dire 리스트를 통해 우리가 가고자 하는 위치들을 하나하나
                ny=ay+dy[t] ### 탐색을 해주었다.
                if 0<=nx<N and 0<=ny<M:
                    if not(visited[nx][ny]) and arr[nx][ny]: ### 우리가 한번도 방문하지 않았고, arr[nx][ny]가 0이 아니고,
                        if test[t] in tunnel[arr[nx][ny]]:   ### 현재 터널과 다음터널이 이어져 있으면,
                            visited[nx][ny]=True             ### 다음터널을 nx,ny를 append를 해주고 방문을 표시한다.
                            q.append([nx,ny])
                            total_cnt+=1                    ### 그리고 전체 total_cnt를 1을 늘려준다.
                        
        visited_cnt+=1   ## 위의 하나의 q에 대해서 일련의 과정이 끝나면 걸린시간을 +1 해준다.
        

    return total_cnt





T=int(input())

for tc in range(1,T+1):
    N,M,R,C,L=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    visited=[[False]*M for _ in range(N)]
    visited_cnt=1   ### 우리는 L 시간동안 죄수가 돌아다닐수 있고, 처음 맨홀을 들어갔을때부터 1시간으로 치므로 1로 처음수치를 정했다.
    result=bfs(R,C)  ### bfs를 해줬다.

    print('#{} {}'.format(tc,result))