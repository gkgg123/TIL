import itertools
T=int(input())

for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for i in range(N)]
    b=itertools.permutations(range(N))
    result=0
    min_result=999999
    for k in b:
        result=0
        for i in range(N):
            result+=arr[i][k[i]]
            if result>min_result:
                break
        min_result=result

    print('#{} {}'.format(tc,min_result))
        