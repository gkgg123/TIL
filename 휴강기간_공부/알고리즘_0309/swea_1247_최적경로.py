T = int(input())

def path(cur,cnt,value):
    global min_result
    px,py = arr[cur][0],arr[cur][1]


    if value > min_result:
        return
    if cnt == N:
        dis = abs(arr[1][0]-px) + abs(arr[1][1]-py)
        if value + dis < min_result:
            min_result = value +dis
            return

    for i in range(2,N+2):
        x,y = arr[i][0],arr[i][1]
        dis = abs(px-x)+abs(py-y)
        if not visited[i]:
            visited[i] = True
            path(i,cnt+1,value+dis)
            visited[i] = False

    




for tc in range(1,T+1):
    N = int(input())
    arr = []

    temp = list(map(int,input().split()))
    for i in range((N+2)):
        arr.append(temp[2*i:2*(i+1)])
    min_result = 999999999999999
    visited = [False]*(N+2)
    visited[0] = True
    path(0,0,0)
    print('#{} {}'.format(tc,min_result))