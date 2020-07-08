### heapq를 이용하는 방법 ####

import heapq
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def heapq_bfs():
    q = []
    ### 거리, x,y
    heapq.heappush(q,(0,0,0))
    while q:
        #### dis가 가장 적은걸 자동적으로 반환해준다. 
        dis,x,y = heapq.heappop(q)
        ### 목적지에 도착하면 dis를 돌려준다.
        if x == N-1 and y == N-1:
            return dis
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            ### 4방향을 탐색하면서, 내가 방문한 노드를 제외한 나머지 노드들을 추가해준다.
            if 0<=nx<N and 0<=ny<N:
                if (nx,ny) not in visited:
                    visited.add((nx,ny))
                    heapq.heappush(q,(dis+arr[nx][ny],nx,ny))



T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,list(input()))) for _ in range(N)]
    visited =set()
    visited.add((0,0))


    result = heapq_bfs()


    print('#{} {}'.format(tc,result))