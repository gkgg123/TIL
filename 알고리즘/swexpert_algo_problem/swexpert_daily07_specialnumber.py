T=int(input())
def search(x,y,cnt):
    global num1
    nx=x-1
    ny=y+1 
    if nx==0:
        search(ny+1,0,cnt)
    elif cnt+1==num1:
        num1_sp.append(nx)
        num1_sp.append(ny)
        return 0
    else:
        search(nx,ny,cnt+1)
def search2(x,y,cnt):
    global num2
    nx=x-1
    ny=y+1 
    if nx==0:
        search2(ny+1,0,cnt)
    elif cnt+1==num2:
        num2_sp.append(nx)
        num2_sp.append(ny)
        return 0
    else:
        search2(nx,ny,cnt+1)
    
def search3(x,y):
    nx=x+1
    ny=y-1
    if nx==ny:
        re=1
        for i in range(nx):
            re+=4*i
        result_cnt[0]+=re
        return 0
    elif ny==0:
        search3(0,nx-1)
    else:
        result_cnt[0]+=1
        search3(nx,ny)

    



for tc in range(1,T+1):
    num1,num2=map(int,input().split())
    total=1
    num1_sp=[]
    num2_sp=[]
    for i in range(72):
        total+=4*i
        if num1<total:            
            search(i,i,total-4*i)
            break
        if num1==total:
            num1_sp.append(i+1)
            num1_sp.append(i+1)
            break
    total=1
    for i in range(72):
        total+=4*i
        if num2<total:            
            search2(i,i,total-4*i)
            break
        if num2==total:
            num2_sp.append(i+1)
            num2_sp.append(i+1)
            break
    result_cnt=[1]

    result=[num1_sp[0]+num2_sp[0],num1_sp[1]+num2_sp[1]]
    # print(result)
    search3(result[0],result[1])
    print('#{} {}'.format(tc,result_cnt[0]))


        