T=int(input())

for test_case in range(1,T+1):
    N,M=map(int,input().split(' '))
    num=list(input().split(' '))
    number=[]
    for j in num:
        if j.isdigit():
            number.append(int(j))
    temp_sum=0
    for i in range(0,N-M+1):
        if i==0:
            max_sum=sum(number[i:i+M])
            min_sum=sum(number[i:i+M])
        else:
            temp_sum=sum(number[i:i+M])
            if max_sum<temp_sum:
                max_sum=temp_sum
            elif min_sum>temp_sum:
                min_sum=temp_sum
    total=max_sum-min_sum
    print('#{} {}'.format(test_case,total))

