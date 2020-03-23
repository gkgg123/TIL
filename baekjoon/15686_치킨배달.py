import itertools
def direction(ch,ho):
    return abs(ch[0]-ho[0])+abs(ch[1]-ho[1])

N,M=map(int,input().split())

arr=[list(input().split()) for _ in range(N)]
home=[]
chi=[]
for i in range(N):
    for j in range(N):
        if arr[i][j]=='1':
            home.append((i,j))
        elif arr[i][j]=='2':
            chi.append((i,j))
k=itertools.combinations(chi,M)
result=99999999999999999999
for t in k:
    temp=0
    for di in home:
        d=99999
        for down in t:
            d=min(d,direction(down,di))
        temp+=d
    result=min(result,temp)
print(result)
            


