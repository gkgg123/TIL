def dfs(x,y,sum_total):
    global total_min

    if x==N-1 and y==N-1:
        if sum_total<total_min:
            total_min=sum_total
            return
    if sum_total>=total_min:
        return
    else:
        if x+1<N:
            dfs(x+1,y,sum_total+arr[x+1][y])
        if y+1<N:
            dfs(x,y+1,sum_total+arr[x][y+1])


T=int(input())


for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    total_min=9999999
    visited=[[0]*N for _ in range(N)]
    dfs(0,0,arr[0][0])
    print('#{} {}'.format(tc,total_min))




