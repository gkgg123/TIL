### 프림 알고리즘 ### 힙을 안쓰는거

T=int(input())


for tc in range(1,T+1):
    V,E = map(int,input().split())
    adj = {i : [] for i in range(V+1)}
    
    ### 무방향이므로, 양쪽에 전부 넣어준다.
    for i in range(E):
        n1,n2,w = map(int,input().split())
        adj[n1].append((n2,w))
        adj[n2].append((n1,w))


    INF = float('inf')
    ### 이 문제를 풀땐 parent_list는 필요없다. 노드가 어디로 연결되어있는지 저장해놓는 용도이다.
    parent_list = [-1]*(V+1)
    ### key_list는 현재 연결될수 있는 방법 중 최소 가중치이다. 처음에는 아무것도 없으므로, inf 로 초기화해준다.
    key_list = [INF]*(V+1)
    ### 그리고 0번 노드를 기준으로 찾을거라, 0번 노드의 key_list는 0 으로 해줬다.
    key_list[0] = 0 
    ### mst는 우리가 방문을 한 노드인지 아닌지 확인하는것이다.
    mst = [False] * (V+1)
    #### search_list는 기준점이 되는 노드의 정보를 넣어준다.
    search_list = []
    search_list.append((0,0))
    #### 그리고 전자는 가중치 후자는 node이다.
    result = 0 
    cnt = 0
    while cnt <V:
        key, node = search_list.pop()
        #### 현재 기준점이 되는 node와 key를 뽑아내준다.

        #### 현재 기준점이 되는 node를 다 탐색했을때 가장 작은 가중치를 가진 값을 찾기 위해
        #### current_min_key 와 그때의 node인 current_min_node가 필요하다.
        #### INF, -1로 초기화해준다.
        current_min_key = INF
        current_min_node = -1

        #### 그리고 node는 선택됬으므로 mst[node] = True로 바꿔준다.
        mst[node] = True
        
        
        ##### 기준점이 되는 node가 오면 먼저 key_list를 갱신해준다.
        for next_node, next_key in adj[node]:
            #### 현재 key_list에 있는 값보다 기준점이 되는 node에서의 key가 더 작으면 갱신을 해준다.
            if key_list[next_node] > next_key:
                parent_list[next_node] = next_node
                key_list[next_node] = next_key
        
        
        #### key_list를 갱신을 해주고 난뒤에 key_list를 전체를 조회하면서, 가장 작으면서 방문하지 않은 노드를 선택해준다.
        for ind in range(V+1):
            if current_min_key > key_list[ind] and not mst[ind]:
                current_min_key = key_list[ind]
                current_min_node = ind
        #### 그리고 최소 가중치를 result에 더해주고, search_list에 append 해준다.
        #### search_list를 안쓰고
        #### key = current_min_key
        #### node = current_min_node로 해줘도 된다.
        result += current_min_key     
        search_list.append((current_min_key,current_min_node))
        cnt+=1

    print('#{} {}'.format(tc,result))