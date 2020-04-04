dx=[-1,1,0,0]
dy=[0,0,1,-1]

T=int(input())

for tc in range(1,T+1):
    N=int(input())
    arr=[list(input()) for _ in range(N)]
    stack=[]
    flag=False
    for i in range(N):
        for j in range(N):
            if arr[i][j]=='2':
                stack.append((i,j,0))
    while stack:
        x,y,cnt=stack.pop(0)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if arr[nx][ny]=='0':
                    arr[nx][ny]=1
                    stack.append((nx,ny,cnt+1))
                elif arr[nx][ny]=='3':
                    flag=True
                    stack.clear()
                    break
    
    if flag:
        print('#{} {}'.format(tc,cnt))
    else:
        print('#{} 0'.format(tc))