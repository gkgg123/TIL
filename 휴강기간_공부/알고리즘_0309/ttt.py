
import heapq
T = int(input())

for tc in range(1,T+1):
    N = int(input())
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))
    E = float(input())
    INF = float('inf')
    vistied = [False] * N
    distance = [INF] * N
    hq = []
    distance[0] =0
    heapq.heappush(hq,(0,0))
    result = 0
    while hq:
        dis,ind = heapq.heappop(hq)
        if vistied[ind]:
            continue
        result += dis

        vistied[ind] = True
        for next_ind in range(N):
            if not vistied[next_ind]:
                temp = (x[ind]-x[next_ind])**2 + (y[ind]-y[next_ind])**2
                if distance[next_ind] > temp:
                    distance[next_ind] = temp
                    heapq.heappush(hq,(temp,next_ind))

    print('#{} {}'.format(tc,round(result*E)))
                
