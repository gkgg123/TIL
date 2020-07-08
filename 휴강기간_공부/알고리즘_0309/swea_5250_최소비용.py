T = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    value = [[9999999]*N for _ in range(N)]
    visit = [[False]*N for _ in range(N)]
    value[0][0]=0
    result = 0
    cnt = 0
    pass_list = set()
    pass_list.add((0,0))
    while True:
        min_value = 99999999
        x,y = -1,-1
        for px,py in pass_list:
            if not visit[px][py] and min_value>value[px][py]:
                min_value = value[px][py]
                x,y = px,py
        visit[x][y] = True
        pass_list.remove((x,y))
        if (x,y) == (N-1,N-1):
            break
        visit[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and visit[nx][ny] == False:
                diff = arr[nx][ny]-arr[x][y]
                if diff<0:
                    diff = 0
                if value[nx][ny] > diff+1+value[x][y]:
                    value[nx][ny] = diff+1+value[x][y]
                    pass_list.add((nx,ny))


    print('#{} {}'.format(tc,value[N-1][N-1]))


