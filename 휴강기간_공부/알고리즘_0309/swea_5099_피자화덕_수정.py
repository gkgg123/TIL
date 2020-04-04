import sys
sys.stdin=open('5099.txt','r')

T=int(input())

for tc in range(1,T+1):
    N,M=map(int,input().split())
    pizza=list(map(int,input().split()))
    arr=pizza[:N]
    arr_index=list(range(N))
    ind=N
    result=0
    while True:
        for i in range(N):
            if arr[i]==0:
                continue
            else:
                arr[i]=arr[i]//2
                if arr[i]==0:
                    if ind<M:
                        arr[i]=pizza[ind]
                        result=arr_index[i]+1
                        arr_index[i]=ind
                        ind+=1
                    else:
                        result=arr_index[i]+1
        if sum(arr)==0:
            break           
         
    print('#{} {}'.format(tc,result))
    