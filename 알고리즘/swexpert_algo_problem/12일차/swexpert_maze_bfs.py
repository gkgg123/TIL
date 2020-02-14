import collections
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def bfs(n):
    q=collections.deque()
    q.append(n)
    while q:
        k=q.popleft()
        x=k//16
        y=k%16
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<16 and 0<=ny<16:
                if maze[nx][ny]==0 and visit[nx][ny]==-1:
                    q.append(16*nx+ny)
                    visit[nx][ny]=0
                elif maze[nx][ny]==3:
                    return 1
    return 0




for tc in range(1,11):
    input()

    maze=[list(map(int,list(input()))) for i in range(16)]
    visit=[[-1]*16 for i in range(16)]
    
    for i in range(16):
        for j in range(16):
            if maze[i][j]==2:
                result=bfs(16*i+j)
    print('#{} {}'.format(tc,result))