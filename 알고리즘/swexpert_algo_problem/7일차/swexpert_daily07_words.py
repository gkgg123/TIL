T=int(input())
gx=[0,1]
sy=[1,0]
def garo_search(x,y):
    global x_temp    
    if 0<=y<N:
        if words[x][y]==0:
            if x_temp[0]>0:
                total_cnt.append(x_temp)
                x_temp=[0]
                garo_search(x,y+1)
            else:
                garo_search(x,y+1)
        else:
            x_temp[0]+=1
            garo_search(x,y+1)
    else:
        if x_temp[0]>0:
            total_cnt.append(x_temp)
            x_temp=[0]
def sero_search(x,y):
    global y_temp    
    if 0<=x<N:
        if words[x][y]==0:
            if y_temp[0]>0:
                total_cnt.append(y_temp)
                y_temp=[0]
                sero_search(x+1,y)
            else:
                sero_search(x+1,y)
        else:
            y_temp[0]+=1
            sero_search(x+1,y)
    else:
        if y_temp[0]>0:
            total_cnt.append(y_temp)
            y_temp=[0]


for tc in range(1,T+1):
    N,K=map(int,input().split())
    words=[list(map(int,input().split())) for i in range(N)]

    total_cnt=[]
    x_temp=[0]
    y_temp=[0]

    for i in range(N):        
        garo_search(i,0)
        sero_search(0,i)
    print('#{} '.format(tc),end='')
    cnt=0
    for i in total_cnt:
        if i[0]==K:
            cnt+=1
    print('{}'.format(cnt))
       
        



