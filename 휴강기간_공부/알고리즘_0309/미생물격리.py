### 처음에 리스트에 미생물을 저장하고,
### 딕셔너리로 중복위치의 미생물을 파악하고,
### 그걸 다시 리스트로 바꿔서 저장하던 방식을 개선했다.

T=int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
dire_reverse = [2,1,4,3]


def move(ar):
    ### 빈 딕셔너리를 만들어준다.
    temp={}
    for ind,val in ar.items():
        x = ind[0]
        y = ind[1]
        num = val[0]  ### 현재 미생물의 수
        dire = val[1]  ### 방향
        cu_init_num = val[2]  ### 초기 미생물의 수이다.
        nx = x+dx[dire-1]
        ny = y+dy[dire-1]

        if nx == 0 or nx == N-1 or ny ==0 or ny==N-1: ## 만약 끝에 닿았다면
            num = num//2   ### 수를 반절 줄이고,
            dire = dire_reverse[dire-1]  ### 방향을 반대로 바꾼다.
    
        if not temp.get((nx,ny)):
            ### 만약 해당 키에 해당하는 값이 없는 최초의 값이면
            ### num,dire,num으로 초기값을 넣어준다.
            temp[(nx,ny)] = [num,dire,num]
        else:
            ### 만약 이미 존재하는 값이 있으면, 그 값을 불러온다.
            prev_num,prev_dire,init_num = temp.get((nx,ny))
            ### 만약 이전에 존재하는 미생물의 초기값 init_num이 현재의 초기값 cu_init_num보다 높으면
            if init_num > cu_init_num:
                ##### 방향을  prev_dire 기준으로 하고, 미생물을 더해준다. 그리고 가장 끝의 초기값은 init_num을 넣어준다.
                temp[(nx,ny)] = [num+prev_num,prev_dire,init_num]
            else:
                ### 만약 현재 cu_init_num이 더 크면, 미생물을 더해주고, 현재 방향인 dire로 바꿔주고, 초기값을 cu_init_num을 해준다.
                temp[(nx,ny)] = [num+prev_num,dire,cu_init_num]

    ### 모든 과정이 끝나고, 인제 value값의 3번째인 init_num을 현재의 미생물의 값이 value의 1번째값으로 바꿔준다.
    ### 이렇게 하지 않을시, 합쳐진 미생물의 초기값으로 안바꿔져서 45번째까지밖에 통과를 못한다.
    for ind,val in temp.items():
        if val[0] != val[2]:  ### val[0] 과 val[2]가 같지 않다는것은 한번이라도 합쳐진 곳이기 때문에 
                              ### val[2]의 초기값을 바꿔준다.
            temp[ind]=[val[0],val[1],val[0]]

    return temp



for tc in range(1,T+1):
    N,M,K = map(int,input().split())

    arr = {}

    ### 딕셔너리로 각 (x,y) 좌표를 기준으로 값을 넣어준다. 미생물의 수, 방향, 미생물의 초기값
    for _ in range(K):
        temp = list(map(int,input().split()))
        arr[(temp[0],temp[1])] = [temp[2],temp[3],temp[2]]

    for i in range(M):
        ### M번 반복한다.
        arr = move(arr)
    
    total = 0
    #### arr의 value값을 가져와서 그 중 미생물 수만 더해준다.
    for i in arr.values():
        total+=i[0]
    print('#{} {}'.format(tc,total))
