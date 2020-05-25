T=int(input())
def find(ar,num):
    left =0
    right = N-1
    flag = -1
    while True:
        m = (left+right)//2
        if num == ar[m]:
            return 1
        else:
            if flag == -1:
                if num>ar[m]:
                    flag = True
                    left = m +1
                else:
                    flag = False
                    right = m-1
            else:
                if num>ar[m]:
                    if flag:
                        return 0
                    else:
                        flag = True
                        left = m +1
                else:
                    if flag:
                        flag = False
                        right = m -1
                    else:
                        return 0
            





for tc in range(1,T+1):
    N,M=map(int,input().split())
    list_a=list(map(int,input().split()))
    list_b=list(map(int,input().split()))
    list_a.sort()
    cnt=0
    for i in range(M):
        if list_b[i] in list_a:
            cnt += find(list_a,list_b[i])
    print('#{} {}'.format(tc,cnt))