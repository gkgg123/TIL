T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    arr=list(map(int,input().split()))
    t=M%N
    print('#{} {}'.format(tc,arr[t]))