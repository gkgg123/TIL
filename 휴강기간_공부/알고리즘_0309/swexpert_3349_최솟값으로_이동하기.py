def street(start,end):
    dx=end[0]-start[0]
    dy=end[1]-start[1]

    if (dx >=0 and dy>=0) or (dx<0 and dy<0): ### (x2-x1)인 dx와 (y2-y1)인 dy의 부호가 같으면 
        dx=abs(dx)                            ### 두 개중 더 길이가 큰 길이만큼 이동해야한다.
        dy=abs(dy)
        if dy>dx:
            dx,dy=dy,dx
        cnt[0]=cnt[0]+dx
    else:
        cnt[0]=cnt[0]+abs(dx)+abs(dy)         ### 만약 dx와 dy의 부호가 다르면, dx,dy의 크기만큼 이동해줘야한다.

T=int(input())


for tc in range(1,T+1):
    W,H,N=map(int,input().split())
    st=list(map(int,input().split()))
    cnt=[0]
    for i in range(N-1):
        e=list(map(int,input().split()))
        street(st,e)
        st=e[:]  ## start와 end을 계속 바꿔주기 위해서 넣어주었다.
    print('#{} {}'.format(tc,cnt[0]))


