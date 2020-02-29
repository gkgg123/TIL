import sys

arr=[[0]*101 for _ in range(101)]
for _ in range(4):
    x,y,nx,ny=map(int,input().split())
    for i in range(x,nx):
        for j in range(y,ny):
            arr[i][j]=1
total=0
for i in range(101):
    total+=sum(arr[i])

print(total)