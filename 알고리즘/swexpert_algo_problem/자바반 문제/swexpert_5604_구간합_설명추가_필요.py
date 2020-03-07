import sys
sys.stdin=open('구간합.txt','r')
T=int(input())
### 구간합을 구현하는데에 힘이 들었다.
### 다른 사람들은 2개의 격차를 한번에 구해서 구했겠지만,
### 그게 어려워서 1부터 A-1까지의 구간합을 구하고,
### 1부터 B까지의 구간합을 구해 빼주었다.
def calc(n):
    re=0
    cnt=1   ### cnt는 계수라고 보면 된다. 일의 자리수 10의 자리수를 나타내는 역할이라 보면 된다.
    while n!=0:
        while n%10 !=9:
            for i in str(n):
                re=re+int(i)*cnt          ### 만약 32이란 숫자가 있다면, 일의 자리 숫자가 0~9까지가 총 3번 반복되고, 
            n-=1                          ###  0,1,2가 추가 됨을 알 수있다.
        if n<10:                          ### 예를 하나 더 들어 158 이란 숫자가 있으면,
            for i in range(n+1):          #### 0~9까지 숫자가 총 15번 반복되고, 8,7,6,5,4,3,2,1,0 의 숫자가 추가 됨을 알 수 있다.
                re=re+i*cnt
            return re
        else:
            for i in range(10):
                re=re+(n//10+1)*cnt*i
        cnt*=10
        n=n//10
    return re








for tc in range(1,T+1):
    A,B=map(int,input().split())

    a=calc(A-1)
    b=calc(B)
    print('#{} {}'.format(tc,b-a))