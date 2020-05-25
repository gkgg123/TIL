#### 꼼수 방법 #####


T=int(input())
def find_set(num):
    visited[num]=1  ### 들어오면 방문을 했다고 표시한다.

    for next_ind in graph[num]:  ### 그리고 그 그래프 내에 있는 값을 끄집어내어,
        if visited[next_ind]==0: ### 방문을 안했으면,
            find_set(next_ind)   ### 다 방문을 해준다.
    




for tc in range(1,T+1):
    N,M = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    visited = [0]*(N+1)  ### 방문을 표시
    arr = list(map(int,input().split()))
    for i in range(M):
        x = arr[2*i]
        y = arr[2*i+1]
        graph[x].append(y)  ### 부모 자식노드에 둘다 추가해준다.
        graph[y].append(x)
    cnt = 0
    for i in range(1,N+1):
        if graph[i] and visited[i]==0:  ### 방문하지 않았고, graph가 있으면 탐색을 한다.
            find_set(i) 
            cnt+=1           ### 한번 들어오면 연결된 모든 노드를 탐색하기 때문에 그게 한 집합이 된다. 그래서 +1 을 해준다.
        elif not graph[i]:  ### graph에 아무것도 없으면 단독노드이므로 +1 을 해준다.
            cnt+=1
    print('#{} {}'.format(tc,cnt))