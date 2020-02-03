
for test_case in range(1,11):
    dump=int(input())
    box=list(map(int,input().split()))

    while dump>0:
        box=sorted(box)
        box[-1]-=1
        box[0]+=1
        dump-=1
    print('#{} {}'.format(test_case,max(box)-min(box)))