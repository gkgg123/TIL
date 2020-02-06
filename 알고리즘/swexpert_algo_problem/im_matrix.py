import sys
sys.stdin=open('im_matrix.txt','r')

T=int(input())

def search(x,y):
    global r_x
    global c_y
    global dist
    dist[x][y]=0
    if 0<=x+1<N and dist[x+1][y]==-1 and numbers[x+1][y]>0:
        r_x[0]+=1
        search(x+1,y)
    elif 0<=y+1<N and dist[x][y+1]==-1 and numbers[x][y+1]>0:
        
        c_y[0]+=1
        for k in range(y+1,-1,-1):
            
            dist[x][k]=0
        search(x,y+1)
    else:
        if r_x[0]+c_y[0]!=0:
            total.append([r_x[0]+1,c_y[0]+1])
        r_x=[0]
        c_y=[0]








for tc in range(1,T+1):
    N=int(input())
    dist=[[-1]*N for i in range(N)]
    numbers=[list(map(int,input().split())) for i in range(N)]
    r_x=[0]
    c_y=[0]
    total=[]
    for i in range(N):
        for j in range(N):
            if numbers[i][j]!=0 and dist[i][j]==-1:
                search(i,j)
    print(total)