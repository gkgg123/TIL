import collections

N=int(input())
M=int(input())


graph=[[] for _ in range(N+1)]
## 내가 어떤 부품을 몇개 모와야 상위부품을 만들수 있는지 축적해주기 위한, graph 리스트,

line=[0]*(N+1)


for _ in range(M):
    i,j,d=map(int,input().split())

    graph[j].append([i,d])
    #### j번째 부품을 d개 모와야 i가 된다는것을 나타내주기 위한 것
    line[i]+=1
    ### 그리고 이 i번째 부품이 몇개의 소부품이 모여져야하는지 나타내 주는거,

arr=[[0]*(N+1) for _ in range(N+1)]
#### 전체 부품 수량을 누적해주기 위한거 ####
check=[False]*(N+1)
### 기본부품이 어떤건지 확인해주기 위한거###
q=collections.deque()


for i in range(1,N+1):
    if line[i]==0:
        ### line[i]가 0이라는 것은 기본부품이라는 것을 뜯하니
        check[i]=True
        #### check에 True로 해서 이게 기본부품인걸 check 해주는거
        q.append(i)
        ### 그리고 밑에 부품을 찾기 위한 que에 넣어준다.
        arr[i][i]=1
        #### 그리고 기본부품을 쓰기 위해선 1개가 필요하기 때문에 넣어준거,
while q:
    here=q.popleft()

    for i in range(len(graph[here])):
        next_ind=graph[here][i][0]
        ### 현재 부품으로 만들수 있는 상위 부품을 찾아낸다
        next_cost=graph[here][i][1]
        ### 상위 부품을 만들기 위해서는 몇개가 필요한지 세어줬다.
        for j in range(1,N+1):
            arr[next_ind][j]=arr[next_ind][j]+arr[here][j]*next_cost
            ### 현재 부품에서 필요한 제품수를 몇개 부품이 필요한지 곱해서 계속 더해주었다.
        line[next_ind]-=1
        ### 그리고 한 부품군에 대해서 조립이 끝나면, 1개씩 차감해준다.
        if line[next_ind]==0:
            ### 그리고 상위제품군에 대해서 기본부품에 대한 조사가 전부 끝나면 que에 추가 시켜준다.
            q.append(next_ind)

for i in range(1,N+1):
    if check[i]:
        print(i,arr[N][i])