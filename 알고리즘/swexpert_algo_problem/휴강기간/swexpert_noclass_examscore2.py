T=int(input())

for tc in range(1,T+1):
    N=int(input())
    arr=list(map(int,input().split()))
    Dp=[False]*10001
    Dp[0]=True

    
    temp=0
    for i in range(N):
        temp+=arr[i]
        for j in range(temp,-1,-1):
            if Dp[j]:
                Dp[j+arr[i]]=True

    result=Dp.count(True)
    print('#{} {}'.format(tc,result))