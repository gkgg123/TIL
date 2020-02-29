import sys
sys.stdin=open("card_buy.txt",'r')

n=int(input())
card=[0]
card+=list(map(int,input().split()))
dp=[0]*(n+1)

dp[1]=card[1]
dp[2]=max((card[2],card[1]*2))

for i in range(3,n+1):
    dp[i]=card[i]
    for j in range(1,i//2+1):
        dp[i]=max(dp[i],dp[j]+dp[i-j])


print(dp[n])