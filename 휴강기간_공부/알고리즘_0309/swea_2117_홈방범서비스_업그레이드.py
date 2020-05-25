T=int(input())


for tc in range(1,T+1):
    N,M = map(int,input().split())

    house = []

    for i in range(N):
        temp = list(map(int,input().split()))
        for j in range(N):
            if temp[j]:
                house.append((i,j))
    
    home = 0
    for i in range(N):
        for j in range(N):
            distance=[0]*(2*N)
            for x,y in house:
                distance[abs(i-x)+abs(j-y)+1]+=1
            for k in range(1,N+2):
                distance[k]+=distance[k-1]
                res = distance[k]
                if res*M >= k*k+(k-1)*(k-1):
                    home = max(home,res)
    print('#{} {}'.format(tc,home))