T=int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
dire_reverse = [2,1,4,3]
def move(ar):
    temp={}
    result=[]
    for x,y,num,dire in ar:
        nx = x+dx[dire-1]
        ny = y+dy[dire-1]
        if nx == 0 or nx == N-1 or ny ==0 or ny==N-1:
            num=num//2
            dire = dire_reverse[dire-1]
        if not temp.get((nx,ny)):
            temp[(nx,ny)]=[]
            temp[(nx,ny)].append([num,dire])
        else:
            temp[(nx,ny)].append([num,dire])
    for location,value in temp.items():
        if len(value)>1:
            value.sort(key=lambda x: -x[0])
            sum_temp=0
            for i in value:
                sum_temp+=i[0]
            result.append([location[0],location[1],sum_temp,value[0][1]])

        else:
            result.append([location[0],location[1],value[0][0],value[0][1]])
    return result



for tc in range(1,T+1):
    N,M,K = map(int,input().split())

    arr = []
    for _ in range(K):
        temp = list(map(int,input().split()))
        arr.append(temp)

    for i in range(M):
        arr = move(arr)
    
    total = 0
    for i in arr:
        total+=i[2]
    print('#{} {}'.format(tc,total))