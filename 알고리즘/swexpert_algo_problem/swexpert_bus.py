T=int(input())
for test_case in range(1,T+1):
    k,n,m=map(int,input().split(' '))
    rail=range(n+1)
    char=list(map(int,input().split(' ')))
    char_map=[0]*(n+1)
    person=0
    stop=0
    cnt=0
    for ind in char:
        char_map[ind]=1
    for st in range(len(char)-1):
        if char[st]+k<char[st+1]:
            stop=99999
    if stop==0:
        while True:
            if sum(char_map[person:person+k+1]):
                temp=0
                for indd,value in enumerate(char_map[:person+k+1]):
                    if value==1:
                        person=indd
                cnt=cnt+1
                if person+k>=n:
                    break
    if stop>0:
        print('#{} 0'.format(test_case))
    else:
        print('#{} {}'.format(test_case,cnt))