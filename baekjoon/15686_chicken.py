import sys
### 치킨 집 문제 이것도 dfs를 이용해서 풀었다.
### 조합을 이용해도 되지만 dfs를 연습하기 위해서 dfs를 사용했다.
### dfs를 이용하여, 주어진 M개의 치킨집을 구해준다.
### 그리고 난뒤 해당 치킨집과 집과의 최소거리들의 합을 구해서, 최소값을 구하는 방식으로 했다.


def calc(vi): ## 이거는 집에서 최소거리의 치킨집을 구하고, 그것들을 전부 더하는 과정이다.
    global min_distance
    total_distance=0
    for i in home:
        min_temp=999999
        for j in vi:
            temp=abs(i[0]-j[0])+abs(i[1]-j[1])
            min_temp=min(min_temp,temp)
        total_distance+=min_temp
    return total_distance

            
def chicken_dfs(k=0):
    global M,N
    global min_distance
    chicken_store=[]
    if k==len(chicken):
        if visited.count(True)==M: ### visited에서 고른 치킨집의 수가, M과 같다면
            
            for i,k in enumerate(visited): ### True에 해당되는 인덱스의 치킨집 인덱스를 뽑아서 리스트에 저장해줬다.
                if k==True:                   
                    chicken_store.append(chicken[i])
            
            b=calc(chicken_store)
            min_distance=min(min_distance,b)
        return


    visited[k]=True####
    chicken_dfs(k+1) #여기는 재귀함수를 이용해서, 모든 경우의수에 대한 조합을 만들어내는 과정이다.
    visited[k]=False #
    chicken_dfs(k+1)####



N,M=list(map(int,sys.stdin.readline().split()))

arr=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
home=[] ### home의 위치값을 저장하기 위한 리스트이다.
chicken=[] #### 치킨집의 위치값을 저장하기 위한 리스트이다.
for i in range(N):
    for j in range(N):
        if arr[i][j]==1:
            home.append([i,j])
        elif arr[i][j]==2:
            chicken.append([i,j])

visited=[False]*len(chicken)
min_distance=99999999999
chicken_dfs()
print(min_distance)