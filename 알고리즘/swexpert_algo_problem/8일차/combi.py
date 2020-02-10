a=[1,2,3,4]

num=len(a)

for i in range(1<<num):
    total=[]
    for j in range(num):        
        if i&(1<<j):
            total.append(a[j])
    
    print(total)