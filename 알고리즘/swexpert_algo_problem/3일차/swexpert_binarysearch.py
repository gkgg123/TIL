T=int(input())

for i in range(1,T+1):
    T_p,P_a,P_b=map(int,input().split())
    cnt_a=0
    cnt_b=0
    a_l=1
    b_l=1
    a_r=T_p
    b_r=T_p

    while True:
        c_a=(a_l+a_r)//2
        cnt_a+=1
        if P_a==c_a:
            break
        if P_a>c_a:
            a_l=c_a
        if P_a<c_a:
            a_r=c_a
    while True:
        c_b=(b_l+b_r)//2
        cnt_b+=1
        if P_b==c_b:
            break
        if P_b>c_b:
            b_l=c_b
        if P_b<c_b:
            b_r=c_b
    if cnt_a<cnt_b:
        print('#{} A'.format(i))
    elif cnt_a>cnt_b:
        print('#{} B'.format(i))
    else:
        print('#{} 0'.format(i))


