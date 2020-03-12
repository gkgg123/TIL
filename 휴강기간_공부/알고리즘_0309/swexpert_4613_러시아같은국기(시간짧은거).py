

T = int(input())
for tc in range(1, T + 1):
    N, M= map(int, input().split())
    color = [[0, 0, 0] for _ in range(N)]
    for n in range(N):
        temp = list(map(str, input()))          ### 이 과정은 각 줄 마다의 W,B,R의 개수를 센 것이다.
        for m in range(M):
            if temp[m] == 'W':
                color[n][0] += 1
            elif temp[m] == 'B':
                color[n][1] += 1
            else:
                color[n][2] += 1
    result = 2501
    for w in range(0, N-2):             ##### 여기서는 WHITE가 몇줄까지 해줄것인지 정해주는것이다.
        for r in range(N - 1, w, -1):   #### RED의 시작줄수를 정해준 것이다.
            res = 0
            for b in range(0, N):       #### 이 부분은 BLUE를 나타낸 것이다. 
                if b <= w:              #### BLUE가 WHITE 마지막 줄수보다 작을때에의 WHITE의 개수를 세준다.
                    res += color[b][0] 
                elif b >= r:            #### BLUE가 RED의 시작 줄수보다 크게 되면 그 부분부터 RED인 것이다.
                    res += color[b][2]  #### RED의 개수를 세준다.
                else:                   #### 그리고 나머지가 BLUE의 위치인것이다.
                    res += color[b][1]
            result = min(result, M * N - res)  ### 전체 행렬에서 res 즉 자리에 맞는 색깔을 빼주면 바뀌어야할 색깔을 알수 있다.
    print(f'#{tc} {result}')                   ### 예를 들면 만약 5개의 행렬이 있고 w,b,r이 각각 1,2,2 이라 하면
                                               ### 위의 for문에서 w가 0, r이 3이다.
                                               ### 실제로 전체에서 w가 마지막 줄의 index가 0이고, red의 시작 index는 3이다.
                                               ### b<=w 인 경우는 0이고,
                                               ### b>=r 인 경우는 3,4 이다.
                                               ### 그러면 나머지 1,2 는 자동적으로 blue가 선택된것이다.
                                               ### 이러한 점을 이용해 계산시간을 줄여서 푸는 방식이다.