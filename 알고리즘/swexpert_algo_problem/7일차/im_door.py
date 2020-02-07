T=int(input())
dx=[0 ,0, 1, -1]
dy=[1 ,-1, 0, 0]
def search(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<N:
            if door[x][y]+1==door[nx][ny]:
                cnt[0]+=1
                search(nx,ny)

for tc in range(1,T+1):
    N=int(input())
    door=[list(map(int,input().split())) for i in range(N)]
    total=[]
    for row in range(N):
        for col in range(N):
            cnt=[0]
            search(row,col)
            total.append([door[row][col],cnt[0]])
    max_num=0
    max_ind=0
    for ind,val in total:
        if max_num<val:
            max_num=val
            max_ind=ind
        elif max_num==val and max_ind>ind:
            max_ind=ind
    print('#{} {} {}'.format(tc,max_ind,max_num+1))
            

