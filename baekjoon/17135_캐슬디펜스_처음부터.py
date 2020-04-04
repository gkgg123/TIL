import itertools
from collections import deque
dx=[0,-1,0]
dy=[-1,0,1]

def defense(arc):
    global max_count,enemy_total
    count=0
    copy_position=enemy_position.copy()
    enemy=enemy_total
    attack=set()
    kill=[[0]*M for _ in range(N)]
    archers_row=N-1
    while enemy>0:
        for ar in arc:
            Q=deque()
            visit={}
            Q.append((archers_row,ar,1))
            visit[(archers_row,ar)]=1
            while Q:
                x,y,d=Q.popleft()
                if d>D:
                    break
                if arr[x][y]=='1' and not kill[x][y]:
                    attack.add((x,y))
                    break
                for i in range(3):
                    nx=x+dx[i]
                    ny=y+dy[i]
                    if 0<=nx and 0<=ny<M:
                        if visit.get((nx,ny)):
                            continue
                        Q.append((nx,ny,d+1))
                        visit[(nx,ny)]=1

        for x,y in attack:
            enemy-=1
            count+=1
            kill[x][y]=1
            copy_position.remove((x,y))
        attack.clear()
        temp=set()

        for x,y in copy_position:
            if x==archers_row:
                enemy-=1
            else:
                temp.add((x,y))
        archers_row-=1
        copy_position=temp.copy()
    
    if max_count<count:
        max_count=count


N,M,D=map(int,input().split())




enemy_position=set()
enemy_total=0
max_count=0
arr=[]

for i in range(N):
    arr+=[input().split()]
    for j in range(M):
        if arr[i][j]=='1':
            enemy_position.add((i,j))
            enemy_total+=1
archers=itertools.combinations(range(M),3)

if enemy_total:
    for archer in archers:
        defense(archer)
print(max_count)
