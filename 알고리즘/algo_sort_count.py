data=[0,4,1,3,1,2,4,1]

T=max(data)
counts=[0]*(T+1)
temp=[0]*(len(data))
for i in data:
    counts[i]=data.count(i)
for j in range(1,T+1):
    counts[j]+=counts[j-1]
for num in data[::-1]:
    temp[counts[num]-1]=num
    counts[num]-=1

print(temp)