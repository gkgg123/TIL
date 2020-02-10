import sys
sys.stdin=open('problem.txt','r')


T=int(input())

for tc in range(1,T+1):
    N=int(input())
    farm=[list(map(int,input().split())) for i in range(N)]
    res=9999999
    farm_c=0
    for y_line in range(1,N):
        farm_c=0
        for i in range(N):            
            farm_c+=sum(farm[i][y_line:5])        
        for x_line in range(1,N):
            farm_b=0
            farm_a=0
            for k in range(0,x_line):                
                farm_a+=sum(farm[k][0:y_line])
            for j in range(N-x_line):                
                farm_b+=sum(farm[N-1-j][0:y_line])       
            if (max(farm_a,farm_b,farm_c)-min(farm_a,farm_b,farm_c))<res:
                res=max(farm_a,farm_b,farm_c)-min(farm_a,farm_b,farm_c)
    print(res)

