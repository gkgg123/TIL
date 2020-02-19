import sys

sys.stdin=open('maze.txt','r')

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def dfs(x,y):
    stack=[]
    stack.append([x,y])
    while stack:
        ax,ay=stack.pop()
        for i in range(4):
            nx=ax+dx[i]
            ny=ay+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if maze[nx][ny]=='0':
                    maze[nx][ny]='2'
                    stack.append([nx,ny])
                elif maze[nx][ny]=='3':
                    result[0]=1
        


T=int(input())

for tc in range(1,T+1):
    N=int(input())
    maze=[list(input()) for i in range(N)]
    
    result=[0]
    for i in range(N-1,0,-1):
        for j in range(N):
            if maze[i][j]=='2':
                dfs(i,j)
  
    print('#{} {}'.format(tc,result[0]))