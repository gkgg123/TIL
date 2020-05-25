## 크루스칼 알고리즘 


### 같은 그룹 만들어주기
def union(parent,child):
    x = find_parent(parent)
    y = find_parent(child)
    make_set[y] = x

    ### 루트노드를 통일시켜주기 위함
    for i in range(V+1):
        if make_set[i] != i:
            make_set[i] = find_parent(make_set[i])

#### 부모를 찾아준다.
def find_parent(ind):
    if make_set[ind]== ind:
        return ind
    else:
        return find_parent(make_set[ind])


T=int(input())


for tc in range(1,T+1):
    V,E = map(int,input().split())
    node_total = []
    #### 노드를 전부 집어넣어주기 위한 리스트
    for i in range(E):
        parent,child,weight = map(int,input().split()) 
        node_total.append((parent,child,weight))
    ### 리스트를 가장 작은걸로 정렬해준다.
    node_total.sort(key=lambda x: x[2])
    #### 각 노드들의 루트 노드(최상위 부모노드) 를 저장해주기 위한 리스트
    make_set = [0]*(V+1)
    ### 각 노드들로 make_set을 초기화 해줌
    for i in range(V+1):
        make_set[i]=i
    ### cnt는 횟수 result는 총 결과    
    cnt = 0
    result = 0
    ### N개의 노드가 있으면 연결하는 간선의 개수는 N-1개 이다. 그래서 V 전까지만 한다.
    while cnt<V:
        #### 가장 작은걸 꺼내오므로 pop 0 을 해준다.
        p1,p2,weight = node_total.pop(0)
        ### 둘의 루트노드라 다르면, 두개가 다른 집합인것이므로, 사이클이 생기지 않는다.
        if make_set[p1] != make_set[p2]:
            #### 그래서 두개를 union 해주고, 가중치를 넣어주고, 횟수를 추가해준다.
            union(p1,p2)
            result += weight
            cnt += 1
    print('#{} {}'.format(tc,result))