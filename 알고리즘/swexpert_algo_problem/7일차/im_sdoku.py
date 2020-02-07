T=int(input())

for tc in range(1,T+1):
    sdoku=[list(map(int,input().split())) for i in range(9)]
    sus=1
    sero_sum=0
    block_sum=0
    for i in range(9):
        if sum(sdoku[i])!=45:
            sus=0
            
            break
        for j in range(9):
            sero_sum+=sdoku[j][i]
        
        if sero_sum!=45:
            sus=0
            
            break        
        sero_sum=0
        
    for i in range(0,9,3):
        for j in range(0,9,3):
            for k in range(3):
                    for t in range(3):
                        block_sum+=sdoku[i+k][j+t]
            
            if block_sum!=45:
                
                sus=0
                
                break
            block_sum=0
    print('#{} {}'.format(tc,sus))

