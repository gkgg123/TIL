def part_sum(n,total_sum):
    a=list(range(1,13))
    cnt=0
    for i in range(2**12):
        sub_set=[]
        flag=bin(i)[2:].zfill(12)
        temp=sum(list(map(int,flag)))
        if temp==n:
            sub_set=[a[j] for j in range(len(a)) if flag[j]=='1']
            if sum(sub_set)==total_sum:
                cnt+=1
    return cnt

T=int(input())

for test_case in range(1,T+1):
    a,b=map(int,input().split())

    result=part_sum(a,b)

    print('#{} {}'.format(test_case,result))


#### 좀 더 쉬운 방법 #### 조합을 이용하자 ####
# from itertools import combinations


# T=int(input())

# for tc in range(1,T+1):
#     items=list(range(1,13))
#     n,num=map(int,input().split())
#     a=combinations(items,n)
#     cnt=0
#     for i in a:
#         if sum(i)==num:
#             cnt+=1
#     print('#{} {}'.format(tc,cnt))