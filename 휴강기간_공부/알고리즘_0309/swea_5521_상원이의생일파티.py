T = int(input())

def find():
    global cnt
    q = []
    visited[1] = False
    q.append((1,0))

    while q:
        ind,dep = q.pop(0)
        if dep < 2:
            for i in graph[ind]:
                if visited[i]:
                    visited[i] = False
                    cnt += 1
                    q.append((i,dep+1))

for tc in range(1,T+1):
    N,M = map(int,input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    cnt = 0
    visited = [True]*(N+1)
    find()
    print('#{} {}'.format(tc,cnt))