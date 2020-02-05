T=int(input())

for tc in range(1,T+1):
    card=input()
    card_split=[]
    s_num=13
    d_num=13
    h_num=13
    c_num=13
    for i in range(len(card)//3):
        card_split.append(card[3*i:3*(i+1)])
    
    result=[]
    fail=0

    for val in card_split:
        if val not in result:
            if val[0]=='S':
                s_num-=1
                result.append(val)
            elif val[0]=='D':
                d_num-=1
                result.append(val)
            elif val[0]=='H':
                h_num-=1
                result.append(val)
            elif val[0]=='C':
                c_num-=1
                result.append(val)
        else:
            fail=1
    if fail==0:
        print('#{} {} {} {} {}'.format(tc,s_num,d_num,h_num,c_num))
    else:
        print('#{} ERROR'.format(tc))



            


