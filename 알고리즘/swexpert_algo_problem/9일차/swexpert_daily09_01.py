for tc in range(1,11):
    T=int(input())

    str_list=[list(input()) for i in range(100)]
    cnt=0
    M=1
    max_len=0
    result=[]
    while M<=100:
        for j in range(100):
            for t in range(100-M+1):
                for k in range(M//2):
                    if str_list[j][k+t]!=str_list[j][M-100-1-k+t]:
                        break
                else:
                    result=str_list[j][t:M+t]
                    if len(result)>max_len:
                        max_len=len(result)                        
        M+=1
    print(result)
    print(max_len)
    M=0
    while M<=100:
        for j in range(100):
            for t in range(100-M+1):
                result=[]
                for k in range(M//2):
                    if str_list[k+t][j]!=str_list[M-100-1-k+t][j]:
                        break
                else:
                    for ttt in range(M):           
                        result.append(str_list[t+ttt][j])
                    if len(result)>max_len:
                        print(j)
                        max_len=len(result)
                        print(result)
        M+=1
    
    print('#{} {}'.format(tc,max_len))

