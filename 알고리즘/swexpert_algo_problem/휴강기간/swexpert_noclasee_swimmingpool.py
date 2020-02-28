import sys

sys.stdin=open('text2.txt','r')
T=int(input())

def dfs(k=0):
    global min_value
    if k>=12:
        temp=0
        for tt in range(12):
            if visited[tt]==0:
                temp+=month[tt]*ticket[0]
            elif visited[tt]==1:
                temp+=ticket[1]
            elif visited[tt]==2:
                temp+=ticket[2]
                visited[tt+1]=-1
                visited[tt+2]=-1
        if min_value[0]>temp:
            min_value[0]=temp
        return

    for i in range(3):
        if i==0 and visited[k]==-1:
            visited[k]=0
            dfs(k+1)
            visited[k]=-1
        if i==1 and visited[k]==-1:
            visited[k]=1
            dfs(k+1)
            visited[k]=-1
        if i==2 and visited[k]==-1:
            visited[k]=2
            dfs(k+3)
            visited[k]=-1



for tc in range(1,T+1):
    ticket=list(map(int,input().split()))
    #1일,1달,3달,1년#
    month=list(map(int,input().split()))
    visited=[-1]*15
    min_value=[ticket[3]]
    dfs()    
    print('#{} {}'.format(tc,min_value[0]))   