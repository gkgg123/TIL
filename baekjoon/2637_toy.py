N=int(input())
M=int(input())
def dfs(cu,cnt):
    if cu in origin_bupum.keys():
        origin_bupum[cu]+=cnt
    else:
        for k in range(1,N):  
            if arr[cu][k]:
                dfs(k,cnt*arr[cu][k])


bupum=[0]*(N+1)

arr=[[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    i,j,m=map(int,input().split())
    arr[i][j]=m
    bupum[i]=1
origin_bupum={}
for ind,val in enumerate(bupum):
    if ind!=0 and val==0:
        origin_bupum[ind]=0

dfs(N,1)
for ind,val in origin_bupum.items():
    print(ind,val)