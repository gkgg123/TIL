



T=int(input())

for tc in range(1,T+1):
    arr=list(input())
    left_list=[]
    lazer=[]
    total=[]
    for i in range(len(arr)):
        if arr[i]=='(':
            left_list.append(i)
        else:
            temp=left_list.pop()
            if i-temp==1:
                lazer.append((i+temp)/2)
            else:
                total.append([temp,i])
    cnt=0
    for i in total:
        cnt+=1
        for j in lazer:
            if i[0]<j<i[1]:
                cnt+=1
    print('#{} {}'.format(tc,cnt))