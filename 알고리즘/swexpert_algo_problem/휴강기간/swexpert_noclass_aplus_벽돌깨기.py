import collections
import copy
import sys
sys.stdin=open('벽돌깨기.txt','r')
### 벽돌깨기는 크게 3가지 함수를 이용했다.
### 폭발을 전파시켜주는 bomb 함수
### 폭발을 하고 남은 벽돌들을 정렬해주는 함수인 sort_list 함수
### 마지막으로 벽돌깰 위치를 정해주는 함수인 dfs 함수를 썼다.

dx=[1,-1,0,0]
dy=[0,0,1,-1]


T=int(input())


def bomb(yy,data):
    visited=[[0]*W for _ in range(H)]  ### 구슬을 쏘면서 중복 방문을 막기위해, visited 함수를 썼다.
    dq=collections.deque()  ### 여기에는 폭발이 일어날 벽돌의 인덱스 x,y와 이 벽돌의 power를 저장해주기 위한 dq를 설정해주었다.
    for j in range(H):
        if data[j][yy]:
            dq.append([j,yy,data[j][yy]])  ## 위에 정해진 열 중에서 가장 첫번째로 만나는곳에 구슬이 부딪히게 되므로, 위에서부터 탐색을 해서 가장 가까운
            visited[j][yy]=1               ## 벽돌을 찾아주고, 그곳의 visited 값을 변환시켜주고
            data[j][yy]=0                  ## 폭발이 일어났으므로, 그 벽돌을 없애주면 된다.
            break
    while dq:     
        x,y,power=dq.popleft()        
        for i in range(4):   ### 4방향으로 탐색할것이다.
            nx=x
            ny=y
            for j in range(power-1):  ### 우리는 한쪽방향으로, 그 power-1만큼 전진해줄것이므로, 2중 for문을 썼다.
                nx=nx+dx[i]
                ny=ny+dy[i]
                if 0<=nx<H and 0<=ny<W:   ### 벽돌 탐색 방향이 행렬을 넘어가지 않고,
                    if data[nx][ny] and not(visited[nx][ny]):   ### 벽돌이 있으면서 방문하지 않은 곳이면,
                        dq.append([nx,ny,data[nx][ny]])         ### dq에 인덱스와 power를 저장해주고
                        data[nx][ny]=0                          ### 벽돌을 없애주고, visited를 바꿔준다.
                        visited[nx][ny]=1
    
    bt=[0]*W           ### 모든 과정이 끝나면 각 열의 벽돌의 개수를 다시 세서 저장해준다.
    for j in range(W):
        for i in range(H):
            if data[i][j]:
                bt[j]+=1
    return bt           ### 그리고 벽돌의 개수를 반환해준다.


def sort_list(dt):
    qu=collections.deque()          #### data 내에 있는 벽돌의 정보를 저장하기 위한 deque를 만들었다.
    rr_bt=[[0]*W for _ in range(H)]  ### 그리고 다시 정렬된 data를 반환해줄 rr_bt 2차원배열을 미리 만들어놨다.
    for j in range(W):
        for i in range(H-1,-1,-1):
            if dt[i][j]:
                qu.append(dt[i][j]) ### 밑에서 부터 탐색을 하면서 벽돌이 존재하면 해당 벽돌의 파워를 하나하나 저장해준다.
        row=H-1 ### 다 저장이 되었다면,
        while qu:
            da=qu.popleft()
            rr_bt[row][j]=da  ### 밑에서 부터 차곡 차곡 쌓을수 있도록 만들어준다.
            row-=1
    return rr_bt                      ### 이렇게 정렬된 data를 반환해준다.





def dfs(cnt,data,bl): ### cnt는 구슬을 몇번 쐈는지 확인해주는 변수, data는 벽돌이 어떻게 쌓아져있는지 2차원배열 , bl은 각 열마다의 벽돌의 개수가 몇개인지 알려주는 리스트이다.
    global min_value

    if cnt==N or sum(bl)==0: ### cnt가 N이 되면 모든 구슬을 다 쐈으므로, 그때의 전체 벽돌의 개수를 세서 비교를 해주면 된다.
        temp=sum(bl)        ### 또한 중간에 모든 벽돌이 사라지면, 더이상 dfs를 할 이유가 없으므로, sum(bl)이 0일때에도 들어오게 해주었다.
        if temp<min_value:
            min_value=temp
            return
    else:
        return_data=copy.deepcopy(data) ### 이건 한번 dfs를 해주다가 되돌아 왔을때 원본값을 되돌려주기 위하여, deepcopy를 썼다.
        for i in range(W):
            if bl[i]:  ### 해당 열에 벽돌이 1개라도 있어야 구슬을 쏠수 있으므로, bl[i]가 0이 아닐때에만 작동하게 해주었다.
                bt=bomb(i,data)   ### 열이 정해지면 해당 열에 구슬을 쏘고, 폭발을 일어나고 남은 벽돌의 개수를 반환해주는 함수 bomb을 만들어줬다.
                rr_tt=sort_list(data)  ### bomb 함수를 쓰고 나면, data 2차원배열 곳곳에 0이 생긴다. 그걸 없애주기 위해서 sort_list라는 함수를 만들었다.
                dfs(cnt+1,rr_tt,bt) ### 정렬된 data와 바뀐 block의 개수를 가지고 다음 dfs로 재귀함수를 해준다.
                data=copy.deepcopy(return_data) ## 재귀함수를 탐방하고 다음번으로 가기 위해서 이 for문에 들어오기전의 원본 데이터로 바꿔준다.



for tc in range(1,T+1):
    N,W,H=map(int,input().split())

    arr=[list(map(int,input().split())) for _ in range(H)]

    block_cnt=[0]*W
    ### 이건 각 열마다 벽돌이 몇개가 있는지 세주기 위한 리스트이다.
    for j in range(W):
        for i in range(H):
            if arr[i][j]:
                block_cnt[j]+=1

    min_value=999999

    dfs(0,arr,block_cnt)
    ### 내가 벽돌을 깨고 싶은 위치를 찾아주기 위하여 dfs를 썼다.
    print('#{} {}'.format(tc,min_value))