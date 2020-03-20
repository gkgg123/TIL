
T=int(input())
### 실패 ####
def dfs(x,cnt):
    global max_cnt
    visited[x][x]=1
    st=[[x,cnt]]
    
    while st:
        a,cn=st.pop()
        
        for i in graph[a]:
            if visited[x][i]==0:
                st.append([i,cn+1])
                visited[x][i]=1
                break
        if max_cnt<cn:
            max_cnt=cn
 


for tc in range(1,T+1):
    N,M=list(map(int,input().split()))
    graph=[[] for _ in range(N+1)]
    max_cnt=1
    for i in range(M):
        x,y=list(map(int,input().split()))
        graph[x].append(y)
        graph[y].append(x)
    visited=[[0]*(N+1) for _ in range(N+1)]
    for i in range(1,N+1):        
        dfs(i,1)

    print('#{} {}'.format(tc,max_cnt))