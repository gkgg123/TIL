T=int(input())

for tc in range(1,T+1):
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    result=[0]*N
    for tes in B:
        for ind,val in enumerate(A):
            if val<=tes:
                result[ind]+=1   ### B의 값과 가장 가깝게 만나는 곳에 result+1을 해주고 그 때 break를 해주었다.
                break
    max_value=0
    max_index=0
    for k,t in enumerate(result):  ### 그리고 그 결과에서 가장 큰 인덱스 값을 구해줬따.
        if max_value<t:
            max_value=t
            max_index=k+1

    print('#{} {}'.format(tc,max_index))

