import sys
import collections
sys.stdin=open('town.txt','r')
def bfs(x):
    que=collections.deque()
    que.append(x)
    visit[x]=0
    while que:
        node=que.popleft()
        for i in graph[node]:
            if visit[i]==-1:
                que.append(i)
                visit[i]=0
    total[0]+=1
    return
T=int(input())
for tc in range(1,T+1):
    N,M=list(map(int,input().split()))
    arr=[list(map(int,input().split())) for i in range(M)]
    graph=[[] for i in range(N+1)]

    for i in arr:
        graph[i[0]].append(i[1])
    visit=[-1]*(N+1)
    total=[0]
    for k in range(1,N+1):
        if visit[k]==-1:
            bfs(k)
    print('#{} {}'.format(tc,total[0]))