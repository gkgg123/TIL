import collections 


T=int(input())

for tc in range(1,T+1):
    N,K=map(int,input().split())
    result=set()
    M=N//4
    q=collections.deque()
    q.extend(list(input()))
    while True:
        cnt=0
        for i in range(4):
            temp=''
            for j in range(M):       
                temp+=q[M*i+j]
            if temp not in result:
                result.add(temp)
                cnt+=1
        if cnt==0:
            break
        else:
            q.rotate(1)
    total=[]
    for k in result:
        total.append(int(k,16))
    total.sort(reverse=True)
    print('#{} {}'.format(tc,total[K-1]))
    