def bubbleSort(T):
    for i in range(len(T)-1,0,-1):
        for j in range(i):
            if T[j]>T[j+1]:
                T[j],T[j+1]=T[j+1],T[j]
    return T


a=[55, 7, 78,12,42]
print(bubbleSort(a))
