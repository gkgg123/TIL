
T=int(input())


### 암호를 인덱스에 맞춰서 넣어줬다. ####
total=[
'0001101', #0
'0011001', #1
'0010011', #2
'0111101', #3
'0100011', #4
'0110001', #5
'0101111', #6
'0111011', #7
'0110111', #8
'0001011',]


for tc in range(1,T+1):
    N,M=map(int,input().split())

    arr=[list(input()) for _ in range(N)]
    result=[0]*8
    flag=False
    for i in range(N):
        j=M
        ind=7
        while j>7:
            a=''.join(arr[i][j-7:j])   ### 7자리씩 슬라이싱해서 join해서 str로 만들어줬다.
            if a in total:             ### 이게 위의 암호에 있는지 확인해주고,
                result[ind]=total.index(a)   ### 있으면, 해당자리에, total.index를 넣어준다.
                ind-=1                       ### 그리고 자리수는 1을 낮춰주고,
                j-=7                         ### arr의 index는 -7해준다.
                flag=True                    ### 다음 줄을 탐색할 필요가 없으므로, True로 해준다.
            else:
                j-=1
        if flag:
            break
    final_result=0


    ### 암호코드인지 확인해주기 위해, 홀수자리는 *3 짝수자리는 그냥 더해주고, 검증코드는 그냥 더해준다.
    for i in range(8):
        if i==7:
            final_result+=result[i]
        elif i%2==0:
            final_result+=3*result[i]
        else:
            final_result+=result[i]
    ### 10의 배수이면 result의 전체합을 출력해준다.
    if final_result%10==0:
        print('#{} {}'.format(tc,sum(result)))
    else:
        print('#{} 0'.format(tc))


    ### 여기서 중요한점은 한줄씩 탐색을 할때 앞에서부터 탐색을하면 안된다 왜냐하면 이런경우가 발생할수 있다.
    ### 9번이 0001011 6번이 0101111 이다.
    ### 여기서 0001011110001101 이라고 되어있으면 앞에서 탐색할시
    #### 0001011 을 9로 판단하게 되고 110001101 그 뒤를 잘못판단할수 있다.
    ### 이 암호는 끝자리가 전부 1인걸 이용해서 뒤에서부터 탐색을 해줘야한다.








    