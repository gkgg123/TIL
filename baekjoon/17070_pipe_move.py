#### 파이프 옮기기 최초 시도 방법 ###
### 재귀 함수를 이용했다.
### 하지만 어떤 방법을 쓰더라도, 재귀함수를 이용해서 pypy3,python3를 통과할수 없었다.
### 찾아보니 c,c++,java는 재귀함수를 쓰더라도 통과가 가능하지만, 파이썬은 불가능했다.

### MOVE에 가로, 세로, 대각선 이동에 대하여 저장해 놓았다.

move=[[0,1],[1,0],[1,1]]

#가로=0
#세로=1
#대각선=2
##st=0 m=0 ->st=0
##st=0 m=2 ->st=2
##st=1 m=1 ->st=1
##st=1 m=2 ->st=2
##st=2 m=0 ->st=0
##st=2 m=1 ->st=1
##st=2 m=2 ->st=2
### st는 현재 파이프의 방향을 나타내고, m은 이동방향을 나타낸다.
### 보시다 시피 m의 값에 따라 다음 st의 값이 정해진다.
def pipe(x,y,st):
    global N
    global result
    if x==N-1 and y==N-1:
        ### 최종 위치에 도착하면 result값을 1씩 올려주어 모든 경우의수를 구해주었다.
        result+=1
        return
    for m in range(3):
        nx=x+move[m][0]
        ny=y+move[m][1]
        if (st==0 and m==1) or (st==1 and m==0):
            continue
            ### 가로 방향으로 있을때 세로방향으로 이동을 못하고, 세로방향으로 있을때 가로방향으로 이동하지 못하는것을 구현해주었다.
        if 0<=nx<N and 0<=ny<N:
            if arr[nx][ny]==0 and m!=2:
                pipe(nx,ny,m)
                #### 대각선 방향을 제외한 나머지를 재귀함수를 돌린것이다.
            elif arr[nx][ny]==0 and m==2 and arr[nx-1][ny]==0 and arr[nx][ny-1]==0 and 1<=nx<N+1 and 1<=ny<N+1 :
                pipe(nx,ny,m)
                ### 대각선일때는 파이프에 걸리면 안되는 구간들이 있어서 조건들이 더 추가되었다.





N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]

result=0
pipe(0,1,0)
print(result)