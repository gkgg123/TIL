for tc in range(1,11):
    input()
    password=list(map(int,input().split()))
    minus=[-1,-2,-3,-4,-5]
    cnt=0
    while True:
        i=cnt%5 ### 문제에서 5번의 암호생성을 반복하는걸 세기위한 값이다.
        cycle=cnt//5 ## 이건 몇번째 사이클인지 세기 위한것이다.
        index=(cycle*5+i)%8### 이건 사이클과 i값을 이용해 현재 접근해야하는 index값에 접근하기 위함이다.
                            ### 0번째 사이클에 접근하는 인덱스는 0,1,2,3,4
                            ### 1번째 사이클에 접근하는 인덱스는 5,6,7,0,1
                            ### 2번째 사이클에 접근하는 인덱스는 2,3,4,5,6
                            ### modulo 8연산인걸 알수 있다. 그래서 8을 나눈 나머지를 구해주었다.


        password[index]+=minus[i]
        cnt+=1
        if password[index]<=0: ### 만약 0보다 작거나 0보다 작은게 나오면, 그 값을 0으로 바꿔주고 해당 index부터 슬라이싱하면 된다.
            password[index]=0
            break
    print('#{} '.format(tc),end='')
    print(' '.join(map(str,password[index+1:])),end=' ')
    print(' '.join(map(str,password[:index+1])))
