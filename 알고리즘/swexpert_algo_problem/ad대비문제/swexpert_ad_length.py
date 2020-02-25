T=int(input())

#### 방향전환####
for tc in range(1,T+1):
    map_list=list(map(int,input().split()))
    start=map_list[0:2]
    end=map_list[2:]
    result=0
    length=abs(start[0]-end[0])+abs(start[1]-end[1])
    max_len=max(abs(start[0]-end[0]),abs(start[1]-end[1]))
    if length%2==0:
        result=max_len*2
    else:
        result=max_len*2-1

    print('#{} {}'.format(tc,result))

#### 방향 전환은 쉬운 공식이 있었다.
### 시작점의 x,y를 x0 y0 로 하고 도착점의 좌표를 x1,y1이라 했을때
### abs(x0-x1)를 abs(y0-y1) 더한 값이 짝수 이면,
### 두개중 큰 수의 2배만큼 이동하면 되는것이었다.
### 그리고 만약의 홀수라면
### 두개 중 큰수의 2배만큼 이동하고, 1을 빼주면 되는 문제였다.
### 하지만 파이썬으로 제출할 수 없어서 제출을 못했다. 그래서 틀릴수도 있다.