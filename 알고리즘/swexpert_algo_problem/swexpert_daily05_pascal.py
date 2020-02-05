T=int(input())

for tc in range(1,T+1):
    n=int(input())

    Plis=[1]
    lis=[]
    print('#{}'.format(tc))
    for i in range(n):
        if i==0:
            print(1)
        else:
            lis=Plis[:]
            lis.append(0)
            for j in range(i):
                lis[-1-j]+=Plis[-1-j]
            for k in lis:
                print(k,end=' ')
            print(' ')
            Plis=lis[:]

        



