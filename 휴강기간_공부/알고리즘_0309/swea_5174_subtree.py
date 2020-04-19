def dfs(st,cnt):
    stack=[st]

    while stack:
        x=stack.pop()
        for i in graph[x]:
            if visited[i]==0:
                stack.append(i)
                cnt+=1
                visited[i]=1
    return cnt


T=int(input())



for tc in range(1,T+1):
    E,N=map(int,input().split())

    graph=[[] for _ in range(E+2)]

    arr=list(map(int,input().split()))

    for i in range(E):
        graph[arr[2*i]].append(arr[2*i+1]) 
    visited=[0]*(E*2)
    result=dfs(N,1)
    print('#{} {}'.format(tc,result))