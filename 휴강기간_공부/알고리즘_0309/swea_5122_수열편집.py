from collections import deque

T=int(input())
for tc in range(1,T+1):
    N,M,L=map(int,input().split())
    qu=deque()
    arr=list(map(int,input().split()))

    qu.extend(arr)
    for _ in range(M):
        doit=list(input().split())
        if doit[0]=='I':
            qu.insert(int(doit[1]),doit[2])
        elif doit[0]=='D':
            del qu[int(doit[1])]
        else:
            qu[int(doit[1])]=doit[2]
    print('#{} '.format(tc),end='')
    if len(qu)>L:
        print(qu[L])
    else:
        print(-1)