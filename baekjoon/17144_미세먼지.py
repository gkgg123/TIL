import sys

sys.stdin=open('dust.txt','r')

dx=[1,-1,0,0]
dy=[0,0,-1,1]


def spray(arr):


    new_dust=[[0]*C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if arr[i][j]>0:
                cnt=0
                st=[]
                for k in range(4):
                    nx=i+dx[k]
                    ny=j+dy[k]
                    if 0<=nx<R and 0<=ny<C:
                        if arr[nx][ny]!=-1:
                            cnt+=1
                            st.append([nx,ny])
                if cnt:
                    while st:
                        x,y=st.pop()
                        new_dust[x][y]+=arr[i][j]//5
                temp=arr[i][j]-(arr[i][j]//5*cnt)
                new_dust[i][j]+=temp
    for x,y in air_con:
        new_dust[x][y]=-1
    return new_dust
                
def air_condition(ar):
    st1=air_con[0]
    st2=air_con[1]
    n_du=[[0]*C for _ in range(R)]

    for i in range(st1[0]-1,-1,-1):
        if ar[i][0] and ar[i+1][0]!=-1:
            n_du[i+1][0]=ar[i][0]
    
    for j in range(C-1,0,-1):
        if ar[0][j]:
            n_du[0][j-1]=ar[0][j]
    for i in range(st1[0],0,-1):
        if ar[i][C-1]:
            n_du[i-1][C-1]=ar[i][C-1]
    for j in range(1,C-1):
        if ar[st1[0]][j]:
            n_du[st1[0]][j+1]=ar[st1[0]][j]
    for i in range(st1[0]-1,0,-1):
        for j in range(1,C-1):
            if ar[i][j]:
                n_du[i][j]=ar[i][j]
    ## 2번째 공청기
    for i in range(R-1,st2[0],-1):
        if ar[i][0] and ar[i-1][0]!=-1:
            n_du[i-1][0]=ar[i][0]
    for j in range(C-1,0,-1):
        if ar[R-1][j]:
            n_du[R-1][j-1]=ar[R-1][j]
    for i in range(st2[0],R-1):
        if ar[i][C-1]:
            n_du[i+1][C-1]=ar[i][C-1]
    for j in range(1,C-1):
        if ar[st2[0]][j]:
            n_du[st2[0]][j+1]=ar[st2[0]][j]
    for i in range(st2[0]+1,R-1):
        for j in range(1,C-1):
            if ar[i][j]:
                n_du[i][j]=ar[i][j]
    for x,y in air_con:
        n_du[x][y]=-1
    return n_du



R,C,T=map(int,input().split())
air_con=[]
dust=[list(map(int,input().split())) for _ in range(R)]
for i in range(R):
    for j in range(C):
        if dust[i][j]==-1:
            air_con.append([i,j])


for _ in range(T):
    new_du=spray(dust)
    for dd in new_du:
        print(dd)
    print('확산')
    dust=air_condition(new_du)
    for dd in dust:
        print(dd)
    print('공청')

total=2
for k in dust:
    total+=sum(k)
print(total)