import sys
sys.stdin=open('town.txt','r')
T=int(input())

for tc in range(1,T+1):
    N,M=list(map(int,input().split()))
    arr=[list(map(int,input().split())) for i in range(M)]
    total=0
    visit=[0]*(N+1)
    for k in arr:
        visit[k[0]]+=1
        visit[k[1]]+=1
    while arr:
        start=arr.pop(0)
        tt=0
        while tt<M:
            if arr:         
                for ind,val in enumerate(arr):
                    for k in range(0,len(start),2):
                        if val[1]==start[k]:
                            start.insert(k,val[1])
                            start.insert(k,val[0])
                            del arr[ind]
                            break
                        elif val[0]==start[k+1]:
                            start.insert(k+2,val[1])
                            start.insert(k+2,val[0])
                            del arr[ind]
                            break
            else:
                break
            tt+=1
        total+=1
           
    for i in range(1,N+1):
        if visit[i]==0:
            total+=1
    print('#{} {}'.format(tc,total))
                    
