from itertools import permutations
import sys
sys.stdin=open('동훈.txt','r')
T=int(input())

for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for i in range(N)]

    b=permutations(range(0,N))
    max_value=0
    for i in b:
        temp=1
        for j in range(N):
            temp*=arr[j][i[j]]/100
            if temp<max_value:
                break
        if temp>max_value:
            max_value=temp
    
    result=round(max_value*100,6)
    print('#{0} {1:0.6f}'.format(tc,result))