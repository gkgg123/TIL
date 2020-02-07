import sys
sys.setrecursionlimit(10**6)
sys.stdin=open("ladder.txt",'r')

def ladder(x,y):
    if x==99:
        return cnt[0]
    if 0<=x<100 and 0<=y<100:
        ry=y+1
        ly=y-1 
        if 0<=ry<100 and li[x][ry]==1 :
            while li[x][ry]!=0:
                cnt[0]+=1
                ry=ry+1
                if ry>99:
                    break
            ladder(x+1,ry-1)
            
        elif 0<=ly<100 and li[x][ly]==1:
            while li[x][ly]!=0:
                cnt[0]+=1
                ly=ly-1
                if ly<0:
                    break
            ladder(x+1,ly+1)
        else:
            cnt[0]+=1
            ladder(x+1,y)
    


for tc in range(1,11):
    T=int(input())
    li=[list(map(int,input().split())) for j in range(100)]
    total=[]
    min_val=[0,99999999]

    for i in range(100):
        if li[0][i]==1:
            cnt=[0]
            ladder(0,i)
            if min_val[1]>cnt[0]:
                min_val[1]=cnt[0]
                min_val[0]=i

    print(min_val)


