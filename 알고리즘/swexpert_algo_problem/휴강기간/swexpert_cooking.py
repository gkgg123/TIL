from itertools import combinations

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    sub_N=N//2
    arr=[list(map(int,input().split())) for _ in range(N)]
    row=[sum(i) for i in arr]
    col=[sum(i) for i in zip(*arr)]

    new_arr=[i+j for i,j in zip(row,col)]
### 크기가 크니 그냥 4*4 행렬로 가정하고 계산하겠다.
### a b c d ###
### e f g h ###
### i j k l ###
### m n o p ###
### 라는 행렬이 있다고 하자..
### 처음에 같은행과 열의 합을 구한다.
### 1행과 1열의 합 list1 =a+b+c+d+a+e+i+m
### 2행과 2열의 합 list2 =e+f+g+h+b+f+j+n
### 3행과 3열의 합 list3 =i+j+k+l+b+f+j+n
### 4행과 4열의 합 list4 =m+n+o+p+d+h+l+p
### 를 정리해줬다.
### 그리고 저 행렬의 모든 합은 a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p 이다.
### 그리고 여기서 가정을 하겠다. 1번째 재료와 2번째 재료를 같이 썼다고 하자 
### 그러면 list1과 list2를 더한값을 모든합에서 빼준다.
### 먼저 list1과 list2를 더해보면
### 2a+2b+c+d+2e+2f+g+h+i+j+m+n 이다 이걸 모든합에서 빼주면
### (k+l+o+p)-(a+b+e+f)가 된다. 
### 이건 그냥 우리가 1,2재료을 선택하고 3,4재료을 선택했을때와 결과물과 똑같이 된다.
### 이걸 하나하나 인덱스에 접근해서 계산하기에는 시간이 걸리니깐 이걸 같은 행과열을 합을 하나로 정해놓고
### 그걸 전체에서 빼주면 자연스럽게 우리가 구하고자 하는 차이가 된다. 

    allstat=sum(new_arr)//2
    new_arr.sort()
    new_arr[1::2]=new_arr[-1::-2]
    allstat -= new_arr[-1]
    mins=99999999

    for l in combinations(new_arr[:-1],sub_N-1):
        mins=min(mins,abs(allstat-sum(l)))

        if not mins:
            break
    print('#{} {}'.format(tc,mins))