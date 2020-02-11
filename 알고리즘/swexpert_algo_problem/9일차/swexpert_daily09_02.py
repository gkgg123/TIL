for tc in range(1,11):
    M=int(input())

    str_list=[list(input()) for i in range(8)]
    cnt=0
    for j in range(8):
        for t in range(8-M+1):
            for k in range(M//2):
                if str_list[j][k+t]!=str_list[j][M-8-1-k+t]:
                    break
            else:
                cnt+=1

    for j in range(8):
        for t in range(8-M+1):
            for k in range(M//2):
                if str_list[k+t][j]!=str_list[M-8-1-k+t][j]:
                    break
            else:
                cnt+=1
    print(cnt)

