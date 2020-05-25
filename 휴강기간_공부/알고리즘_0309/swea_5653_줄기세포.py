T=int(input())
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for tc in range(1,T+1):
    N,M,K = map(int,input().split())
    cell_location={}

    for i in range(N):
        temp = list(map(int,input().split()))
        for j in range(M):
            if temp[j]:
                cell_location[(i,j)]=[]
                cell_location[(i,j)].append([temp[j],temp[j],0,0])
# 첫번째는 세포의 생명력
# 두번째는 활성가능 시간
# 세번째는 0 은 비활성화, 1은 활성화 -1은 죽은 세포
# 네번째는 최초로 들어온 시간
# 
    hour = 1
    while hour<=K:
        temp={}
        spread_list=[]
        for location,value in cell_location.items():
            value=list(*value)
            if value[1] -1 ==0:
                cell_location[location][0]=[value[0],value[1]-1,1,value[3]]                              
            elif value[1]-1 == -1:
                spread_list.append([location[0],location[1],value[0]])
                if value[0]+(value[1]-1) <= 0:
                    cell_location[location][0] = [value[0],value[1]-1,-1,value[3]]
                else:
                    cell_location[location][0] = [value[0],value[1]-1,value[2],value[3]]
            elif value[0]+(value[1]-1) <= 0:
                cell_location[location][0] = [value[0],value[1]-1,-1,value[3]]
            else:
                cell_location[location][0] = [value[0],value[1]-1,value[2],value[3]]
    
        for ax,ay,val in spread_list:
            for i in range(4):
                x=ax+dx[i]
                y=ay+dy[i]
                if not cell_location.get((x,y)):
                    cell_location[(x,y)]=[]
                    cell_location[(x,y)].append([val,val,0,hour])
                else:
                    prev = cell_location.get((x,y))[0]
                    pre_time = prev[3]
                    if prev[3]==hour:
                        if prev[0]<val:
                            cell_location[(x,y)]=[]
                            cell_location[(x,y)].append([val,val,0,hour])



        hour+=1
    result=0

    for ind,value in cell_location.items():
        value=list(*value)
        if value[2]>=0:
            result+=1

    print('#{} {}'.format(tc,result))


