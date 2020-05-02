def binary_float(num):
    ind=1
    result=''
    while num!=0:
        num=num*2
        if num>=1:
            result+='1'
            num-=1
        else:
            result+='0'
        ind+=1
        if ind==14:
            result='overflow'
            break
    return result
        




T=int(input())


for tc in range(1,T+1):
    a=float(input())
    result=binary_float(a)
    print('#{} {}'.format(tc,result))