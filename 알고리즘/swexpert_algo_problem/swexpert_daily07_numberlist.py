T=int(input())


for tc in range(1,T+1):
    N,M=map(int,input().split())
    num_1=list(map(int,input().split()))
    num_2=list(map(int,input().split()))
    total=[]
    if N>M:
        for i in range(N-M+1):
            result=0
            for k in range(M):
                result+=num_1[k+i]*num_2[k]
            total.append(result)
    else:        
        for i in range(M-N+1):
            result=0
            for k in range(N):
                result+=num_2[k+i]*num_1[k]
            total.append(result)
    print(total)
    print('#{} {}'.format(tc,max(total)))
