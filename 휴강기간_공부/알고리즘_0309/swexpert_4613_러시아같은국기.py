import sys
sys.stdin=open('러시아.txt','r')


def dfs(arr,cnt,ind):
    if ind==3 and sum(arr)==N:   ### 배분해주기 위한 함수이다.
        result.append(arr[:])   ### 만약 N=4 이면 
        return                  ### W,B,R은 [1,1,2] [1,2,1],[2,1,1]이런식으로 배분을 해야한다. 그러기 위한 함수이다.
    elif ind==3:                ### 재귀를 통해 만들어주고, 끝까지 오고 그 합이 N과 같을때에만 제대로 배분이 된것이다.
        return
    temp=0
    while temp<=cnt:
        a=arr[:]
        a[ind]+=temp
        dfs(a,cnt-temp,ind+1)
        temp+=1        
        
T=int(input())



for tc in range(1,T+1):
    N,M=map(int,input().split())
    
    a=[list(input()) for _ in range(N)]
    count=[1,1,1]
    total=N-3
    result=[]

    min_value=999999
    dfs(count,total,0)
    for k in result:
        cnt=0
        t1=k[0]-1   ### 구해진 배분에서 그 범위를 정해주기 위해서이다.W
        t2=k[1]+t1  ### B
        t3=k[2]+t2  ### R의 순이다.
        for i in range(t1+1):
            for j in range(M):
                if a[i][j]!='W':
                    cnt+=1
        for i in range(t1+1,t2+1):
            for j in range(M):
                if a[i][j]!='B':
                    cnt+=1
        for i in range(t2+1,t3+1):
            for j in range(M):
                if a[i][j]!='R':
                    cnt+=1
        if cnt<min_value:
            min_value=cnt

    print('#{} {}'.format(tc,min_value))