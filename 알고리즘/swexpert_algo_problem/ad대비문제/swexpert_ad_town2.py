### 창용 마을의 무리의 개수 ####

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
#### 

T=int(input())
for tc in range(1,T+1):
    N,M=list(map(int,input().split()))
    arr=[list(map(int,input().split())) for i in range(M)]
    graph=[[] for i in range(N+1)]

    for i in arr:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    ### 자식 노드의 부모노드를 추가해주지 않으면 ###
    ### 1
    ### 7 5
    ### 1 2
    ### 2 3
    ### 3 4
    ### 4 1
    ### 7 1
    ### 정답 : 3
    ### 출력 : 4 가 나온다.
    #### 왜냐하면 처음에 1은 방문을 했다고 했기 때문에 다시 안 찾아간다.
    #### 그래서 자식의 부모노드도 같이 추가를 해줘야지 이러한 불상사를 막는다.

    visit=[-1]*(N+1)
    ### 방문한 곳을 다시 안 찾아가기 위해 저장해놓은 곳이다.
    total=[0]
    for k in range(1,N+1):
        ### range를 1부터 N+1 까지 해주는 이유는 입력 중에 값이 없는 경우도 있다 즉
        ### 5 1
        ### 1 2
        ### 로 주어졌다고 했을때
        ### 주어진 간선만 검색할시 
        ### 출력이 1이 나올수 있다.
        ### 하지만 정답은 [1,2] [3] [4] [5] 로
        ### 총 4가 나와야하므로 1,N+1로 했다. 
        if visit[k]==-1:
            bfs(k)
    print('#{} {}'.format(tc,total[0]))

### 나중에 찾아보니 이 문제는 Union Find 라는 알고리즘을 써서 푸는게 정석적인 풀이였다. ###