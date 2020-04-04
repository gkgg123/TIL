T=int(input())

for tc in range(1,T+1):
    N,M,L=map(int,input().split())
    arr=list(input().split())
    for _ in range(M):
        ind,val=map(int,input().split())
        arr.insert(ind,val)
    print('#{} {}'.format(tc,arr[L]))