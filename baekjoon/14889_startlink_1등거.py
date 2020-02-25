### 백준 wider93 의 코드를 복습하는 거###
from itertools import combinations
N = int(input()) // 2
M = 2*N
stat = [list(map(int, input().split())) for _ in range(M)]
row = [sum(i) for i in stat]
col = [sum(i) for i in zip(*stat)]
### 해당 작업은 각 행과 열의 합을 구해주기 위함이다. ####
### i번의 사람이 참여하는 합들을 더해준것이다. ###

newstat = [i+ j for i, j in zip(row, col)]
#### 그리고 이 부분에서는 각각 구한 행과 열의 값을 더해주었다. ####
allstat = sum(newstat) // 2
#### 그리고 행렬의 전체 합을 구해준것이다. #####

newstat.sort()
newstat[1::2] = newstat[-1::-2]
### 아마 추측하기로 이부분은 계산량을 줄여주기 위해서 순서를 바꿔준것 같다.
allstat -= newstat[-1]
### 이 문제는 a팀에 1,2,3,4 b팀에 5,6,7,8이 된거랑
### a팀에 5,6,7,8 b팀에 1,2,3,4이 되어도 결과가 같기 때문에
### 한명을 한팀에 정해놓고 하는것이 계산량이 줄어주기 때문에 이렇게 한것 같다.


### 아마 이렇게 행과열을 합해준것은 다음과 같은 과정이 가능하기 때문인것 같다.. #####
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
### 그리고 여기서 가정을 하겠다. 1팀과 2팀이 같이 했다고 하자 
### 그러면 list1과 list2를 더한값을 모든합에서 빼준다.
### 먼저 list1과 list2를 더해보면
### 2a+2b+c+d+2e+2f+g+h+i+j+m+n 이다 이걸 모든합에서 빼주면
### (k+l+o+p)-(a+b+e+f)가 된다. 
### 이건 그냥 우리가 1,2팀을 선택하고 3,4팀을 선택했을때와 결과물과 똑같이 된다.
### 이걸 하나하나 인덱스에 접근해서 계산하기에는 시간이 걸리니깐 이걸 같은 행과열을 합을 하나로 정해놓고
### 그걸 전체에서 빼주면 자연스럽게 우리가 구하고자 하는 차이가 된다. 
### 이러한 점을 이용해 계산시간을 줄이고, 빠른 결과물을 나타낸것 같다.
mins = 65535
for l in combinations(newstat[:-1], N-1):
    mins = min(mins, abs(allstat - sum(l)))
    if not mins:
        print(0)
        break
else:
    print(mins)