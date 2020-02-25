import sys
sys.stdin=open('startlink.txt','r')
### 스타트와 링크 풀이법 
### itertools를 이용해 조합을 써도 되지만 dfs를 이용하여, 조합을 만들어줬다.
### 해당부분만 바뀌었고, 기본적인 풀이는 같다.


def calc(vi):
    global arr
    team_a=[]
    team_b=[]
    for i,v in enumerate(vi):
        if v==True:
            team_a.append(i)
        else:
            team_b.append(i)

    team_a_score=0
    team_b_score=0
    for i in range(N//2):
        for j in range(i+1,N//2):
            team_a_score+=arr[team_a[i]][team_a[j]]
            team_b_score+=arr[team_b[i]][team_b[j]]
    temp=abs(team_a_score-team_b_score)


    if temp<min_total[0]:
        
        min_total[0]=temp



    


def match_team(k=1):
    global N
    if k==N:
        if visited.count(False)==N/2:
            calc(visited)
            return
        return
    visited[k]=True
    match_team(k+1)
    visited[k]=False
    match_team(k+1)



N=int(input())
arr=[list(map(int,sys.stdin.readline().split())) for i in range(N)]
visited=[False]*N
for i in range(N):
    for j in range(i+1,N):
        arr[i][j]+=arr[j][i]
min_total=[9999999999999999]
match_team()
print(min_total[0])