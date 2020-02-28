import sys
sys.stdin=open('text2.txt','r')

def cal(n,money,f_d,f_m,f_m3):
    global min_value
    if n>12:
        if min_value>money:
            min_value=money
    elif min_value<=money:
        return
    else:
        cal(n+1,money+min(month[n]*f_d,f_m),f_d,f_m,f_m3)
        cal(n+3,money+f_m3,f_d,f_m,f_m3)


T=int(input())

for tc in range(1,T+1):
    d,m,m3,y=list(map(int,input().split()))
    month=[0]
    month.extend(list(map(int,input().split())))
    min_value=y
    cal(1,0,d,m,m3)
    print('#{} {}'.format(tc,min_value))

