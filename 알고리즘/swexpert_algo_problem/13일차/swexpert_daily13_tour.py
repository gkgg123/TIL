

def gababo(x,y):
    a=x-1
    b=y-1
    if arr[a]==arr[b]:
        return x
    else:
        if (arr[a]==1 and arr[b]==2) or (arr[a]==2 and arr[b]==3) or (arr[a]==3 and arr[b]==1):
            return y
        else:
            return x
    
def rec(st,end):
    if st==end:
        return st
    first=rec(st,(st+end)//2)
    second=rec((st+end)//2+1,end)
    return gababo(first,second)

T=int(input())

for tc in range(1,T+1):
    N=int(input())
    arr=list(map(int,input().split()))
    print('#{}'.format(tc),end=' ')
    print(rec(1,N))