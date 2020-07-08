import sys

sys.stdin=open('swea_1248_공통조상.txt','r')


T = int(input())


def find_parents(ind,temp):
    if graph_child[ind]:
        temp.append(graph_child[ind][0])
        return find_parents(graph_child[ind][0],temp)
    else:
        return temp

def find_childs(ind):
    result = 0
    for i in graph_parent[ind]:
        result += 1
        result += find_childs(i)
    
    return result



for tc in range(1,T+1):
    V,E,node_a,node_b = map(int,input().split())
    graph_child = [[] for _ in range(V+1)]
    graph_parent = [[] for _ in range(V+1)]
    arr = list(map(int,input().split()))

    for ind in range(E):
        parent,child = arr[2*ind],arr[2*ind+1]
        graph_child[child].append(parent)
        graph_parent[parent].append(child)


    node_a_parent = find_parents(node_a,[])
    node_b_parent = find_parents(node_b,[])
    common_parent = -1
    if len(node_a_parent) < len(node_b_parent):
        node_a_parent,node_b_parent = node_b_parent,node_a_parent
    for i in node_a_parent:
        for j in node_b_parent:
            if i == j:
                common_parent = i
                break
        if common_parent>0:
            break
    cnt = find_childs(common_parent) + 1
    print('#{} {} {}'.format(tc,common_parent,cnt))
