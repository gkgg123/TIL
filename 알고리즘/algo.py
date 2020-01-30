number=list(map(int,input().split()))
if number[0]==number[1] and number[0]==number[2]:
    print('triplet')

for i1 in number:
    for i2 in number:
        if i2 != i1:
            for i3 in number:
                if i3 != i1 and i3 != i2:
                    if i1+1==i2 and i2+1==i3:
                        print('run')