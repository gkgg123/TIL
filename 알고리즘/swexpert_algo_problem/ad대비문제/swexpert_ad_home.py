#### 홈방범 서비스 #####


def bfs(cu_x,cu_y,benefit,cu_pay):
    global dis
    home=0    
    for i in range(N):
        for j in range(N):
            temp=abs(i-cu_x)+abs(j-cu_y)
            ### 운영범위안인지를 판단해주는 것이다.
            if temp<=(cu_pay-1) and arr[i][j]==1:
            ### 운영 범위 안에 집이 있으면 집의 수를 추가 해주었다.
                home+=1
    result=home*benefit-dis[cu_pay]
    ## 그리고 구해진 home 의 수를 통해 이익을 계산하였다.
    if result>=0:
        ## 이 문제는 손해를 안 보는 것이다.
        ## 그래서 이익이 0원일때에도 home값을 return 해주었다.
        return home
    else:
        return 0


T=int(input())

for tc in range(1,T+1):
    N,M=list(map(int,input().split()))
    arr=[list(map(int,input().split())) for i in range(N)]
    dis=[0]*(N+2)
    ### dis는 운영 비용이다.
    for i in range(1,len(dis)):
        dis[i]=i**2+(i-1)**2
    ### dis에 문제에 주어진것처럼 운영비용들을 저장해놓았다.
    ### 여기서 N까지가 아닌 N+1까지의 운영비용을 저장해놓은 이유는
    ### N*N 행렬을 전부 감쌀수 있는 것은 N+1 크기의 운영영역이기 때문에
    ### N+1까지 만들어 놨다.    
    max_home=0
    for i in range(1,len(dis)):
        for x in range(N):
            for y in range(N):
                res=bfs(x,y,M,i)
                ### BFS 를 썻고 x,y는 좌표 M은 한 집당 얻을수 있는 수익 i는 서비스 범위이다.
                if max_home<res:
                    max_home=res
                #### 이 문제는 최대 이득을 구하는것이 아닌
                #### 손해를 보지않는 한에서 최대한 많은 집에 서비스를 하는것이기 때문에
                #### 홈의 갯수를 세는것이 중요하다.
    print('#{} {}'.format(tc,max_home))
