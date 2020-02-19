T=int(input())

for tc in range(1,T+1):
    calc=list(input().split())
    stack=[]
    total=0
    for i in calc:
        if i.isdigit():
            stack.append(int(i))
        else:
            if i=='.' and len(stack)==1:
                total=stack.pop()
                break
            elif i=='.' and len(stack)!=1:
                total='error'
                break
            elif len(stack)<2:
                total='error'
                break
            else:
                a=stack.pop()
                b=stack.pop()
                if i=='/':
                    stack.append(b//a)
                elif i=='*':
                    stack.append(b*a)
                elif i=='+':
                    stack.append(b+a)
                elif i=='-':
                    stack.append(b-a)
    print('#{} {}'.format(tc,total))
