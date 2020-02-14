import sys
sys.stdin=open('farm.txt','r')

T=int(input())


for tc in range(1,T+1):
    N=int(input())
    farm=[list(map(int,list(input()))) for i in range(N)]
    total=0
    k=N//2
    '''
    #  for i in range(N//2+1):
    #     t=2*i    
    #     while t>=0:
    #         total+=farm[i][k+t]
    #         t-=1
    #     k-=1
    # k=0
    # for i in range(N//2):
    #     t=N-2-2*i
    #     hang=i+N//2+1        
    #     while t>0:
    #         total+=farm[hang][k+t]            
    #         t-=1
    #     k+=1
    '''
    # for i in range(N):
    #     if i<=N//2:
    #         t=2*i    
    #         while t>=0:
    #             total+=farm[i][k+t]
    #             t-=1
    #         k-=1
    #     else:
    #         t=(N-i)*2-1
    #         while t>0:
    #             total+=farm[i][k+t+1]
    #             t-=1
    #         k+=1
    for i in range(N):
        for j in range(N):
            if (abs(i-N//2)+abs(j-N//2))<=N//2:
                total+=farm[i][j]

    print('#{} {}'.format(tc,total))


