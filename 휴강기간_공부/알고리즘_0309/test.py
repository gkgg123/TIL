from itertools import permutations

def factorial(n):
    global result
    if n == 1:
        return result
    else:
        return n * factorial(n-1)

def minBattery(state,count, roadN,battery): # 출발, 현재 횟수, 순열 전체리스트,용량
    global minResult, n
    if count == N:  ### 횟수가 전체 길이만큼 되면 판별
        if battery < minResult:
            minResult = battery
            return
    else:
        if battery >= minResult:
            return
        else:
            if count<N-1:  ### 마지막에서 두번째 전까지는 그대로 한다.
                minBattery(roadN[count],count+1,roadN,battery+N_N[state-1][roadN[count]-1])
            else:  ### 마지막에는 무조건 1하고 연결이 되니깐 따로 빼준다.
                minBattery(1,count+1,roadN,battery+N_N[state-1][0])

numbers = int(input())

for number in range(numbers):
    N = int(input())
    N_N = [list(map(int, input().split())) for i in range(N)]

    road = [i for i in range(2, N+1)]
    road_list = list(permutations(road, len(road)))
    result = 1
    minResult = 1000000000000
    for n in range(factorial(N-1)):
        for m in range(2, N+1):
            minBattery(1,0, road_list[n],0)

    print('#{} {}'.format(number+1, minResult))