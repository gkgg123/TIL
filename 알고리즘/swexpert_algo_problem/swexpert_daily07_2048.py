T=int(input())

def arr(s,num):
    N=num
    temp=0
    if s=='up':        
        while temp<N:
            for i in range(0,N-1,1):
                for j in range(N):
                    if b_2048[i][j]==0:                
                        b_2048[i][j]=b_2048[i+1][j]
                        b_2048[i+1][j]=0
            temp+=1

    elif s=='down':        
        while temp<N:
            for i in range(N-1,0,-1):
                for j in range(0,N):
                    if b_2048[i][j]==0:                
                        b_2048[i][j]=b_2048[i-1][j]
                        b_2048[i-1][j]=0
            temp+=1

    elif s=='right':
        while temp<N:
            for i in range(N-1,0,-1):
                for j in range(N):
                    if b_2048[j][i]==0:                
                        b_2048[j][i]=b_2048[j][i-1]
                        b_2048[j][i-1]=0
            temp+=1
    else:
        while temp<N:
            for i in range(0,N-1,1):
                for j in range(N):
                    if b_2048[j][i]==0:                
                        b_2048[j][i]=b_2048[j][i+1]
                        b_2048[j][i+1]=0
            temp+=1
def co(s,num):
    if s=='up':
        for i in range(0,N-1,1):
            for j in range(N):
                if b_2048[i][j]==b_2048[i+1][j]:
                    b_2048[i][j]=b_2048[i][j]+b_2048[i][j]
                    b_2048[i+1][j]=0
    elif s=='down':
        for i in range(N-1,0,-1):
            for j in range(N):
                if b_2048[i][j]==b_2048[i-1][j]:
                    b_2048[i][j]=b_2048[i][j]+b_2048[i][j]
                    b_2048[i-1][j]=0
    elif s=='left':
        for i in range(0,N-1,1):
            for j in range(N):
                if b_2048[j][i]==b_2048[j][i+1]:
                    b_2048[j][i]=b_2048[j][i]+b_2048[j][i]
                    b_2048[j][i+1]=0
    
    else:
        for i in range(N-1,0,-1):
            for j in range(N):
                if b_2048[j][i]==b_2048[j][i-1]:
                    b_2048[j][i]=b_2048[j][i]+b_2048[j][i]
                    b_2048[j][i-1]=0


for tc in range(1,T+1):
    N,st=input().split()
    N=int(N)
    b_2048=[list(map(int,input().split())) for i in range(N)]

    arr(st,N)
    co(st,N)
    arr(st,N)
    ## up일떄##
    # for i in range(0,N-1,1):
    #     for j in range(N):
    #         if b_2048[i][j]==b_2048[i+1][j]:
    #             b_2048[i][j]=b_2048[i][j]+b_2048[i][j]
    #             b_2048[i+1][j]=0
    ## down일떄##
    # for i in range(N-1,0,-1):
    #     for j in range(N):
    #         if b_2048[i][j]==b_2048[i-1][j]:
    #             b_2048[i][j]=b_2048[i][j]+b_2048[i][j]
    #             b_2048[i-1][j]=0
    ## left일떄##
    # for i in range(0,N-1,1):
    #     for j in range(N):
    #         if b_2048[j][i]==b_2048[j][i+1]:
    #             b_2048[j][i]=b_2048[j][i]+b_2048[j][i]
    #             b_2048[j][i+1]=0
    
    # right일떄
    # for i in range(N-1,0,-1):
    #     for j in range(N):
    #         if b_2048[j][i]==b_2048[j][i-1]:
    #             b_2048[j][i]=b_2048[j][i]+b_2048[j][i]
    #             b_2048[j][i-1]=0
     

    print('#{}'.format(tc))

    for i in b_2048:
        for j in i:
            print(j,end=' ')
        print('')
    # # ##### UP 일때 #######
    # for i in range(0,N-1,1):
    #     for j in range(N):
    #         if b_2048[i][j]==0:                
    #             b_2048[i][j]=b_2048[i+1][j]
    #             b_2048[i+1][j]=0
    # #### Down 일떄 ######
    # temp=0
    # while temp<N:
    #     for i in range(N-1,0,-1):
    #         for j in range(0,N):
    #             if b_2048[i][j]==0:                
    #                 b_2048[i][j]=b_2048[i-1][j]
    #                 b_2048[i-1][j]=0
    #     temp+=1
    # #### Left 일떄 ######
    # # for i in range(0,N-1,1):
    # #     for j in range(N):
    # #         if b_2048[j][i]==0:                
    # #             b_2048[j][i]=b_2048[j][i+1]
    # #             b_2048[j][i+1]=0
    # # #### Right 일떄 ######
    # # for i in range(N-1,0,-1):
    # #     for j in range(N):
    # #         if b_2048[j][i]==0:                
    # #             b_2048[j][i]=b_2048[j][i-1]
    # #             b_2048[j][i-1]=0
    
        