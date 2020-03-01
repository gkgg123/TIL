### DFS를 전체 탐색을 했더니, 시간초과가 떴다. 그래서 인터넷을 방법을 찾다가 Cycle이 되는것들을 바로바로 판단을 해서
### 추가하는 방식으로 풀었다.

def dfs(v,i):
    visited[v]=True   ### 내가 들어온 값을 v,i를 두었는데, i는 내가 찾고자 싶은 부모노드, 
                      ### v는 내가 자식노드들을 찾아다니면서 나오는 자식노드라 생각하면 똑같다.
                      ### i의 자식노드를 따라 다니면서 v는 계속 갱신된다.
                      ### 그러다가 해당 v의 자식노드 중 i와 동일한것이 있으면, 그것은
                      ### cycle이 완성이 되는것이다.
                      ### 그래서 그때 result에 추가해주면 되는것이다.

    for w in arr[v]:
        if visited[w]==False:
            dfs(w,i)
        elif visited[w] and w==i:
            result.append(w)




N=int(input())

arr=[[] for i in range(N+1)]
for i in range(N):
    arr[i+1].append(int(input()))  ## 이건 해당 인덱스에 자식노드를 추가해놓는것과 마찬가지이다.


result=[]

for i in range(1,N+1):  ## 매번 visited를 초기화 시켜주고 처음 인덱스부터 시작한다.
    visited=[False]*(N+1)
    dfs(i,i)
print(len(result))

for i in result:
    print(i)