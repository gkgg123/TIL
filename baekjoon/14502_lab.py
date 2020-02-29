import sys
from itertools import combinations
import copy
sys.stdin=open("input.txt",'r')
sys.setrecursionlimit(10**6)
dx=[-1,1,0,0]
dy=[0,0,1,-1]
def dfs(x,y,_cnt):
    dist[x][y]=_cnt
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<n and 0<=ny<m:
            if lab_temp[nx][ny]==0 and dist[nx][ny]==-1:
                lab_temp[nx][ny]=2
                dfs(nx,ny,_cnt)

n,m=list(map(int,input().split()))

lab=[[0 for i in range(m)] for j in range(n)]
for k in range(n):
    lab[k]=list(map(int,input().split()))
total_zero=[]
for row in range(n):
    for col in range(m):
        if lab[row][col]==0:
            total_zero.append((row,col))

a=combinations(total_zero,3)
total_cnt=[]
for i in a:
    lab_temp=copy.deepcopy(lab)
    dist=[[-1 for i in range(m)] for j in range(n)]
    lab_temp[i[0][0]][i[0][1]]=1
    lab_temp[i[1][0]][i[1][1]]=1
    lab_temp[i[2][0]][i[2][1]]=1
    cnt=0
    cnt_result=0
    for row in range(n):
        for col in range(m):
            if lab_temp[row][col]==2 and dist[row][col]==-1:                
                dfs(row,col,cnt)
    for row in range(n):
        for col in range(m):
            if lab_temp[row][col]==0:
                cnt_result+=1
    total_cnt.append(cnt_result)
print(max(total_cnt))