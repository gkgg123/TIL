import sys
sys.stdin=open('swexpert_daily11_stack01.txt','r')
def bfs(st):
    stack=st[:]
    result=[]
    result.extend(stack)
    for i,v in enumerate(visit):
        if v==0 and i!=0 and not in result:
            result.append(i)
    while stack:
        temp=stack.pop()
        if visit[temp]==0 and dist.get(temp):
            stack.extend(dist[temp])
        if visit[temp]==1:
            if dist.get(temp):
                stack.extend(dist[temp])
            if temp not in result:
                result.append(temp)
        else:
            visit[temp]-=1                    
    return result
        





for tc in range(1,5):
    v,e=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    dist={}
    visit=[0]*(v+1)
    for i in range(len(arr)//2):
        dist[arr[2*i]]=arr[2*i+1]
    for keys in dist.keys():
        temp=[]
        for i in range(len(arr)//2):
            if arr[2*i]==keys:
                temp.append(arr[2*i+1])
        dist[keys]=temp
    for i in range(len(arr)//2):
        visit[arr[2*i+1]]+=1
    pa=[]
    ch=[]

    for i in range(len(arr)//2):
        pa.append(arr[2*i])
        ch.append(arr[2*i+1])
    start=list(set(pa)-set(ch))

    
    print('#{}'.format(tc),end=' ')
    rr=bfs(start)
    for i in rr:
        print(i,end=' ')
    print('')