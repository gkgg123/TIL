T=int(input())

for tc in range(1,T+1):
    N=int(input())
    numbers=[list(input().split()) for i in range(N)]
    # print(numbers)
    sum_90=[]
    sum_180=[]
    sum_270=[]

    for i in range(N):
        temp=''
        for j in range(N-1,-1,-1):
            temp+=numbers[j][i]
        sum_90.append(temp)
    for i in range(N-1,-1,-1):
        temp=''
        for j in range(N-1,-1,-1):
            temp+=numbers[i][j]
        sum_180.append(temp)
    for i in range(N-1,-1,-1):
        temp=''
        for j in range(N):
            temp+=numbers[j][i]
        sum_270.append(temp)
    
    print("#{}".format(tc))
    for i in range(N):
        print(sum_90[i],end=' ')
        print(sum_180[i],end=' ')
        print(sum_270[i])
    
    
    
