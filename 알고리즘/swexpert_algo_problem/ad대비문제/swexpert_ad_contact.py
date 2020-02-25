import sys
import collections
sys.stdin=open('contact.txt','r')
### 10일차 contact#####
def bfs(st):
    que=collections.deque()
    que.append(st)
    while que:
        node=que.popleft()
        pre_visit=visit[node]
        for i in graph[node]:
            if visit[i]==0:
                que.append(i)
                visit[i]+=pre_visit+1
                ### 이 부분이 평소 visit하고 다른 부분이다. 원래 visit을 값을 변화시키거나 했지만
                ### 여기에서는 이전 방문한 노드의 visit 횟수에 1을 추가하여 여기가 제일 스타트 위치에서 얼마나 떨어져있는지
                ### 알게 해줬다.
    return 0
    

for tc in range(1,11):
    N,start=list(map(int,input().split()))
    cal=list(map(int,input().split()))
    graph=[[] for i in range(101)]
    for i in range(0,N,2):
        graph[cal[i]].append(cal[i+1])

    ### 해당 문제는 bfs로 풀었고, 자식 노드들의 위치를 graph에 저장을 해놨다.
    visit=[0]*101
    ### 한번 방문한 곳은 다시 방문하지 않기 위해 visit을 썼으면 최종 이동거리를 저장하기 위해 visit을 썼다.
    bfs(start)
    max_value=0
    max_index=0
    for v in range(len(visit)-1,-1,-1):
        if visit[v]>max_value:
            max_value=visit[v]
            max_index=v
    print('#{} {}'.format(tc,max_index))