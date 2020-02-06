T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    li=[list(map(int,input().split())) for i in range(N)]
    result=[]
    total=0
    for i in range(N-M+1):
        for j in range(N-M+1):
            total=0
            for k in range(M):
                for t in range(M):
                    total+=li[i+t][j+k]
            result.append(total)
    print('#{} {}'.format(tc,max(result)))
        
        
