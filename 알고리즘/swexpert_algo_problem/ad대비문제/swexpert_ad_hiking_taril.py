import copy
import sys
sys.stdin=open('hiking.txt','r')

### 등산로 조성 ####
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def dfs(x,y,arr,cut,cnt):
    visit[x][y]=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<N:
            if arr[nx][ny]<arr[x][y] and visit[nx][ny]==-1 and arr[nx][ny]>=0:
                ### 깎을 필요가 없을때에는 dfs 재귀함수로 계속 돌려주었다.                
                visit[nx][ny]=0
                dfs(nx,ny,arr,cut,cnt+1)
            elif arr[nx][ny]>=arr[x][y] and cut >0 and visit[nx][ny]==-1 and arr[x][y]>=0:
                ### 이 부분에서 처음에 cut을 !=로 했다가 cut이 -가 될때까지해서 문제가 됬다 그래서 0보다 커야로 바꿔줬다.
                ### 또한 arr[x][y]가 0보다 크게 한것도 처음 문제를 제대로 이해하지 못해 한것인데 어차피 주어진 조건이 
                ### 1이상의 수로 주어지므로 필요는 없어보였다.
                temp_cut=arr[nx][ny]-arr[x][y]+1
                ### 깎아야할 때 깎아야할 수치를 구해주었다.
                if temp_cut<=cut:
                    ### 그리고 깎아야할 수치가 주어진 cut 수치보다 작을때 시행하도록 했다.
                    pre=arr[nx][ny]
                    ### 이부분에서 많이 해맸다.
                    ### 10개 테스트 케이스 중 5개만 맞았던 이유 중 하나가 이거 때문이었다.
                    ### 한번 값을 변환하고 더이상 가지 못하고 되돌아갔을때 그 값을 원상복구 시켜줘야한다.
                    ### 그래서 이전 값을 저장해 놓았다.
                    arr[nx][ny]=arr[nx][ny]-temp_cut
                    ### 최소한도로 깎아주고 값을 변화시켜주었다.
                    visit[nx][ny]=0
                    dfs(nx,ny,arr,0,cnt+1)
                    ### 여기도 함정이 있었다.
                    ### 처음에 공사횟수가 여러번이 가능할줄 알고 cut값을 temp_cut값을 뺀값을 넣어주었다.
                    ### 하지만 문제 조건에 명시된 것 중 하나가 바로
                    ### 단 한 번만 공사가 가능한 것이다. 그렇기 때문에 cut 값에 0을 넣어주었다.
                    arr[nx][ny]=pre
                    ### 이것은 이전 값으로 되돌려주는것으로 바로 위의 재귀함수를 탈출했다는것은
                    ### 값을 변화시켰을때의 노드를 전부 탐색했다는것과 같다.
                    ### 그래서 값을 원래 상태로 복구 시켜준것이다.
    visit[x][y]=-1
    #### 이 부분 또한 우리가 한번 탐색을 하다가 잘못 탐색을 하고 되돌아 올수 있다.
    #### 근데 그 부분을 다시 방문 할 수 있는 일이다.
    #### 만약 우리가 아래부터 먼저 탐색을 한다고 치고 만약 다음과 같이 주어지면
    #### 9 8
    #### 1 7
    #### 로 주어졌다 치자. 그러면 우리는 9에서 아래로 탐색하기 때문에 1을 방문을 하였다. 그러면서 visit을 0으로 만들어준다.
    #### 그러나 1로 간뒤 다음 탐색을 하면 더이상 갈곳이 없어 9로 복귀를 한다.
    #### 그 뒤에 9->8->7을 간뒤에 정상적으로라면 1을 탐색을 해야하지만,
    #### 만약 visit을 초기화 시켜주지 않으면 이미 방문한곳이었기때문에 가지 않고 길이3으로 값을 출력하고 탐색을 중단할 것이다.
    #### 이 문제를 해결하기 위하여 dfs 검색이 끝나고 나면 visit을 초기화 해주었다.            
    value.append(cnt)
    
    return








T=int(input())

for tc in range(1,T+1):
    N,K=list(map(int,input().split()))
    hiking=[list(map(int,input().split())) for i in range(N)]
    max_index=[]
    max_value=0

    ### 처음에 max 값의 인덱스 위치를 구해주는 과정을 해주었다.
    ### 문제에서 첫 스타트 위치는 먼저 주어진 행렬에서 가장 큰 값을 기준으로 한다고 했다.
    ### 문제풀이 도중에 max 값이 변질 될 우려가 있으니 처음에 구해주었다.
    for i in range(N):
        for j in range(N):
            if hiking[i][j]>max_value:
                max_value=hiking[i][j]
                max_index.clear()
                max_index.append([i,j])
            elif hiking[i][j]==max_value:
                max_index.append([i,j])

    value=[]
    ### 그렇게 구해진 max값의 인덱스로 하여 for문을 돌렸고
    ### 여기서는 가장 긴 값을 구하는것이기 때문에
    ### bfs 대신 dfs를 썼다.
    for k in max_index:
        hiking_temp=copy.deepcopy(hiking)
        ### 원본 값이 변질될까 두려워 deepcopy를 썼지만
        ### 나중에 문제를 해결하다보니 변질된 값을 보전해주는 것을 찾아서 필요성이 낮아진것 같다.
        visit=[[-1]*N for i in range(N)]
        ### 이거는 visit으로 들렸던 곳을 다시 안가기 위해 만들어준 변수이다. 이걸 여기 for문안에 넣은 이유는
        ### 위에와 비슷한 이유로 다른 출발점에서 스타트할때 visit을 초기화 시켜주기 위해서 했지만
        ### 문제를 풀다보니 함수내에서 visit을 다시 초기화해주는 작업을 해서 필요성이 낮아진것 같다.
        dfs(k[0],k[1],hiking_temp,K,1)
        ### dfs에는 총 5가지의 원소가 들어갔따.
        ### 1. x축의 위치
        ### 2. y축의 위치
        ### 3. 등산경로의 행렬
        ### 4. 깎을 수 있는 양
        ### 5. 이동거리
        ### 이렇게 들었갔다. 처음 스타트위치에서 들어갈때부터 1부터 시작하므로 1이 들어갔다.
    print('#{} {}'.format(tc,max(value)))