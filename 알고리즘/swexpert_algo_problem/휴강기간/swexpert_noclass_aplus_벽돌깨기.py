import collections
import copy
import sys
sys.stdin=open('벽돌깨기.txt','r')
dx=[1,-1,0,0]
dy=[0,0,1,-1]


T=int(input())
def bomb(yy,data):
    visited=[[0]*W for _ in range(H)]
    dq=collections.deque()
    for j in range(H):
        if data[j][yy]:
            dq.append([j,yy,data[j][yy]])
            visited[j][yy]=1
            data[j][yy]=0
            break
    while dq:
        x,y,power=dq.popleft()        
        for i in range(4):
            nx=x
            ny=y
            for j in range(power-1):
                nx=nx+dx[i]
                ny=ny+dy[i]
                if 0<=nx<H and 0<=ny<W:
                    if data[nx][ny] and not(visited[nx][ny]):
                        dq.append([nx,ny,data[nx][ny]])
                        data[nx][ny]=0
                        visited[nx][ny]=1
    bt=[0]*W
    for j in range(W):
        for i in range(H):
            if data[i][j]:
                bt[j]+=1
    return bt


def sort_list(dt):
    qu=collections.deque()
    rr_bt=[[0]*W for _ in range(H)]
    for j in range(W):
        for i in range(H-1,-1,-1):
            if dt[i][j]:
                qu.append(dt[i][j])
        row=H-1
        while qu:
            da=qu.popleft()
            rr_bt[row][j]=da
            row-=1
    return rr_bt                      





def dfs(cnt,data,bl):
    global min_value
    if cnt==N or sum(bl)==0:
        temp=sum(bl)
        if temp<min_value:
            min_value=temp
            return
    else:
        return_data=copy.deepcopy(data)
        for i in range(W):
            if bl[i]:
                bt=bomb(i,data)
                rr_tt=sort_list(data)
                dfs(cnt+1,rr_tt,bt)
                data=copy.deepcopy(return_data)



for tc in range(1,T+1):
    N,W,H=map(int,input().split())

    arr=[list(map(int,input().split())) for _ in range(H)]
    block_cnt=[0]*W
    for j in range(W):
        for i in range(H):
            if arr[i][j]:
                block_cnt[j]+=1

    min_value=999999
    dfs(0,arr,block_cnt)
    print(min_value)