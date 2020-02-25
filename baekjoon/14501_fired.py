### 동적계획법을 이용해 풀었다. ####
### 먼저 각 날짜마다 해당 날짜을 일했을때의 이득을 dp에 저장해주었다.
### 그리고 해당날짜와 그전 날짜 j에 일했을때 얻을수 있는 이득과 + 해당날짜의 이득을 더한것과 dp[i]를 비교하여 더 큰값을
### dp에 계속 저장해주었다.
### 그리고 저장된 dp에서 i번째 날에 일을했을때 최종날짜를 넘기는 dp들을 제외한 나머지 날짜들의 최대값을 구해
### 출력해주었다.

N=int(input())

arr=[list(map(int,input().split())) for i in range(N)]

days=[0]
benefis=[0]
dp=[0]
for i in range(N):
    days.append(arr[i][0])
    benefis.append(arr[i][1])
    dp.append(arr[i][1])

for i in range(2,N+1):
    for j in range(1,i):
        if i-j>=days[j]:
            dp[i]=max(dp[j]+benefis[i],dp[i])

for i in range(1,N+1):
    if i+days[i]>N+1:
        dp[i]=0
print(max(dp))