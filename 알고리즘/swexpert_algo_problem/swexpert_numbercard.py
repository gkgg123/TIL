T=int(input())
for test_case in range(1,T+1):
    le=int(input())
    cnt=[0]*10
    number=input()
    max_cnt=0
    max_number=0
    for i in number:
        cnt[int(i)]+=1
    for ind,val in enumerate(cnt):
        if val>=max_cnt:
            max_cnt=val
            max_number=ind

    

    print('#{} {} {}'.format(test_case,max_number,max_cnt))

