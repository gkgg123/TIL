import sys
sys.setrecursionlimit(10**7)
# def f(n,k):
#     if n==1:
#         return 1
#     else:
#         return ((f(n-1,k)+k-1) % n)+1
### 재귀로 풀다보니 재귀제한에 걸려 문제가 되서 ## 반복문을 사용했다.


N,K=list(map(int,sys.stdin.readline().split()))
R=1
for i in range(1,N+1):
    R=((R+K-1)%i)+1

print(R)