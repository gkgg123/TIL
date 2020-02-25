import sys
import itertools
### itertools를 이용해서 콤비네이션을 통해 팀을 반씩 나누고, 그걸 이용해
### 능력치 차이의 최소값을 구해주었다.

N=int(input())
team=set(range(0,N))
arr=[list(map(int,sys.stdin.readline().split())) for i in range(N)]
b=itertools.combinations(team,N//2)


for i in range(N):
    for j in range(i+1,N):
        arr[i][j]+=arr[j][i]

#############################################
# for i in b:
#     for k in result:
#         if len(set(i)-set(k))==N//2:
#             break
#     else:
#         result.append(i)                                  
# 오히려 중복을 제거할려고 한 부분 때문에 시간초과가 계속 떴다.
##############################################################
min_number=999999999
for i in b:
    other_team=list(team-set(i))
    a_team=0
    b_team=0
    for k in range(N//2):
        for j in range(k+1,N//2):
            a_team+=arr[i[k]][i[j]]
            b_team+=arr[other_team[k]][other_team[j]]
    temp=abs(a_team-b_team)
    if temp<min_number:
        min_number=temp
print(min_number)