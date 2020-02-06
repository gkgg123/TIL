import sys
import copy
sys.stdin=open('othe.txt','r')



T=int(input())
dx=[-1,0,1,-1,1,-1,0,1]
dy=[-1,-1,-1,0,0,1,1,1]
dd=[1,2]
def oth(x,y,color):
    result=[]        
    for i in range(8):
        global total_ind
        nx=x+dx[i]
        ny=y+dy[i]
               
        if 0<=nx<N and 0<=ny<N:
            if othe[nx][ny]==0:
                continue
            elif othe[nx][ny]==dd[color-1]:
                if len(total_ind)!=0:
                    result.append(copy.deepcopy(total_ind))
                    continue
                else:
                    continue
            elif othe[nx][ny]==dd[color%2]:
                total_ind.append([nx,ny])
                while othe[nx][ny]==dd[color%2]:
                    nx+=dx[i]
                    ny+=dy[i]
                    if 0<=nx<N and 0<=ny<N:
                        if othe[nx][ny]==dd[color%2]:
                            total_ind.append([nx,ny])
                        elif othe[nx][ny]==dd[color-1]:
                            result.append(copy.deepcopy(total_ind))
                            break
                        else:
                            total_ind=[]
                            break
                    else:
                        total_ind=[]
                        break
        else:
            total_ind=[]
            continue
    return result

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
        a=[]
        li=list(map(int,input().split()))
        # print(p,othe)
        a=oth(li[0]-1,li[1]-1,li[2])
        re=[]
        for k in a:
            for j in k:
                re.append(j)

        for i in re:
            othe[li[0]-1][li[1]-1]=li[2]
            othe[i[0]][i[1]]=li[2]
    cnt_b=0
    cnt_w=0
    for num in othe:
        for k in num:
            if k==2:
                cnt_w+=1
            elif k==1:
                cnt_b+=1

    print('#{} {} {}'.format(tc,cnt_b,cnt_w))
