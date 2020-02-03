import sys
sys.stdin=open("swexpert_daily03.txt",'r')

# for test_case in range(1,11):
#     t=int(input())
#     b=[[0 for col in range(100)] for row in range(100)]
#     max_value=0
#     for i in range(100):
#         b[i][:]=map(int,input().split())
#     cross_sum1=[]
#     cross_sum2=[]
    
#     for i in range(100):
#         temp1=sum(b[i][:])
#         temp2=[]
#         for j in range(100):
#             temp2.append(b[j][i])
#         temp2_sum=sum(temp2)
        
#         cross_sum1.append(b[i][i])
#         cross_sum2.append(b[i][100-i-1])
#         if temp1>max_value:
#             max_value=temp1
#         if temp2_sum>max_value:
#             max_value=temp2_sum
#     if sum(cross_sum1)>max_value:
#         max_value=cross_sum1
#     if sum(cross_sum2)>max_value:
#         max_value=cross_sum2
#     print('#{} {}'.format(t,max_value))
    
for test_case in range(1,11):
    t=int(input())
    b=[list(map(int,input().split())) for i in range(100)]
    max_value=0
    cross_sum1=0
    cross_sum2=0 
    for i in range(100):
        temp1=sum(b[i][:])
        temp2=0
        for j in range(100):
            temp2+=b[j][i]        
        cross_sum1+=b[i][i]
        cross_sum2+=b[i][100-i-1]
        if temp1>max_value:
            max_value=temp1
        if temp2>max_value:
            max_value=temp2
    if cross_sum1>max_value:
        max_value=cross_sum1
    if cross_sum2>max_value:
        max_value=cross_sum2
    print('#{} {}'.format(t,max_value))
    
