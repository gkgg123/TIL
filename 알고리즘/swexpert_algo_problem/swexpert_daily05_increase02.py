T=int(input())

for tc in range(1,T+1):
    n=int(input())
    num=list(map(int,input().split()))
    a=[]

    for i in range(n):
        for j in range(i+1,n):
            a.append(str((num[i]*num[j])))
    max_n=0
    a=sorted(a)
    print(a)
    for val in a:        
        if len(val)>1:
            for k in range(len(val)-1):
                if val[k]>val[k+1]:
                    break
            else:
                max_n=val


    if max_n==0:
        print('#{} -1'.format(tc))
    else:
        print('#{} {}'.format(tc,max_n))
            
            