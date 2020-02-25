dx=[-1,1,0,0]
dy=[0,0,1,-1]
## up,down,right,left ##
U,D,R,L=1,2,4,8
cctv_view=[
    [0],
    [U,D,R,L],
    [U|D,R|L],
    [U|L,U|R,R|D,D|L],
    [L|R|U,U|R|D,R|D|L,L|D|U],
    [U|D|R|L]
]
### 해당 문제는 비트연산을 통해 방향을 정해주었다.###
### 1&1<<0 => 1을 반환
### 2&1<<1 => 1을 반환
### 4&1<<2 => 1을 반환
### 8&1<<3 => 1을 반환
### x&1<<k 를 해주면 해당 x에 존재하는 인덱스들을 k를 움직이면서 하나씩 빼올수있다.
### 만약 U,D,R,L이 각각 1,2,4,8 인데 U|D를 하면 3이된다.
### 이걸 3&1<<0 ->1
###      3&1<<1 ->1
### k가 0,1일때에만 1을 반환하고 나머지를 0을 반환한다, 이걸 이용해서
### dx,dy를 U,D,R,L의 순서에 맞게 배치해주면 우리가 원하는 방향을 뽑아낼수 있다.




def cctv_blind_spot(x,y,dire,d):
    for k in range(4):
        if dire&1<<k:  ### 이 부분을 통해 어느 방향을 봐야하는지 알려준다.
            nx,ny=x,y
            while arr[nx][ny]!=6:
                b[nx][ny]+=d ### 그리고 그 방향으로 전부 검색을 한다.
                nx=nx+dx[k]
                ny=ny+dy[k]
#### 이부분은 CCTV를 어느방향으로 켰을때 안전구역을 확장시키는 용도로 한다. 그래서 6을 만나기전까지는 계속 뻗어나간다. 그리고 그 값을
#### d로 더하는 이유는 밑에서 설명하겠다.


def cctv_dfs(index=0): ### 이거는 cctv를 어느방향으로 볼지 정해주는 함수이다.
    global min_area
    if index==len(cctv_info): ### 재귀함수를 돌다가 index가 cctv 개수와 같아지면, 사각지대를 세주는 부분이다.
        cnt=0
        for ax in range(N+2):
            for ay in range(M+2):
                if b[ax][ay]==0:
                    cnt+=1
                if min_area<cnt: ### 계산량을 줄여주기 위해, 중간에 최소값보다 더 많은 사각지대가 발생하면 바로 멈추도록 했다.
                    break
        if min_area>cnt:
            min_area=cnt
        return



    x,y,cctv_number=cctv_info[index]  ### cctv_info에서 x,y값과 cctv 종류를 뽑아내준다.

    for i in cctv_view[cctv_number]:  ### 그러면 cctv_종류에 따라 cctv_view에 있는 방향을 가져와준다.
        cctv_blind_spot(x,y,i,1)  ## 한쪽방향으로 켜져있을때 그때를 검색해준다. 그때는 d를 +1을 해준다.
        cctv_dfs(index+1)        ### 그리고 그때 다음번 카메라가 켜져있는지를 재귀함수를 통해 반복해준다.
        cctv_blind_spot(x,y,i,-1)   ### 마지막으로 이 cctv를 무조건 어느 방향으로도 켜져있어야하기 때문에 초기화 시켜주기 위해서,
                                    ### 같은 방향으로 -1을 해준다.
                                    ### 즉 cctv 종류 1을 기준으로 하면 먼저 윗쪽 탐색을 하고 나면 그 부분을 지우고 다음번 동쪽을 탐색해야하기
                                    ### 때문에 초기화 시켜주는 작업을 해준것이다.


N,M=list(map(int,input().split()))
arr=[[6]*(M+2)]                           ### 행렬 값의 경계를 벗어나지않게 해주기 위해서 상하좌우로 벽을세워주었다.
for i in range(N):
    arr.append([6]+list(map(int,input().split()))+[6])
arr.append([6]*(M+2))
b=[[0]*(M+2) for _ in range(N+2)]
cctv_info=[] ### cctv_info에는 총 3가지의 정보가 들어간다. cctv의 위치좌표 x,y값과 cctv의 종류를 나타내준다.

for i in range(N+2):
    for j in range(M+2):
        if arr[i][j]==6:
            b[i][j]=1
        elif arr[i][j]>0:
            cctv_info.append([i,j,arr[i][j]])

min_area=999999999999
cctv_dfs()

print(min_area)