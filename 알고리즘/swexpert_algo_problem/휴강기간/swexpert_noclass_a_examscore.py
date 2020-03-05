T=int(input())
def dfs(k=0):
    s=[[0,0]]

    while s:
        cnt,temp=s.pop()
        if cnt==N:
            result.add(temp)
        else:
            for i in range(2):
                temp2=temp+arr[cnt]*i
                s.append([cnt+1,temp2])
                



for tc in range(1,T+1):
    N=int(input())
    arr=list(map(int,input().split()))

    visited=[0]*N
    result=set()
    dfs()
    print('#{} {}'.format(tc,len(result)))