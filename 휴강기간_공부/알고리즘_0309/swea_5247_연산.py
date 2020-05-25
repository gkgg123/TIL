from collections import deque

T=int(input())

def find_number(N,cnt):
    q =deque()
    q.append([N,0])

    while q:
        number,cnt = q.popleft()
        if number >1000000 or number<0:  ### 범위를 넘어가는건 세줄 필요가 없다.
            continue
        if number == M : ### bfs이므로 같은 깊이를 탐색하므로 가장 먼저 온 게 가장 낮은 깊이를 가진 것이다. 그래서 반환해주면 끝
            return cnt
        if visited[number]: ### 한번도 방문하지 않은곳이면 4개의 연산을 해준다.
            cnt+=1
            q.append([number+1,cnt])
            q.append([number-1,cnt])
            q.append([number*2,cnt])
            q.append([number-10,cnt])
            visited[number]=False  ### 그리고 방문했다는 표시를 해준다.




for tc in range(1,T+1):
    N,M =map(int,input().split())
    visited = [True] * 1000001  ### 한번 연산한 곳은 안찾기 위함. 
    cnt = find_number(N,0)
    print('#{} {}'.format(tc,cnt))