T=int(input())

for tc in range(1,T+1):
    ss=list(input())
        

    stack=[]

    while True:
        tt=len(ss)
        for i in range(tt-1):
            if ss[i]==ss[i+1]:                
                del ss[i+1]
                del ss[i]
                break
        else:
            break

    print('#{} {}'.format(tc,len(ss)))
