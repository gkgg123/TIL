from itertools import combinations

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    sub_N=N//2
    arr=[list(map(int,input().split())) for _ in range(N)]
    row=[sum(i) for i in arr]
    col=[sum(i) for i in zip(*arr)]

    new_arr=[i+j for i,j in zip(row,col)]

    allstat=sum(new_arr)//2
    new_arr.sort()
    new_arr[1::2]=new_arr[-1::-2]
    allstat -= new_arr[-1]
    mins=99999999

    for l in combinations(new_arr[:-1],sub_N-1):
        mins=min(mins,abs(allstat-sum(l)))

        if not mins:
            break
    print('#{} {}'.format(tc,mins))