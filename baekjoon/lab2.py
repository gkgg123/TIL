import sys
from itertools import combinations
import copy
sys.stdin=open("input.txt",'r')
sys.setrecursionlimit(10**6)
dx=[-1,1,0,0]
dy=[0,0,1,-1]
def dfs(x,y,_cnt):
    
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<n and 0<=ny<m:
            if lab_temp[nx][ny]==0:
                cnt[0]+=1
                lab_temp[nx][ny]=2
                dfs(nx,ny,_cnt)

n,m=list(map(int,sys.stdin.readline().split()))

lab=[[0 for i in range(m)] for j in range(n)]
for k in range(n):
    lab[k]=list(map(int,sys.stdin.readline().split()))
total_zero=[]
zeros=0
ones=0
twos=0
for row in range(n):
    for col in range(m):
        if lab[row][col]==0:
            total_zero.append((row,col))
            zeros+=1
        if lab[row][col]==1:
            ones+=1
twos=n*m-zeros-ones


max_safe=0
a=combinations(total_zero,3)
total_cnt=[]
for i in a:
    lab_temp=copy.deepcopy(lab)
    lab_temp[i[0][0]][i[0][1]]=1
    lab_temp[i[1][0]][i[1][1]]=1
    lab_temp[i[2][0]][i[2][1]]=1
    cnt=[0]
    for row in range(n):
        for col in range(m):
            if lab_temp[row][col]==2:                
                dfs(row,col,cnt[0])
    
    safe=n*m-twos-cnt[0]-ones-3
    if max_safe<safe:
        max_safe=safe


print(max_safe)