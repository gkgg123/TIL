T=int(input())

for tc in range(1,T+1):
    arr=list(input())
    N=len(arr)  ### 문자열의 길이
    insert_list=[0]*(N+1)   ### 어느 위치에 - 을 몇개나 넣는지 알기 위해서 만들어준 list
    H=int(input())
    insert_index=list(map(int,input().split())) 

    for k in insert_index: ## 들어온 위치에 따라 숫자를 하나씩 세준다.
        insert_list[k]+=1
    result=''

    for i in range(N):
        result=result+insert_list[i]*'-'  ## 개수만큼 -을 곱해서 더해준다.
        result+=arr[i]
    result+=insert_list[N]*'-'  ### 마지막것만 따로 해준다.

    print('#{} {}'.format(tc,result))