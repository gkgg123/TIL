

li={

    '2':'ABC',
    '3':'DEF',
    '4':'GHI',
    '5':'JKL',
    '6':'MNO',
    '7':'PQRS',
    '8':'TUV',
    '9':'WXYZ'
}
T=input()
total=0
for i in T:
    for j,k in li.items():
        if i in k:
            total+=int(j)+1
print(total)