### 최소신장트리 ####
### 힙을 쓰면 key_list를 돌면서 최소값을 찾을 이유가 없다 자동적으로 
### heapq에서 pop을 쓰면 (a,b,c) 이렇게 있으면 a가 가장 작은 값을 반환해준다. 
### 그리고 hq가 다 쓸때까지 반복을 해주면 된다.
import heapq

T=int(input())


for tc in range(1,T+1):
    V,E = map(int,input().split())
    ajd = {i : [] for i in range(V+1)}
    for _ in range(E):
        n1,n2,w = map(int,input().split())
        ajd[n1].append([n2,w])
        ajd[n2].append([n1,w])
    INF = float('inf')
    mst = [False] * (V+1)
    key = [INF] * (V+1)
    # start_node = 0
    key[0] = 0
    hq = []
    heapq.heappush(hq,(0,0))   ### 앞에가 가중치 뒤에가 node
    result = 0

    while hq:

        k,node = heapq.heappop(hq)

        if mst[node]: ### 한번 방문했던 노드이면 다음으로 넘어간다.
            continue

        result += k  #### result에 가중치를 더해준다.
        
        mst[node]=True ### 방문을 했다고 표시한다.

        for next_node,we in ajd[node]:  ### 현재 노드에서 방문가능한 모든 노드들에 대해서 key_list를(현재 가지고 있는 가중치보다 현재노드에서 왔을때 가중치가 더 낮으면) 갱신을 해주고,
                                        ### 그리고 그 값들을 hq에 전부 집어넣어준다.
                                        ### 그러면 hq에는 key_list가 갱신될때마다 그때의 가중치와 노드정보를 전부 넣어주는데
                                        ### hq은 heapq 특성상 가중치가 가장 낮은것을 반환해주므로 크게 신경쓸 필요가 없다.
            if not mst[next_node] and key[next_node] > we:
                key[next_node] = we
                heapq.heappush(hq,(we,next_node))
    print('#{} {}'.format(tc,result))