    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    def bfs(x,y,cnt):
        stack=[]
        stack.append((x,y,cnt))
        while stack:
            ax,ay,cnt_n=stack.pop(0)
            for i in range(4):
                nx=ax+dx[i]  
                ny=ay+dy[i]
                if 0<=nx<N and 0<=ny<N:  ### 행렬 범위를 벗어나지 않으면서
                    if arr[nx][ny]=='0':   ### 0을 만나면 
                        arr[nx][ny]=9      ### 다시 안오게 값을 변화시켜주고,
                        stack.append((nx,ny,cnt_n+1))   ### cnt+1 해서 넣어준다.
                    elif arr[nx][ny]=='3':   ### 그리고 '3'을 만나면 cnt_n을 반환해준다.
                        return cnt_n
        return 0   ### 다 돌아도 못 만나는거면 연결이 안된것이므로 0을 반환해준다.


    T=int(input())


    for tc in range(1,T+1):
        N=int(input())
        arr=[list(input()) for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if arr[i][j]=='2':  #### '2'인곳을 찾아 bfs를 해준다, 그때의 좌표값 i,j와 몇칸 떨어져있는지 확인할 cnt용 0을 입력한다.
                    result=bfs(i,j,0)

        print('#{} {}'.format(tc,result))