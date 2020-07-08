T = int(input())
def union(parent,child):
    x = find_parent(parent)
    y = find_parent(child)
    make_set[y] = x
    ### 루트노드를 통일시켜주기 위함
    for i in range(N):
        if make_set[i] != i:
            make_set[i] = find_parent(make_set[i])
#### 부모를 찾아준다.
def find_parent(ind):
    if make_set[ind]== ind:
        return ind
    else:
        return find_parent(make_set[ind])


for tc in range(1,T+1):
    N = int(input())
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))
    E = float(input())
    make_set = [0] * N
    for i in range(N):
        make_set[i] = i

    node_total = []

    for i in range(N-1):
        for j in range(i+1,N):
            temp = (x[i] - x[j])**2 + (y[i] - y[j])**2
            node_total.append((temp,i,j))
    node_total.sort()
    cnt = 0
    result = 0
    while cnt < N-1:
        distance,x,y = node_total.pop(0)
        if make_set[x] != make_set[y]:
            union(x,y)
            result += distance
            cnt += 1

    print('#{} {}'.format(tc,round(result*E)))   