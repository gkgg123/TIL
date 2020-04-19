T=int(input())


for tc in range(1,T+1):
    N,M,L=map(int,input().split())
    a=1
    graph=[[] for _ in range(N+1)]
    result=[0]*(N+1)
    while a*2<=N:
        if 2*a <=N:
            graph[2*a].append(a)
        if 2*a+1<=N:
            graph[2*a+1].append(a)
        a+=1
    for i in range(M):
        ind,val=map(int,input().split())
        result[ind]=val
    


    for ind in range(N,1,-1):
        if graph[ind]:
            result[graph[ind][0]]+=result[ind]


    print('#{} {}'.format(tc,result[L]))