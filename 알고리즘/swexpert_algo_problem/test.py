# aaa=[[0,1,2],[3,4,5],[6,7,8]]
# m=len(aaa)
# dx=[0,0,-1,1]
# dy=[1,-1,0,0]
# print(aaa)
# for x in range(len(aaa)):
#     for y in range(len(aaa[x])):
#         print('현재 위치 {}'.format(aaa[x][y]))
#         for I in range(4):
#             textX=x+dx[I]
#             textY=y+dy[I]
            
#             if 0<=textX<m and 0<=textY<m:
                
#                 print(aaa[textX][textY])



### 강사님 꺼 ####
di=[-1, 0,1,0]
dj=[0,1,0,-1]

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for i in range(N)]
    res=[[0 for i in range(N)] for j in range(N)]
    result=0
    for x in range(N):
        for y in range(N):
            for i in range(N):
                textX=x+di[i]
                textY=y+dj[i]
                if 0<=textX<N and 0<=textY<N:
                    res[x][y]+=abs(arr[x][y]-arr[textX][textY])
                    result+=abs(arr[x][y]-arr[textX][textY])
    print(result)



    print('#{} {}'.format(tc,res))
