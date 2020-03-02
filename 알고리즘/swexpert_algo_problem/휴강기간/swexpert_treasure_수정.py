import collections 
### 보물상자 비밀번호는 하나씩 바꿔주는 것인데 중복을 피하기 위해 set을 쓰고 쉽게 하기 위해서
### collection import 해서 rotate를 썼다.

T=int(input())

for tc in range(1,T+1):
    N,K=map(int,input().split())
    result=set()
    M=N//4                    ### M은 각면의 길이이다.
    q=collections.deque()
    q.extend(list(input()))  ## input을 넣어주는데 extend를 하여 하나의 list 형태로 했다.
    while True:
        cnt=0
        for i in range(4):  ## 총 4면에 대해서 비밀번호를 만들어 줘야하기 때문에 range(4)를 했다.
            temp=''         ## 해당 면의 비밀번호를 임시저장하기 위해 temp라는 빈 str를 만들어줬다.
            for j in range(M):       ### 그리고 해당면의 길이만큼 반복하면서
                temp+=q[M*i+j]       #### 그 면에 있는 16진수 숫자를 만들어줬다.
            if temp not in result:   ### 그리고 result라는 set에 없으면, temp를 추가해주었다.
                result.add(temp)
                cnt+=1               ### 이거는 전부 중복되어서 한번도 안들어오면
        if cnt==0:                   ### 여기서 break를 위해 만들었는데
            break                    ### 어차피 면은 4면밖에 없으므로, rotate를 M만큼만 하면 그냥 탈출하게 해도 된다.
        else:
            q.rotate(1)
    total=[]                         ### 그렇게 된것을 16진수로 바꿔줘야하는데
    for k in result:
        total.append(int(k,16))
    total.sort(reverse=True)
    print('#{} {}'.format(tc,total[K-1]))
    