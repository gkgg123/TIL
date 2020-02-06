import sys
import copy
sys.stdin=open('othe.txt','r')



T=int(input())
dx=[-1,0,1,-1,1,-1,0,1]
dy=[-1,-1,-1,0,0,1,1,1]
dd=[1,2]
def oth(x,y,color):
    othe[x][y]=color
    for i in range(8):
        for t in range(1,N+1):
            nx=x+dx[i]*t
            ny=y+dy[i]*t
            if 0<=nx<N and 0<=ny<N:
                if othe[nx][ny]==0:
                    break
                if othe[nx][ny]==color:
                    for cnt in range(1,t):
                        othe[x+dx[i]*cnt][y+dy[i]*cnt]=color
                    break
            


for tc in range(1,T+1):
    N,M=map(int,input().split())
    othe=[[0]*N for i in range(N)]    
    for i in range(N//2-1,N//2+1):
        for j in range(N//2-1,N//2+1):
            if (i+j)%2==0:
                othe[i][j]=2
            else:
                othe[i][j]=1
    for p in range(M):
        total_ind=[]
        
        li=list(map(int,input().split()))
        # print(p,othe)
        oth(li[0]-1,li[1]-1,li[2])
        # print(p,othe)
    cnt_b=0
    cnt_w=0
    for num in othe:
        for k in num:
            if k==2:
                cnt_w+=1
            elif k==1:
                cnt_b+=1

    print('#{} {} {}'.format(tc,cnt_b,cnt_w))
