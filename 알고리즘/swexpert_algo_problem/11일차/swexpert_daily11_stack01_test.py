import collections
import sys
sys.stdin=open('swexpert_daily11_stack01.txt','r')
def bfs():
    result=[]
    q=collections.deque()
    for i in range(1,V+1):
        if cnt[i]==0:
            q.append(i)
    while q:
        node=q.popleft()
        result.append(node)
        for i in graph[node]:
            cnt[i]-=1
            if cnt[i]==0:
                q.append(i)
    return result


for tc in range(1,3):
    V,E=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    graph=[[] for i in range(V+1)]
    cnt=[0]*(V+1)
    for i in range(0,E*2,2):
        graph[arr[i]].append(arr[i+1])
        cnt[arr[i+1]]+=1
    print(bfs())
