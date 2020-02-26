T=int(input())

for tc in range(1,T+1):
    N=int(input())
    bus=[list(map(int,input().split())) for _ in range(N)]
    P=int(input())
    P_list=[]
    for _ in range(P):
        P_list.append(int(input()))

    bus_cnt=[0]*5001
    for k in bus:
        for t in range(k[0],k[1]+1):
            bus_cnt[t]+=1
    print('#{} '.format(tc),end='')

    for tt in P_list[:-1]:
        print('{}'.format(bus_cnt[tt]),end=' ')
    print(bus_cnt[P_list[-1]])