import sys
import collections
### [Professional] 키 순서 ####
sys.stdin=open('height_sort.txt','r')


def dfs1(x):
    stack=[x]
    while stack:
        node=stack.pop()
        for i in graph1[node]:
            if visit[x][i]==0:
                visit[x][x]+=1
                visit[x][i]=1       
                stack.append(i)
    return
def dfs2(x):
    stack=[x]
    while stack:
        node=stack.pop()
        for i in graph2[node]:
            if visit[x][i]==0:
                visit[x][x]+=1
                visit[x][i]=1       
                stack.append(i)
    return

T=int(input())

for tc in range(1,T+1):
    N=int(input())
    M=int(input())
    arr=[list(map(int,input().split())) for i in range(M)]
    #### 이건 dfs를 이용하여 풀어냈다
    #### 부모노드로 한번 dfs 해서 부모노드를 통해가서 dfs의 갯수와
    #### 자식 노드를 기준으로 한 dfs를 하여 dfs 의 갯수를
    #### 더했을때 총 갯수가 전체 주어진 N보다 1이 작으면,
    #### 해당 값은 키의 순서가 이어진것을 알 수 있다.
    #### 처음에는 bfs를 했지만 dfs로 바꾼이유는
    #### 왠지 모르지만 시간초과가 떠서 그랬다.
    #### 아마 bfs를 넓게 탐색을 하다 보니
    #### 끝값을 찾고 리턴하는데 시간이 오래걸린것같다.
    #### 그에 반면 dfs는 해당 최대깊이까지 찍고 바로 돌아오는 것이기 때문에 시행시간이 짧은것같다.
    #### 문제에서 주어진 N의 최대조건이 500이다보니 그런것 같다.
    graph1=[[] for i in range(N+1)]
    graph2=[[] for i in range(N+1)]
    for i in arr:
        graph1[i[0]].append(i[1])
        graph2[i[1]].append(i[0])
    visit=[[0]*(N+1) for i in range(N+1)]
    #### visit도 (N+1)*(N+1)로 만들어 준 이유가,
    #### 대각선 행과열에는 우리가 찾고자하는 i의 값을 누적해고 visit 값을 누적하고
    #### i행에는 한번 방문한곳을 다시 방문하는 일을 막고자 (N+1)*(N+1)행렬을 만들었다.
    for i in range(1,N+1):        
        dfs1(i)
        dfs2(i)
    cnt=0
    for i in range(1,N+1):
        if visit[i][i]==N-1:
            cnt+=1
    print('#{} {}'.format(tc,cnt))


    ### 나중에 찾아보니 이 문제는 플로이드 와샬 문제로 푸는것이 정석적인 풀이방법이었다. ###