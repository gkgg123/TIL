import itertools
### 처음 풀었던 방식이다. 
### operator의 개수를 구한뒤, 각 operator마다 곱해주었고,
### 그것을 모아서 순열을 만들었다.
### 그리고 각순열을 전부계산 돌리면서 최대값과 최소값을 구해주었다. 
N=int(input())
arr=list(map(int,input().split()))
operator=list(map(int,input().split()))

operator_str='+-*/'
operator_list=[]
for i in range(4):
    for j in range(operator[i]):
        operator_list.append(operator_str[i])

operator_per=itertools.permutations(operator_list)
min_total=99999999999
max_total=-1000000000

for i in operator_per:
    temp=arr[0]
    for k in range(N-1):
        if i[k]=='+':
            temp+=arr[k+1]
        elif i[k]=='-':
            temp-=arr[k+1]
        elif i[k]=='*':
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
