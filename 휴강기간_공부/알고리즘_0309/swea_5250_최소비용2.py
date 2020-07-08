import heapq

T = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    value = [[999999999] * N for _ in range(N)]
    value[0][0]=0
    pass_list = []
    heapq.heappush(pass_list,(0,0,0))

    while True:
        cu_val,x,y = heapq.heappop(pass_list)
        visited[x][y] = True
        if (x,y) == (N-1,N-1):
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx <N and 0<=ny<N:
                if not visited[nx][ny]:
                    diff = arr[nx][ny]-arr[x][y]
                    if diff < 0:
                        diff = 0
                    if value[nx][ny] > diff+1+value[x][y]:
                        value[nx][ny] = diff+1+value[x][y]

                        heapq.heappush(pass_list,(value[nx][ny],nx,ny))
    print('#{} {}'.format(tc,value[N-1][N-1]))
