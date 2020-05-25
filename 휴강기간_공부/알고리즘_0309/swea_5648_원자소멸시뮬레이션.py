T=int(input())
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def move(ar):
    remove_list=[]
    for i in range(len(ar)):
        ar[i][0]=ar[i][0]+dx[ar[i][2]]
        ar[i][1]=ar[i][1]+dy[ar[i][2]]
        if ar[i][0]<-2001 or ar[i][0]>2001 or ar[i][1]>2001 or ar[i][1]<-2001:
            remove_list.append(i)
    remove_list.reverse()
    for k in remove_list:
        del ar[k]

def find(ar):
    global energy
    result={}
    for i in ar:
        temp=(i[0],i[1])
        if result.get(temp):
            result[temp].append(i)
        else:
            result[temp]=[i]
    re_li = []

    for i in result:
        if len(result[i])>1:
            item = result[i]
            for en in item:
                energy += en[3]

        else:
            item = result[i]
            re_li.append(item[0])
    return re_li



    











for tc in range(1,T+1):
    N=int(input())
    arr=[]

    ### x,y,방향(0,1,2,3)(상,하,좌,우),K
    for _ in range(N):
        temp = list(map(int,input().split()))
        temp[0] = temp[0]*2
        temp[1] = temp[1]*2
        arr.append(temp)
    cnt=0
    energy=0
    while cnt<4000:
        move(arr)
        arr=find(arr)
        cnt+=1
        if len(arr)<2:
            break
    
    print('#{} {}'.format(tc,energy))
