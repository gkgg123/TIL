#### 다른 사람 코딩 좋은거 ####


for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    stem = []
    board = {}
    ans = 0
 
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
 
    for y in range(N):
        for x in range(M):
            if matrix[y][x] > 0:
                #### 생명력, y,x 좌표 , 그리고 cnt는 바이러스의 상태를 알기 위한것이다.
                stem.append((matrix[y][x], y, x, 0))   ### stem은 바이러스가 퍼질걸 계속 하는 거
                board[(y, x)] = matrix[y][x]   #### 바이러스가 있는 위치를 board에 따로 관리했다.
                ans += 1

    for i in range(K):
        ### sort를 하면 바이러스의 생명력을 기준으로 오름차순으로 정렬되기 때문에 가장 뒤에서 빼면 가장 큰 생명력이다.
        stem.sort()
        new = []
        while stem:
            #### 생명력 y,x, cnt는  바이러스의 상태를 알기 위한 시간이다.
            vit, y, x, cnt = stem.pop()
            if cnt == vit: ### cnt 와 vit가 같아지면, 번식을 한다.
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if not board.get((ny, nx)):  ### 만약에 바이러스 목록에 없으면,
                        board[(ny, nx)] = vit  ### 현재 바이러스의 생명력을 추가해주고,
                        new.append((vit, ny, nx, 0))  ### 새로운 리스트에 추가해준다.
                        ans += 1
            cnt += 1
            if cnt == vit*2: ### 그리고 생명력이의 2배가 cnt가 되면 죽은거기때문에
                ans -= 1  ### 바이러스의 개수를 줄여준다.
            else: ### 그 외에는 살아있기 때문에 다시 새로운 new 목록에 넣어준다.
                new.append((vit, y, x, cnt))
        ### 교체해준다.
        stem = new
    print('#{} {}'.format(tc, ans))