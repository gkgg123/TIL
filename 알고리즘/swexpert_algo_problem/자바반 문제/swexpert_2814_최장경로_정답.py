T=int(input())
### 재귀를 이용하여 풀었다.
def dfs(x,cnt):
    global max_cnt
    visited[x]=1
    if max_cnt<cnt:  ### cnt가 최장경로보다 길어지면, 바꿔준다.
        max_cnt=cnt
    for i in graph[x]:   ### graph에 있는 노드들을 꺼내
        if visited[i]==0:  ### 방문한적이 없으면
            dfs(i,cnt+1)   ### 방문을하고
            visited[i]=0   ### 초기화를 시켜준다.
        
    
                
 


for tc in range(1,T+1):
    N,M=list(map(int,input().split()))
    graph=[[] for _ in range(N+1)]
    max_cnt=1
    for i in range(M):
        x,y=list(map(int,input().split()))
        graph[x].append(y)                   ### 간선은 양방향이므로, 한쪽이 연결되어있으면 반대쪽으로도 연결되어있으니
        graph[y].append(x)                   ### 이런식으로 추가해줬다.

    for i in range(1,N+1):
        visited=[0]*(N+1)                    ### 각 노드들로 부터 출발하여, 가장 긴 경로를 찾아준다.
        dfs(i,1)                             ### 현재 인덱스와 최초 길이를 넣어준다.

    print('#{} {}'.format(tc,max_cnt))