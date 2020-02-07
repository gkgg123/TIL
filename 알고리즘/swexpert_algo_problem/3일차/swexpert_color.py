T=int(input())

for test_case in range(1,T+1):
    tt=int(input())
    red=[[0 for col in range(10)] for row in range(10)]
    blue=[[0 for col in range(10)] for row in range(10)]
    cnt=0
    for k in range(1,tt+1):
        temp=list(map(int,input().split()))
        for i in range(temp[0],temp[2]+1):
            for j in range(temp[1],temp[3]+1):
                if temp[4]==1:
                    red[i][j]=1
                else:
                    blue[i][j]=2
    for ind1 in range(10):
        for ind2 in range(10):
            if red[ind1][ind2]+blue[ind1][ind2]==3:
                cnt+=1
                    

    print(cnt)