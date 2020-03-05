
import sys
sys.stdin=open('동훈.txt','r')
T=int(input())

def dfs(val,cnt):
    global max_value
    if val*100<=max_value:
        return
    if cnt==N:
        if val*100>max_value:
            max_value=val*100
        return
    for i in range(N):
        if visited[i]==False:
            visited[i]=True
            dfs(val*arr[cnt][i]/100,cnt+1)
            visited[i]=False



for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for i in range(N)]

    visited=[False]*(N)    
    max_value=0
    dfs(1.0,0)
    result=round(max_value,6)
    print('#{0} {1:0.6f}'.format(tc,max_value))