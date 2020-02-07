a=[[0 for i in range(5)] for j in range(5)]

a[0][:]=[9,20,2,18,11]
a[1][:]=[19,1,25,3,21]
a[2][:]=[8,24,10,17,7]
a[3][:]=[15,4,16,5,6]
a[4][:]=[12,13,22,23,14]
total=[]
for i in a:
    for j in i:
        total.append(j)




