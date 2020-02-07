import sys
sys.stdin=open("maxmin_1day.txt","r")
T=int(input())
for test_case in range(1,T+1):
    rep=int(input())
    numbers=list(map(int,input().split(' ')))
    max_number=numbers[0]
    min_number=numbers[0]
    for i in range(1,rep):
        if max_number<numbers[i]:
            max_number=numbers[i]
        elif min_number>numbers[i]:
            min_number=numbers[i]
    result=max_number-min_number
    
    print('#{} {}'.format(test_case,result))