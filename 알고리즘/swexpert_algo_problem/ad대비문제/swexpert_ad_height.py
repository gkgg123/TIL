import sys
import itertools
#### 장훈이의 높은 선반 #####
sys.stdin=open('height.txt','r')

T=int(input())

for tc in range(1,T+1):
    N,total=list(map(int,input().split()))
    saram=list(map(int,input().split()))

    result=[]

    for i in range(1,N+1):
        temp=itertools.combinations(saram,i)
        ### itertools 중에 콤비네이션 즉 조합을 지원해주는 내부함수가 있다. 그걸 이용하여 풀었다.
        ### 모든 경우의 수에 대한 조합이 temp에 저장이 된다.
        ### 이거는 튜플형태로 저장되므로
        ### 밑에서 for 문을 사용하여 해당 튜플의 전체합을 구해주고
        ### 주어진 total값과 가장 차이가 적은 값을 찾아냈다.
        for j in temp:
            temp_sum=0
            for k in j:
                temp_sum+=k
            result.append(temp_sum)
    min_value=999999
    for tt in result:
        min_temp=tt-total
        if min_temp>=0 and min_temp<min_value:
            min_value=min_temp
    print('#{} {}'.format(tc,min_value))