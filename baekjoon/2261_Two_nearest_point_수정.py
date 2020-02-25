from sys import stdin
import math
stdin=open('1.txt','r')
def calc_dis(x,y):
    mm=(x[0]-y[0])**2+(x[1]-y[1])**2
    return mm

def divide(start,end):
    length=end-start
    if length==2:
        return calc_dis(arr[start],arr[start+1])
    elif length==3:
        return min(calc_dis(arr[start],arr[start+1]),calc_dis(arr[start],arr[start+2]),calc_dis(arr[start+1],arr[start+2]))
    
    mid=(start+end)//2
    first=divide(start,mid)
    second=divide(mid,end)

    min_distance=min(first,second)
    
    mid_x_value=arr[mid][0]
    temp=[]
    for i in range(start,end):
        if (mid_x_value-arr[i][0])**2<=min_distance:
            temp.append(arr[i])
    temp.sort(key=lambda x: x[1])
    result=min_distance
    temp_len=len(temp)
    d=math.sqrt(min_distance)
    if temp_len>=2:
        for i in range(temp_len-1):
            for j in range(i+1,temp_len):
                if temp[j][1]-temp[i][1]>d:
                    break
                if temp[i][0]>mid_x_value and temp[j][0]>mid_x_value:
                    continue
                elif temp[i][0]<mid_x_value and temp[j][0]<mid_x_value:
                    continue
                result=min(result,calc_dis(temp[i],temp[j]))
            if result==1:
                return result
    return result



N=int(stdin.readline())

arr=[list(map(int,stdin.readline().split())) for _ in range(N)]
arr.sort()
set_arr=set(map(tuple,arr))
### 수정판 ###
if len(set_arr)!=len(arr):
    print(0)
else:
    min_die=divide(0,N)
    print(min_die)