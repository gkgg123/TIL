def dfs(start,cnt,su_to):
    global total_min
    if cnt==N:
        if su_to<total_min:
            total_min=su_to
            return
    elif cnt==N-1:
        dfs(1,cnt+1,su_to+arr[start][0])
    else:
        visited[start]=1
        if su_to>total_min:
            return
        else:
            for i in range(1,N):
                if visited[i]==0:
                    visited[i]=1
                    dfs(i,cnt+1,su_to+arr[start][i])
                    visited[i]=0



T=int(input())


for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]


    total_min=999999999
    visited=[0]*N
    dfs(0,0,0)

    print('#{} {}'.format(tc,total_min))