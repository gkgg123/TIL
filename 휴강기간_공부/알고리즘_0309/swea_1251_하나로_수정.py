### 프림 알고리즘을 이용(200ms대) ####

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))
    E = float(input())
    INF = float('inf')

    ### 방문을 했는지 확인하는 것이다.
    vistied = [False] * N

    ### 거리를 저장하기 위함이다.
    distance = [INF] * N

    ### 우리가 시작점으로 하는 0번섬은 0으로 초기화를 해준다.
    distance[0] =0

    ## cur_ind는 현재위치의 섬이고, next_ind는 다음위치의 섬이다. 
    cur_ind, next_ind = 0 , 0

    ### 이것도 프림알고리즘을 이용한 것으로, 앞서 4000ms대와 다르게 전체 거리를 계산해서 sort하는것이 아닌
    ### 단계단계별로 나가는것이다.
    for _ in range(N-1):
        ### stan은 현재 기준점이 되는 섬에서 다음섬까지의 거리를 비교하는 기준이다.
        stan = INF
        ### 현재섬은 이미 방문한 것이므로, 방문표시를 해준다.
        vistied[cur_ind] = True

        ### 그리고 나머지 섬에 대해서 for문을 돌린다.
        for ind in range(N):
            ### 만약 방문한 섬이라면 다음번으로 넘긴다.
            if vistied[ind]:
                continue
            ### 그리고 현재섬과 다른섬과의 거리를 구한다.
            temp = (x[cur_ind]-x[ind])**2 + (y[cur_ind]-y[ind])**2

            ### 그 거리가 현재의 distance보다 적으면 값을 교체해준다.
            if temp < distance[ind]:
                distance[ind] = temp

            ### 그리고 distance가 기준점이 되는 stan보다 작다면 바꿔주고, next_ind에 값을 넣어준다.
            if stan > distance[ind]:
                stan = distance[ind]
                next_ind = ind
        ## 그리고 현재섬을 next_ind로 바꿔준다.
        cur_ind = next_ind

    result = 0
    ### 그리고 이렇게 저장된 distance를 전부 더해준다.
    for i in range(N):
        result += distance[i]
    print('#{} {}'.format(tc,round(result*E))) 

