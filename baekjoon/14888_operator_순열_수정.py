import itertools
### 처음 풀었던 방식보다 더 나은 방식이라 생각한다.
### 각 연산자의 개수를 구하고,
### 연산자를 숫자 1,2,3,4로 구분하여,
### 연산자의 개수만큼 곱해주어 하나의 연산자 리스트를 만들어주었다.
### 그리고 순열을 돌리고 중복된걸 없애기 위해
### set함수를 이용해서 중복을 없애주었다.
### 그리고 그 순열에 맞게 값을 계산해주었다
N=int(input())
arr=list(map(int,input().split()))
plus,minus,multiple,divide=list(map(int,input().split()))

operator_list=[]
operator_list+=[1]*plus
operator_list+=[2]*minus
operator_list+=[3]*multiple
operator_list+=[4]*divide

operator_per=itertools.permutations(operator_list)
operator_set=set()
for k in operator_per:
    operator_set.add(k)

min_total=99999999999
max_total=-1000000000

for i in operator_set:
    temp=arr[0]
    for k in range(N-1):
        if i[k]==1:
            temp+=arr[k+1]
        elif i[k]==2:
            temp-=arr[k+1]
        elif i[k]==3:
            temp*=arr[k+1]
        else:
            if temp<0:
                temp=(temp*-1)//arr[k+1]*-1
            else:
                temp=temp//arr[k+1]
    if max_total<temp:
        max_total=temp
    if min_total>temp:
        min_total=temp
print(max_total)
print(min_total)
