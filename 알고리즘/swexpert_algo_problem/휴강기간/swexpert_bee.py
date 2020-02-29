import sys
### 그냥 단순하게 모든 조합을 하나하나 다 구해서 해도 되지만, 정해진 범위의 합을 구한 뒤 C가 넘어가면
### 부분집합으로 최대의 값을 가지는 것을 구해 그것을 저장해 주었다.
sys.stdin=open('bee.txt','r')

T=int(input())

for tc in range(1,T+1):
    N,M,C=map(int,input().split())

    arr=[list(map(int,input().split())) for _ in range(N)]

    
    square_list=[[0]*N for _ in range(N)]
    max_value=0
    for i in range(N):
        for j in range(N-M+1):
            temp_list=arr[i][j:j+M] ### 벌집을 슬라이싱 해주는 과정이다.
            temp_max=0
            if sum(temp_list)>C:  ### 만약에 용량을 뛰어넘을 경우
                for k in range(1,1<<M):
                    temp_sum=0
                    temp_square=0
                    for t in range(M):
                        if k&(1<<t):  ### 부분집합을 구해
                            temp_sum+=temp_list[t]
                            temp_square+=temp_list[t]**2
                    if temp_sum<=C and temp_square>temp_max:  ### 저장용량을 넘지않으면서 최대값인걸 구해주었다.
                        temp_max=temp_square
            else:
                for t in range(M):
                    temp_max+=temp_list[t]**2
            square_list[i][j]=temp_max


    result=[]
    for i in range(N):
        for j in range(N):
            result.append(square_list[i][j])
    for i in range(len(result)-M):
        for j in range(i+M,len(result)):  ### 1차원배열로 바꾼뒤 하나하나 선택하면서 최대값을 구해주었다.
            if max_value<result[i]+result[j]:
                max_value=result[i]+result[j]
    print('#{} {}'.format(tc,max_value))


    
