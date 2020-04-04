def bfs(st,en):
    visited[st]=1
    stack=[]     
    stack.append((st,0))  ### 몇칸을 거쳐서 가는지 구하는 것으로 cnt를 0으로 처음에 넣어준다.
    while stack:
        x,cnt=stack.pop(0)
        for i in graph[x]:
            if i==en:
                return cnt+1  ### 마지막에도 한칸 움직이는것이므로 cnt+1을 해준다/
            elif visited[i]==0:
                stack.append((i,cnt+1))   ### 만약에 방문한적이 없으며, 스택에 i와 cnt+1을 해서 저장해준다.
                visited[i]=1
    return 0  ## 다 돌아도 end에 못가는거면 연결이 안되어있는것이므로 0을 보내준다.




T=int(input())

for tc in range(1,T+1):
    V,E=map(int,input().split())
    graph=[[] for _ in range(V+1)]  ### 노드들을 저장해주기 위한거

    for i in range(E):
        x,y=map(int,input().split())
        graph[x].append(y)   ### 양방향이므로, 자식,부모노드 둘다에 저장해준다.
        graph[y].append(x)

    start,end=map(int,input().split())  ### 처음과 끝을 결정해준다.
    visited=[0]*(V+1)
    result=bfs(start,end)   ### bfs를 해준다.
    print('#{} {}'.format(tc,result))