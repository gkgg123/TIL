def dfs(st):
    stack=st[:]
    while stack:
        temp=stack.pop()
        visit[temp[0]]=1
        visit[temp[1]]=1
        for k in node:
            if k[0]==temp[1]:
                stack.append(k)
        



T=int(input())

for tc in range(1,T+1):
    V,E=list(map(int,input().split()))

    node=[list(map(int,input().split())) for i in range(E)]
    start,finish=list(map(int,input().split()))
    visit=[0]*(V+1)
    tt=[]
    # print(node)
    for i in node:
        if i[0]==start:
            tt.append(i)

    dfs(tt)
    print('#{} {}'.format(tc,visit[finish]))