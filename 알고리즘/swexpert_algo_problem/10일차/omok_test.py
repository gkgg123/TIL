def find_five():
    for y in range(19):
        for x in range(19):
            if omok[x][y]==1 or omok[x][y]==2:
                color=omok[x][y]
                for dis in range(4):
                    nx=x+dx[dis]
                    ny=y+dy[dis]
                    if 0<=nx<19 and 0<=ny<19 and omok[nx][ny]==color:
                        if 0<=x-dx[dis]<19 and 0<=y-dy[dis]<19:
                            if omok[x-dx[dis]][y-dy[dis]]==color:
                                continue
                        cnt=1
                        while 0<=nx<19 and 0<=ny<19 and omok[nx][ny]==color:
                            cnt+=1
                            nx+=dx[dis]
                            ny+=dy[dis]
                        if cnt==5:
                            ans[0]=color
                            ans[1]=x+1
                            ans[2]=y+1
                            return

dx=[1,1,0,-1]
dy=[0,1,1,1]

omok=[list(map(int,input().split())) for i in range(19)]
ans=[0,0,0]
find_five()
print(ans)