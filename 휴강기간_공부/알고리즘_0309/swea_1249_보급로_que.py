#### deque를 이용한 방법


from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    q = deque()
    q.append((0,0))

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            ### 4방향을 탐색한다.
            if 0<= nx < N and 0<= ny <N:
                ### 다음위치의 누적거리가 현재위치의 누적거리+현재위치에서 다음위치의 거리를 더해준것보다 클시
                ### 값을 바꿔주면서 q에 append를 해준다.
                ### 모든 작업이 끝나면 모든 distance 행렬에는 0,0에서 걸리는 최단거리가 나온다.
                if distance[nx][ny] > distance[x][y] + int(arr[x][y]):
                    distance[nx][ny] = distance[x][y] + int(arr[x][y])
                    q.append((nx,ny))




T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    ### 누적거리를 저장하기 위한 행렬이다.
    distance = [[1000000] * N for _ in range(N)]
    ### 우리는 무조건 0,0에서 시작을한다.
    distance[0][0] = 0
    bfs()
    print('#{} {}'.format(tc,distance[N-1][N-1]))
