
### 다익스트라 알고리즘 ###

T = int(input())



for tc in range(1,T+1):
    V,E = map(int,input().split())
    ### 노드들에 대한 정보를 저장해놓는다.
    adj = {i : [] for i in range(V+1)}
    for _ in range(E):
        ### 시작점, 끝점 , 가중치
        start,end,w = map(int,input().split())
        adj[start].append((end,w))
    


    INF = float('inf') 
    ### 처음 거리 리스트들을 전부 무한대로 초기화해준다.
    distance_list = [INF]*(V+1)
    ### 방문을 했는지 알기 위한 mst이다.
    mst = [True] * (V+1)
    #### 우리는 0번 노드에서 목표노드인 V 까지 가는것이므로
    ### 0번 노드의 distance를 0으로 초기화 해준다.
    distance_list[0] = 0 


    node = 0  ### 첫 노드가 0 이므로 node를 0으로 해줬다.
    result = 0 
    while node != V:
        ### 방문을 했으므로, False로 해준다.
        mst[node] = False
        

        ### 먼저 distance_list를 갱신해준다.
        ### 기존에 있던 distance_list의 값 distance_list[next_node]과 우회해서 오는 값 distance_list[node]+distance랑 비교를 해서 더 작은거로 갱신을 해준다.
        ### 0,1,2, 번 노드가 있다 하자.
        ### 0->1 2
        ### 0->2 5
        ### 1->2 1
        ### 우리가 0번 노드로 해서 distance_list를 해보면
        ### 처음에 [0 inf inf] 일것이다.
        ### 그리고 밑의 과정을 하면
        ### [0,2,5] 가 될것이다. 그러면 우리는 다음 노드로, 방문하지 않고 가중치가 가장 작은 1번 노드를 선택해줄것이다.
        ### 다음 노드 1번이 왔을때
        ### distance[2] 는 5인데
        ### distanc[1]+ 1 은 2이다.
        ### 0번 노드에서 1번 노드를 들리고 2번 노드를 가는게 더 가중치가 적으므로,
        ### 갱신을 해줘야한다.
        ### 더 자세한 설명 : https://mattlee.tistory.com/50
        for next_node,distance in adj[node]:
            distance_list[next_node] = min(distance_list[next_node],distance_list[node] + distance)
        

        ### distance_list를 갱신해주고 난뒤 distance_list 중 가장 작은 가중치 이면서, 방문하지 않은 노드를 구해준다.
        next_min_distance = INF
        next_min_node = -1

        for ind in range(V+1):
            if mst[ind] and next_min_distance > distance_list[ind]:
                next_min_distance = distance_list[ind]
                next_min_node = ind
        ### 그리고 다음노드를 가장 작은 가중치를 가졌던 노드로 바꿔준다.
        node = next_min_node

    #### 시작점을 기준으로 최단 경로를 해준 것이므로,
    #### 목적지 노드인 V를 넣어주면 된다.
    print('#{} {}'.format(tc,distance_list[V]))

