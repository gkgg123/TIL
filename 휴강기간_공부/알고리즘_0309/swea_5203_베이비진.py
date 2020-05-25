def babyjin(li):
    for i in li:
        if li.count(i)>=3:
            return True


    set_li=set(li)
    li_new=list(set_li)
    li_new.sort()

    for i in range(len(li_new)-2):
        pre=li_new[i]
        nex=li_new[i+1]
        net=li_new[i+2]
        if nex==pre+1 and net==pre+2:
            return True
    return False


def battle(ar):
    p1=[]
    p2=[]
    p1.append(ar[0])
    p1.append(ar[2])
    p2.append(ar[1])
    p2.append(ar[3])

    for i in range(4,12):
        if i%2==0:
            p1.append(ar[i])
            p1_result=babyjin(p1)
            if p1_result:
                return 1
        else:
            p2.append(ar[i])
            p2_result=babyjin(p2)
            if p2_result:
                return 2
    return 0




T=int(input())


for tc in range(1,T+1):
    arr=list(map(int,input().split()))
    result=battle(arr)

    print('#{} {}'.format(tc,result))