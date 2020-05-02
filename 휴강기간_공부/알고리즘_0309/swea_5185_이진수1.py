T=int(input())

for tc in range(1,T+1):
    N,M=input().split()
    result=''
    for i in M:
        M_deci=int(i,16)          ### 16진수를 10진수로 바꿔준다.
        M_bit=format(M_deci,'b')  ### 2진수로 변환해준다. 0b를 없이 그냥 이진수만 나오게 해주낟.
        if len(M_bit)<4:          ### 길이가 4가 안되면 그만큼 0을 추가해주고, M_bit를 추가해준다.
            for i in range(4-len(M_bit)):
                result+='0'
            result+=M_bit
        else:
            result+=M_bit        ### 4bit이면 그냥 바로 추가해준다.
    print('#{} '.format(tc),end='')
    print(result)               ### 출력
                