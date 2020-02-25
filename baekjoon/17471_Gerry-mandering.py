import itertools
import collections
### 게리멘더링 풀이 컨셉 ####
### 일단은 combination을 통해 지역구를 나눠준다.
### 그리고 각 지역구 끼리 연결 되어있으면 인구수를 A,B로 나뉘어 구해주고 격차가 최소인 값을 구하는 방식으로 했다.


def bfs(arr,team):                  ### 지역구끼리 이어져있는지 확인하기 위하여 bfs를 썼다.
    q=collections.deque()           ### 생각은 쉬웠지만 이걸 구현하기 위해서 여러가지 방법을 써봤다.
    q.append(arr)                   ### 그러다가 team 전체 리스트를 받아들이고, 그 team의 첫 인덱스 값만을 입력한다면, 구할수 있을것이라 생각했다.
    cnt=1                           ### 만약에 지역구가 전체가 연결되어 있으면, 다 이어질것이고, 그게 아니면 이어지지 않을것을 이용해서 풀었다.
    visited[arr]=True               ### cnt는 우리가 지역구를 방문한 횟수이다. 처음에 각 team의 최초 위치로 bfs를 들어왔기 때문에 cnt=1이다.
    while q:
        node=q.popleft()
        for k in graph[node]:                   ### 해당 인덱스의 자식노드들이 있으면 for문으로 들어온다.
            if visited[k]==False and k in team:  #### 그리고 그 인덱스를 우리가 방문하지 않았고, 해당 인덱스가 우리팀 내에 있으면 안으로 들어간다.
                visited[k]=True
                q.append(k)
                cnt+=1                          #### 그리고 방문횟수를 1을 더해준다.
    
    if cnt==len(team):              ## 모든 bfs가 끝나고 총 방문횟수가 team의 길이와 같다면 모든 곳을 방문한 것이기 때문에 True를 반환하고,
        return True
    else:                           ## 아니면, False를 방문한다.
        return False
 

N=int(input()) 
arr=list(range(1,N+1)) ### COMBINATION을 돌리기 위한 arr을 만들어줬다. N이 주어지면 1~N 까지의 지역구가 생기게 되고 그걸 위해서 range(1,N+1)
                       ### 을 통해 조합을 위한 arr을 만들어줬다.

people=[0]            ### 각 지역구마다, 인구수를 저장하기 위해 people이란 list를 만들어줬고 0번 인덱스를 0으로 채워줬다.

people.extend(list(map(int,input().split())))   ### 그리고 인구를 저장하기 위해 list 형태로 input이 들어왔으므로, extend를 썼다. 


graph=[[]]   ### 부모인덱스에  자식노드를 저장하기 위해 빈 이중리스트를 만들어줬고 0번 인덱스는 쓸일이 없으므로 [] 빈리스트를 넣어줬다.

people_total=sum(people)   ### 어차피 두 선거구로 나뉘는 것이기 때문에 전체 인구수를 구해주고 한쪽팀 인구수를 구해 빼주면 될것 같아서 전체 인구수를 구해주었다.


for i in range(N):
    temp=list(map(int,input().split()))
    graph.append(temp[1:])
    ### 지역구와의 상관관계를 graph에 넣어주었고 temp의 0번 인덱스, 즉 자식 노드의 개수는 필요가 없어서 버려주었다.


min_number=999999999999999


for i in range(1,N//2+1):   ### 조합을 돌린다고 했는데 1~N 까지 해도 되지만 nCk=nCn-k 와 동일하기 때문에, 전체 N 중에서 N//2 까지만 돌리면 된다.

    b=itertools.combinations(arr,i)  ### combination을 통해 지역구를 구분해준다.
    for k in b:
        a_team=list(k)              ## 콤비네이션에 있는 걸 list해서 a_team을 해주었고
        b_team=list(set(arr)-set(k))   ### 전체에서 a_team을 빼주면 b_team이 되므로 set의 차집합을 이용해서 b_team을 설정해주었다.
        
        visited=[False]*(N+1)     #### 지역구에 들어가는걸 구분하기 위해 visited 리스트를 만들어 주었고, 이건 매 조합이 바뀔때마다 초기화 되어야하므로 이 안에 넣어주었다.
        
        if bfs(a_team[0],a_team) and bfs(b_team[0],b_team):   ### a_team,b_team이 전부 bfs를 만족해서 True를 받아야지만, 선거구끼리의 인구수를 구하는 작업을 했다.
            a_team_sum=0
            for tt in a_team:
                a_team_sum+=people[tt]
            b_team_sum=people_total-a_team_sum
            if abs(b_team_sum-a_team_sum)<=min_number:
                min_number=abs(b_team_sum-a_team_sum)       
    if min_number==0:  ## 최소값은 0보다 작을수 없으므로, 0이 나오면 탈출하게 했다.
        break

if min_number>1000: ## 선거구가 나뉘어지지 않으면 초기값인 99999999가 그대로 이므로 -1을 출력하게 했다.
    print(-1)
else:
    print(min_number)