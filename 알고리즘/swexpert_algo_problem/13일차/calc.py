icp={
    '*':2,
    '/':2,
    '+':1,
    '-':1,
    '(':3,
}
isp={
    '*':2,
    '/':2,
    '+':1,
    '-':1,
    '(':0
}

A='( 6 + 5 * ( 2 - 8 ) / 2 )'
k= list(A.split())
st=[]
calc=[]
for i in k:
    if i.isdecimal():
        calc.append(i)
    else:
        if len(st)==0:
            if i=='*' or i=='/' or i=='+' or i=='-' or i=='(':
                st.append(i)
        elif i==')':
            for tt in st[::-1]:
                if tt=='(':
                    st.pop()
                    break
                else:
                    calc.append(st.pop())
        else:
            if i=='*' or i=='/' or i=='+' or i=='-' or i=='(':
                for tt in st[::-1]:
                    if isp[tt]<icp[i]:
                        st.append(i)
                        break
                    else:
                        calc.append(st.pop())
            

for ttt in st[::-1]:
    calc.append(ttt)
print(calc)
calc.append('.')
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
print('{}'.format(total))

