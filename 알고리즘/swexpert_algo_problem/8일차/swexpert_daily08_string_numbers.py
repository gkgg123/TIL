T=int(input())

for tc in range(1,T+1):
    str1=set(input())
    str2=input()

    max_numbers=0

    for i in str1:
        if max_numbers<str2.count(i):
            max_numbers=str2.count(i)
    print('#{} {}'.format(tc,max_numbers))