### 링크드로 해야하는데 deque를 이용해서 통과

import sys
sys.stdin=open('5110.txt','r')
from collections import deque


T=int(input())

for tc in range(1,T+1):
    N,M=map(int,input().split())
    arr=[list(map(int,input().split())) for i in range(M)]
    result=deque()
    result.extend(arr[0][:])

    t=1
    Flag=False
    while t<M:

        for i in range(t*N):
            if result[i]>arr[t][0]:
                Flag=True
                ind=i
                break
        if Flag:
            for i in range(N-1,-1,-1):
                result.insert(ind,arr[t][i])
            t+=1
            Flag=False
        else:
            result.extend(arr[t][:])
            t=t+1
    print('#{} '.format(tc),end='')
    for i in range(10):
        print(deque.pop(),end=' ')
    print('')
