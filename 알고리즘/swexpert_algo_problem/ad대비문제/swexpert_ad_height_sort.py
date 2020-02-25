import sys
import collections

sys.stdin=open('height_sort.txt','r')

def bfs1(x):
    que=collections.deque()
    que.append(x)
    temp=[]
    while que:
        node=que.popleft()
        temp.append(node)
        for i in graph1[node]:
            if i not in temp and i not in que:
                visit[x]+=1       
                que.append(i)
    return
def bfs2(x):
    que=collections.deque()
    que.append(x)
    temp=[]
    while que:
        node=que.popleft()
        temp.append(node)
        for i in graph2[node]:            
            if i not in temp and i not in que:
                visit[x]+=1       
                que.append(i)
    return
 
T=int(input())
 
for tc in range(1,T+1):
    N=int(input())
    M=int(input())
    arr=[list(map(int,input().split())) for i in range(M)]
    graph1=[[] for i in range(N+1)]
    graph2=[[] for i in range(N+1)]
    for i in arr:
        graph1[i[0]].append(i[1])
        graph2[i[1]].append(i[0])
    visit=[0]*(N+1)
    for i in range(1,N+1):        
        bfs1(i)
        bfs2(i)
    cnt=visit.count(N-1)
    print('#{} {}'.format(tc,cnt))