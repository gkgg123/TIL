import itertools
def direction(x,y):
    global home

    return [abs(x-h[0])+abs(y-h[1]) for h in home]

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
    d=[direction(*chi) for chi in t]  #### 집을 하나씩 순회하면서 하나의 치킨집 chi를 direction 함수에 넣어
                                      #### 전체 집과 chi와의 거리를 저장해준다
                                      #### 즉 치킨집1 =[home1 home2 home3 hom4]
                                      #####   치킨집2 =[home1 home2 home3 hom4]
                                      #형식으로 저장된다 그래서 이걸 zip으로 각 home끼리 묶어주고 그중에서 최저값을 구해서
                                      #  저장된 result와 비교를 하여 더 작은값으로 바꿔준다. 
    temp = sum([min(col) for col in zip(*d)])
    result=min(result,temp)
print(result)
            


