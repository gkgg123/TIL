T=int(input())

for test_case in range(1,T+1):
    le=int(input())
    result=[0]*10
    temp=list(map(int,input().split()))

    for i in range(5):
        temp=sorted(temp)
        result[2*i]=temp.pop()
        result[2*i+1]=temp.pop(0)
    print('#{}'.format(test_case),end=' ')
    for j in result:
        print(j,end=' ')
    print('')



