from sys import stdin
stdin=open('1.txt','r')
N=int(stdin.readline())

arr=[list(map(int,stdin.readline().split())) for _ in range(N)]

arr.sort(key=lambda x : x[0])
min_distance=10**12
for ind,i in enumerate(arr):
    for j in arr[ind+1:]:
        if (i[0]-j[0])**2>min_distance:
            break
        elif (i[1]-j[1])**2>min_distance:
            continue
        else:
            dis_temp=(i[0]-j[0])**2+(i[1]-j[1])**2
            if dis_temp<min_distance:
                min_distance=dis_temp

print(min_distance)