T=int(input())

#### 격자판의 숫자이어 붙이기 #####
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def dfs(x,y,re):
    if len(re)==7:
        result.add(re)
        ### 그리고 그 길이가 7이 되면 그 값을 result에 넣어주고
        ### return 하였다. 중복체크는 어차피 set함수가 해주므로
        ### result의 길이만 구해주면 갯수가 구해진다.
        return    
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<4 and 0<=ny<4:
            dfs(nx,ny,re+arr[nx][ny])
            ### dfs를 이용해 재귀를 돌리면서 값을 하나하나씩 더해나갔다.

for tc in range(1,T+1):
    arr=[list(input().split()) for i in range(4)]
    result=set()
    #### 이 문제는 중복되지 않는 숫자들을 구하는 것이다.
    #### 그리고 이 문제는 순서에 따라 숫자를 이어붙이는 것이기 때문에 int로 받아들이지않고 str 형태로 받아들었다.
    #### 그리고 중복되지않는것을 자동적으로 판별하기 위하여 set함수를 이용해 result를 만들었다.
    print(arr)
    for i in range(4):
        for j in range(4):
            dfs(i,j,'')
    print('#{} {}'.format(tc,len(result)))



