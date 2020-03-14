import sys

sys.stdin=open('1873.txt','r')

dx=[-1,1,0,0]  ### 상하 좌우로 나타냈다.
dy=[0,0,-1,1]  
tank=['^','v','<','>']  ### tank의 현재 바라보는 방향을 dx,dy와 동일하게 줬다.
di=['U','D','L','R']    ### 명령어에서 나오는 U,D,L,R도 dx,dy와 동일하게 줬다.


def shoot(x,y,dire):
    nx=x
    ny=y
    while True:
        nx=nx+dx[dire]       #### 다음위치로 계속 진행한다.
        ny=ny+dy[dire]
        if 0<=nx<H and 0<=ny<W:  ### 다음위치가 행렬 내에 있고,
            if arr[nx][ny]=='*':  ### 벽돌로 된 벽이 있으면 평지로 만들고 멈춘다.
                arr[nx][ny]='.'
                break 
            elif arr[nx][ny]=='#':  ## 강철로 된 벽이 있으면 그냥 멈춘다.
                break
        else:
            break   ### 행렬 범위 밖으로 넘어가면 그냥 멈춘다.




def dfs(x,y,start,end):
    stack=[[x,y]]

    while start!=end:    ### 명령어의 길이만큼 다 되면 멈추도록 했다.
        ax,ay=stack.pop()    ### tank의 현재위치를 저장하고
        tank_current=tank.index(arr[ax][ay])   ### tank의 현재 바라보는 방향을 정의해준다/
        commend=comm[start]     ### 그리고 현재 명령어를 찾아준다.
        if commend=='S':    ### 만약에 S이면 shooting이므로, shoot 함수를 통해 shoot 행동을 시행해주고, shoot은 탱크의 위치가 
            shoot(ax,ay,tank_current)  ##변하지 않으므로 현재위치를 그대로 stack에 append 해준다.
            stack.append([ax,ay])
        else:
            tank_next=di.index(commend)  ### S를 제외한 나머지는 전부 방향이동이므로, command로 index를 찾아서
            nx=ax+dx[tank_next]          ### tank가 다음방향을 찾아내준다.
            ny=ay+dy[tank_next]
            if 0<=nx<H and 0<=ny<W:      ### 만약에 tank가 범위를 벗어나지않고,
                if arr[nx][ny]=='.':     ### 다음 방향이 평지이면,
                    stack.append([nx,ny])   ### 다음방향을 append해주고
                    arr[ax][ay]='.'         ### 현재위치를 평지로 만들어주고,
                    arr[nx][ny]=tank[tank_next]    ### 다음 위치를 tank의 다음방향모습으로 바꿔준다.
                else:
                    stack.append([ax,ay])   ### 평지가 아니라면, 현재위치를 append해주고,
                    arr[ax][ay]=tank[tank_next]   ### 현재위치에서 방향만 틀어준다.
            else:
                stack.append([ax,ay])     ### 만약에 다음위치가 행렬 범위 밖으로 넘어가면
                arr[ax][ay]=tank[tank_next]   ### 현재위치를 append 해주고, 방향만 틀어준다.
        start+=1



T=int(input())

for tc in range(1,T+1):
    H,W=map(int,input().split())
    arr=[list(input()) for _ in range(H)]
    N=int(input())
    comm=list(input())
    for i in range(H):
        for j in range(W):
            if arr[i][j] in tank:
                result=[i,j]      ### tank의 현재위치를 찾아낸다.
    dfs(result[0],result[1],0,len(comm))   ### 그리고 dfs라는 함수를 이용해 탐색을 시작한다.
    print('#{} '.format(tc),end='')        ### input 값은 탱크의 x,y 좌표값과, commend 최초 위치인 0, 그리고 명령어의 끝자리인 길이를 넣어줬다.
    for i in range(H):
        print(''.join(arr[i]))