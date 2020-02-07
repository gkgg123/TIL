T=int(input())

for tc in range(1,T+1):
    li=[input() for i in range(5)]
    max_li=0
    for i in li:
        if max_li<len(i):
            max_li=len(i)
    for ind,j in enumerate(li):
        if max_li>len(j):
            for pl in range(max_li-len(j)):
                li[ind]+=' '
    result=''
    for i in range(max_li):
        for j in li:
            result+=j[i]
    result=result.replace(" ","")
    print('#{} {}'.format(tc,result))
