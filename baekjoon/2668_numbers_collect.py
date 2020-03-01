def calc(vi):
    global max_len
    global max_list
    a1=set()
    a2=set()
    for i in range(N):
        if vi[i]==True:
            a1.add(arr1[i])
            a2.add(arr2[i])
    if a1==a2:
        if max_len<len(a1):
            max_len=len(a1)
            max_list=list(a1)






def dfs(k=0):
    if k==N:
        calc(visited)
        return

    visited[k]=True
    dfs(k+1)
    visited[k]=False
    dfs(k+1)

N=int(input())
arr1=list(range(1,N+1))
arr2=[]

for _ in range(N):
    arr2.append(int(input()))
visited=[False]*N
max_len=0
max_list=[]
dfs()
print(max_len)
for i in max_list:
    print(i)