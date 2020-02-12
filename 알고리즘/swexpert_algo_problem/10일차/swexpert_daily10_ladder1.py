def go(x):
    result = 0
    y = 0
    while True:
        if y==99 and arr[99][x]==2:
            return 1
        elif y==99:
            return result
        for t in [1,-1]:
            if arr[y][x+t]:
                while arr[y][x+t]:
                    x += t
                    result += 1
                break
        y += 1
        result += 1
for T in range(1,11):
    input()
    arr = [[0]+list(map(int,input().split()))+[0] for i in range(100)]
    ans = min([[go(i),i-1] for i in range(1,102) if arr[0][i]==1])
    print('#{} {}'.format(T,ans))