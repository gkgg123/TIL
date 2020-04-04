from collections import deque


# 선택된 궁수 3명의 위치로 디펜스 시작
def defense():
    global max_count, enemy_count
    count = 0
    copy_position = enemy_position.copy()
    enemy = enemy_count
    attack = set()
    kill = [[0] * M for _ in range(N)]
    archer_row = N - 1
    # 적이 없어질때까지 반복
    while enemy > 0:
        # 궁수의 위치(성) 바로 앞에서부터 BFS로 사정거리 내에 적이 있는지 확인
        for archer in archers:
            Q = deque()
            visit = {}
            Q.append((archer_row, archer, 1))
            visit[(archer_row, archer)] = 1
            while Q:
                x, y, d = Q.popleft()
                if d > D:
                    break
                # 공격할 적 저장
                if arr[x][y] == '1' and not kill[x][y]:
                    attack.add((x, y))
                    break
                for dx, dy in delta:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx and 0 <= ny < M:
                        if visit.get((nx, ny)):
                            continue
                        Q.append((nx, ny, d + 1))
                        visit[(nx, ny)] = 1
        # 공격으로 적 없애기
        for x, y in attack:
            enemy -= 1
            count += 1
            kill[x][y] = 1
            copy_position.remove((x, y))
        attack.clear()
        temp = set()
        # 적들 성 앞으로 한칸씩 이동
        for x, y in copy_position:
            if x == archer_row:
                enemy -= 1
            else:
                temp.add((x, y))
        archer_row -= 1
        copy_position = temp.copy()
    if max_count < count:
        max_count = count
        print(archers,count)


# 조합으로 궁수 3명의 위치 잡기
def castle(k, s):
    if k == 3:
        defense()
    else:
        for p in range(s, M):
            archers[k] = p
            castle(k + 1, p + 1)


# 입력받기
N, M, D = map(int, input().split())
enemy_position = set()
delta = ((0, -1), (-1, 0), (0, 1))
arr = []
enemy_count = 0
max_count = 0
archers = [0] * 3
# 맵 정보 받으면서 적 위치 및 적 숫자 확인
for i in range(N):
    arr += [input().split()]
    for j in range(M):
        if arr[i][j] == '1':
            enemy_position.add((i, j))
            enemy_count += 1
if enemy_count:
    castle(0, 0)
print(max_count)
