T= int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]


for tc in range(1,T+1):
    N,M,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    new_arr = [[0]*(M+K) for _ in range(N+K)]
    start_time =[ [-1]*(M+K)  for _ in range(N+K)]
    d = K//2
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                new_arr[i+d][j+d] = arr[i][j]
                start_time[i+d][j+d] = 0
    
   ### 강사님 코드에서 중요한 것은 (흐른시간 - 생성된 시간)/ 생명력 을 나눴을때, 1보다 작으면 비활성 상태:
   ### 1보다 크고 2보다 작으면 활성상태
   ### 2보다 크거나 같으면 죽은상태인것만 확인해주면 된다.
    for hour in range(1,K+1):
        for x in range(d-hour//2, N+d+hour//2):
            for y in range(d-hour//2, M+d+hour//2):
                tmp = []
                if new_arr[x][y] == 0:
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0<=nx<N+K and 0<=ny<M+K:
                            if new_arr[nx][ny]>0 and (hour-start_time[nx][ny])/new_arr[nx][ny] >1:
                                tmp.append(new_arr[nx][ny])
                    if len(tmp)>0:
                        new_arr[x][y] = max(tmp)
                        start_time[x][y] = hour

    cnt = 0 
    for x in range(N+K):
        for y in range(M+K):
            if new_arr[x][y] >0 and (K-start_time[x][y])//new_arr[x][y]<2:
                cnt+=1
    print('#{} {}'.format(tc,cnt))

                        


            
