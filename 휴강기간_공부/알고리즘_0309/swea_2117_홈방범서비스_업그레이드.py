## 시간 줄인거


T=int(input())


for tc in range(1,T+1):
    N,M = map(int,input().split())

    house = []
    ### 집의 좌표를 house에 넣어준다.
    for i in range(N):
        temp = list(map(int,input().split()))
        for j in range(N):
            if temp[j]:
                house.append((i,j))

    home = 0  ## 최대 집의 수를 구하기 위함이다.

    ### i,j에 방범 서비스를 한다고 했을시, 거기서 각 집인 house 까지의 거리를 구하고, 
    ### 거리에 맞게 distance에 1씩 늘려준다.
    for i in range(N):
        for j in range(N):
            distance=[0]*(2*N)
            for x,y in house:
                distance[abs(i-x)+abs(j-y)+1]+=1

            ### 그리고 서비스 영역을 늘려준다. 서비스 영역은 최대 N+1 인데, N*N 행렬이라 할시 전부 서비스할수 있는 범위가 N+1이다.
            for k in range(1,N+2):
                ## 영역 k가 늘어날수록 k-1 영역도 포함해서 늘어나므로, 이전걸 더 해준다.
                distance[k]+=distance[k-1]
                #### res는 영역 k 내에 있는 서비스 집의 수이다.
                res = distance[k]
                #### 이익과 운영비용을 비교해서 손해를 보지 않으면,
                if res*M >= k*k+(k-1)*(k-1):
                    ### home과 res값 중 큰걸 저장해준다.
                    home = max(home,res)
    print('#{} {}'.format(tc,home))