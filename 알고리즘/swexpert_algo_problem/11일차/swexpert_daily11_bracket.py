T=int(input())

for tc in range(1,T+1):
    inp=input()
    stack=[]
    a=1

    for i in inp:              
        if i=='(' or i=='{':
            stack.append(i)
        elif i==')' or i=='}':
            if len(stack)>0:
                b=stack.pop()
                if i==')':
                    if b!= '(':
                        a=0
                        break
                else:
                    if b!='{':
                        a=0
                        break
            else:
                a=0
                break
    if len(stack)==0:
        print('#{} {}'.format(tc,a))
    else:
        print('#{} 0'.format(tc))
