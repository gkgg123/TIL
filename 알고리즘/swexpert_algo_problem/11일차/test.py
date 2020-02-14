import sys
import collections

sys.stdin=open('swexpert_daily11_stack01.txt','r')

def dfs():
    result=[]
    que=collections.deque()
    for k in range(1,V+1):
        if visit[k]==0:
            que.append(k)
    while que:
        node = que.popleft()
        result.append(node)
        for i in node_total[node]:
            visit[i]-=1
            if visit[i]==0:
                que.append(i)
    return ' '.join(map(str,result))
        



for tc in range(1,11):
    V,E=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    node_total=[[] for i in range(V+1)]
    visit=[0]*(V+1)

    for n in range(0,E*2,2):
        node_total[arr[n]].append(arr[n+1])
        visit[arr[n+1]]+=1
    print('#{} {}'.format(tc,dfs()))



    