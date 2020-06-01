#### 동적 계획법의 풀이

T = int(input())

def tsp(current,visited):
    if visited == (1<<(N+1))-1:
        return distance[current][N+1]
    
    areyouvisited = dp[current][visited] ## 너 여기 방문한적 있니??
    ### 0이 아니면 방문한 적이 있으므로, 되돌아간다.
    if areyouvisited != 0:
        return areyouvisited
    min_value = 999999999999999999
    for next_ind in range(1,N+1):
        if visited & (1<<next_ind) == 0:
            min_value = min(min_value,tsp(next_ind,visited|(1<<next_ind))+distance[current][next_ind])
    dp[current][visited] = min_value
    return min_value
    



for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    distance = [[0]*(N+2) for _ in range(N+2)]
    new_arr = []
    new_arr.append([arr[0],arr[1]])

    
    for i in range(2,N+2):
        new_arr.append(arr[2*i:2*(i+1)])

    new_arr.append([arr[2],arr[3]])



    dp = [[0]*(1<<(N+1)) for _ in range(N+2)]

    for i in range(N+2):
        for j in range(N+2):
            x,y = new_arr[i]
            nx,ny = new_arr[j]
            distance[i][j] = abs(x-nx) + abs(y-ny)


    print('#{} {}'.format(tc,tsp(0,1)))

