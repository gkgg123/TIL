def search(ar,cnt):
    end=ar[cnt][1]
    while True:
        start=25
        temp=True
        for i in ar:
            if i[0]>=end:
                if start>i[1]:
                    start=i[1]
                    temp=False
        end=start
        if temp:
            break
        else:
            cnt+=1

    return cnt+1



T=int(input())



for tc in range(1,1+T):
    N=int(input())
    arr=[]
    for i in range(N):
        temp=list(map(int,input().split()))
        arr.append(temp)
    arr.sort(key=lambda x : x[1])
    result=search(arr,0)
    print('#{} {}'.format(tc,result))