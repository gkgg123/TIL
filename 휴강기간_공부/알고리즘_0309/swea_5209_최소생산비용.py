T=int(input())

def dfs(cnt,total):
    global min_result
    if total> min_result:
        return
    if cnt == N-1:
        if min_result>total:
            min_result=total
            return


    if cnt+1 <N:
        for i in range(N):
            if visited[i] == -1:
                visited[i] = 1 
                dfs(cnt+1,total+arr[cnt+1][i])
                visited[i] = -1





for tc in range(1,T+1):
    N=int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]


    min_result = 999999999999
    for i in range(N):
        visited=[-1]*N
        visited[i]=1
        dfs(0,arr[0][i])
    print('#{} {}'.format(tc,min_result))
