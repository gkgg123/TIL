import sys
import copy
sys.setrecursionlimit(10**6)
sys.stdin=open('maze.txt','r')


dx=[-1,1,0,0]
dy=[0,0,1,-1]

def search(x,y,temp):
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<16 and 0<=ny<16:
            if temp[nx][ny]==0:
                temp[nx][ny]=2
                search(nx,ny,temp)
            elif temp[nx][ny]==3:
                cnt[0]+=1
                return 0
            else:
                continue

    




for tc in range(1,11):
    T=int(input())
    maze1=[input() for i in range(16)]
    maze=[]

    for i in maze1:
        temp=[]
        for k in i:
            temp.append(int(k))
        maze.append(temp[:])
        
    # print(maze)
    cnt=[0]
    temp=copy.deepcopy(maze)

    for i in range(16):
        for j in range(16):            
            if temp[i][j]==2:
                search(i,j,temp)
    if cnt[0]>0:
        print('#{} 1'.format(tc))
    else:
        print('{} 0'.format(tc))
