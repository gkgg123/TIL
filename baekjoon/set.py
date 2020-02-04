arr=[3,6,7,1,5,4]

n=len(arr)


for i in range(1<<n):
    result=[]
    for j in range(n+1):
        if i &(1<<j):
            result.append(arr[j])
    print(result)