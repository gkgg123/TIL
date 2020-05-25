
#### 강의대로 푼 방식 


T=int(input())


def union(parent,child):
    x = find_parent(parent)  ### 부모노드의 부모를 찾아서 가져와준다.
    y = find_parent(child)   ### 자식노드의 부모를 가져와준다.
    ######### 그리고 자식노드의 부모노드를 저장해주는 값에 parent의 부모 값으로 바꿔준다.
    make_set[y]=x

def find_parent(ind):
    if make_set[ind] == ind:  ### ind와 부모노드가 같으면 최상위 부모노드이므로 그 값을 반환해준다.
        return ind
    else:
        return find_parent(make_set[ind])  ### 그게 아니면 최상위노드를 찾아준다.


for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    make_set=[0]*(N+1) ### 강의에서 말했던 make_set 처음에 자신을 부모로 가지게 만들어준다.
    for i in range(1,N+1):
        make_set[i]=i
   ##### 해당 노드의 부모노드를 바꿔주는 과정인 union을 해준다.
    for i in range(M):
        x= arr[2*i]
        y=arr[2*i+1]
        union(x,y)
    cnt = 0
    for i in range(1,N+1):
        if make_set[i]==i:  ### ind와 부모노드가 같으면 그게 해당집합의 최상위 부모노드이므로 그 개수를 세준다.
            cnt+=1

    print('#{} {}'.format(tc,cnt))
