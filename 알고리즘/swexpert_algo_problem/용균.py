import sys
sys.stdin=open('othe.txt','r')

D = [[i,j] for i in range(-1,2) for j in range(-1,2) if i!=0 or j!=0]
 
for T in range(1,int(input())+1):
    N,M = map(int,input().split())
    d = [[0]*N for i in range(N)]
    t = N//2
    d[t][t],d[t-1][t-1] = 2,2
    d[t-1][t],d[t][t-1] = 1,1
    for i in range(M):
        y,x,c = map(int,input().split())
        y -= 1
        x -= 1
        d[y][x] = c
        for dy,dx in D:
            for t in range(1,N+1):
                ny = y + dy*t
                nx = x + dx*t
                if 0<=ny<N and 0<=nx<N:
                    if d[ny][nx]==0:
                        break
                    if d[ny][nx]==c:
                        for cnt in range(1,t):
                            d[y+dy*cnt][x+dx*cnt] = c
                        break
    ans = [0,0,0]
    for i in range(N):
        for j in range(N):
            ans[d[i][j]] += 1
    print('#{} {} {}'.format(T,ans[1],ans[2]))