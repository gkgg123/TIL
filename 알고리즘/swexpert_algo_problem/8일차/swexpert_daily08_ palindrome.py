import sys

sys.stdin=open('swexpert_daily08_palindrome.txt','r')

T=int(input())

for tc in range(1,T+1):
    N,M=list(map(int,input().split()))

    str_arr=[list(input()) for i in range(N)]
    result=[]
    print(str_arr)


    # for i in range(N-M+1):
    #     if M%2==0:
    for j in range(N):
        for t in range(N-M+1):
            for k in range(M//2):
                if str_arr[j][k+t]!=str_arr[j][M-N-1-k+t]:
                    break
            else:                
                result=str_arr[j][t:M+t]
            
    for j in range(N):
        for t in range(N-M+1):
            for k in range(M//2):
                if str_arr[k+t][j]!=str_arr[M-N-1-k+t][j]:
                    break
            else:
                for ttt in range(M):           
                    result.append(str_arr[t+ttt][j])
    print('#{} '.format(tc),end='')
    print(''.join(result))


