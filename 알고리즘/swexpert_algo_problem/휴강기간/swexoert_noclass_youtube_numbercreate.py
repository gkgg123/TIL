import sys
sys.stdin=open('text.txt','r')

### dfs를 이용해서 푼 방법을 찾았고, 그걸 복습하면서 짠 코드이다.

### 각 연사자들의 개수를 따로 받아들인뒤,
### 전부 검사하는 재귀함수를 이용했다.
### 각 연산자가 0보다 클시 각각 재귀함수를 써서 모든 경우의 수를 구했고
### 마지막에 계산된값이 최대값인지 최소값인지 구분해서 저장하는식으로 풀었다.
def calc(num,p,mi,mu,di,k):
    global max_number
    global min_number
    if k==N:
        if max_number<num:
            max_number=num
        if min_number>num:
            min_number=num
        return
    nn=arr[k]

    if p>0:
        calc(num+nn,p-1,mi,mu,di,k+1)
    if mi>0:
        calc(num-nn,p,mi-1,mu,di,k+1)
    if mu>0:
        calc(num*nn,p,mi,mu-1,di,k+1)
    if di>0:
        calc(int(num/nn),p,mi,mu,di-1,k+1)
    





T=int(input())
for tc in range(1,T+1):
    N=int(input())
    plus,minus,multiple,divide=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    


    max_number=-10000000000
    min_number=1000000000
    first=arr[0]
    calc(first,plus,minus,multiple,divide,1)
    print('#{} {}'.format(tc,(max_number-min_number)))
    