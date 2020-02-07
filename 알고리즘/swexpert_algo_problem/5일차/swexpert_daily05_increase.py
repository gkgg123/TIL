T=int(input())

for tc in range(1,T+1):
    n=int(input())
    num=list(map(int,input().split()))
    a=[]

    for i in range(n):
        for j in range(i+1,n):
            a.append((num[i]*num[j]))
    result=[]

    for val in a:
        if val//10!=0:
            fail=0
            sto=val
            start=val%10
            val=val//10
            while val>0:
                temp=val%10
                if temp>start:
                    fail+=1
                val=val//10
                start=temp
            if fail==0:
                result.append(sto)

    if len(result)==0:
        print('#{} -1'.format(tc))
    else:
        print('#{} {}'.format(tc,max(result)))
            
            
        