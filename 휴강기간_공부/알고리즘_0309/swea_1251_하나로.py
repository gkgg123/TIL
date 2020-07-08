import sys
sys.stdin = open('swea_1251_하나로.txt','r')

### 프림 알고리즘 활용법 4000ms 대 ####


T = int(input())


for tc in range(1,T+1):
    N = int(input())

    ### x,y 좌표로 나눠서 받았다. 
    island_x = list(map(int,input().split()))
    island_y = list(map(int,input().split()))
    ### 그리고 섬의 좌표를 번호에 따라 저장하기위해 N의 크기만큼 따로 만들어줬다.
    island = [[] for _ in range(N)]

    for i in range(N):
        x,y = island_x[i],island_y[i]
        island[i] = [x,y]
    ### 섬끼리의 길이를 저장하기위함이다.
    distance = []
    for i in range(N-1):
        for j in range(i+1,N):
            temp = ((island[i][0]-island[j][0])**2 + (island[i][1]-island[j][1])**2 )
            distance.append([temp,i,j])

    ### E를 받아들인다.
    E = float(input())
    ### distance를 거리를 기준으로 오름차순으로 정렬해준다.
    distance.sort()

    ### N개의 섬이 연결되어있는지 확인하는 리스트이다.
    conneted_list=[0] * N
    ### 시작점을 0번섬으로 시작할것이기 때문에, 0번섬은 1로 체크를 해준다.
    conneted_list[0] = 1
    ### 최종결과를 저장하기 위함이다.
    result = 0
    #### connented_list가 전체 N하고 같아지기 전까지 계속 반복한다.
    while sum(conneted_list) != N:
        ### distance라는 리스트에서 하나하나 뽑아서 dis: 거리 , start : 시작섬 end : 연결된 섬
        for dis,start,end in distance:
            ### 프림 알고리즘에서 선택된 섬을 기준으로 연결된 섬중에 가장 짧은 거리를 고르는걸 기준으로 한다.
            if conneted_list[start] or conneted_list[end]:
                ### 그래서 start,end 둘중 하나라도 connented가 되어있어야하고,
                if conneted_list[start] and conneted_list[end]:
                    ### 둘다 연결되어있으면, 이미 연결된것이므로, 넘어간다.
                    continue
                else:
                    ### 그렇지 않다면 최소거리가 들어온것이므로, 둘다 연결 표시를 해주고,
                    conneted_list[start] = 1
                    conneted_list[end] = 1
                    ### 거리를 더해주고, 다시 처음부터 검색하기 위해 break로 빠져나가준다.
                    result += dis
                    break
    ### 그렇게 구한 결과 result에 E를 곱하고 반올림 round를 해준다.
    print('#{} {}'.format(tc,round(result*E)))


            