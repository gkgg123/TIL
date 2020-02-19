import sys
sys.stdin=open('tournament.txt','r')


T=int(input())
def gababo(x,y):
    if x==y:
        return 1
    else:
        if x==1 and y==2:
            return 2
        elif x==1 and y==3:
            return 1
        elif x==2 and y==3:
            return 2
        elif x==2 and y==1:
            return 1
        elif x==3 and y==1:
            return 2
        else:
            return 1


for tc in range(1,T+1):
    N=int(input())
    arr=list(map(int,input().split()))

    arr_index=list(range(1,N+1))
   
    while len(arr)>2:
        temp=[]
        temp_index=[]
        if len(arr)%2==1:
            if ((len(arr)+1)//2)%2==0:

                for i in range(0,(len(arr)+1)//2,2):
                    k= gababo(arr[i],arr[i+1])
                    if k==1:
                        temp.append(arr[i])
                        temp_index.append(arr_index[i])
                    else:
                        temp.append(arr[i+1])
                        temp_index.append(arr_index[i+1])

                for j in range((len(arr)+1)//2,len(arr)-1,2):
                    k=gababo(arr[j],arr[j+1])
                    if k==1:
                        temp.append(arr[j])
                        temp_index.append(arr_index[j])
                    else:
                        temp.append(arr[j])
                        temp_index.append(arr_index[j])
                temp.append(arr[-1])
                temp_index.append(arr_index[-1])
            else:

                for i in range(0,(len(arr)+1)//2-1,2):
                    k= gababo(arr[i],arr[i+1])
                    if k==1:
                        temp.append(arr[i])
                        temp_index.append(arr_index[i])
                    else:
                        temp.append(arr[i+1])
                        temp_index.append(arr_index[i+1])
                temp.append(arr[(len(arr)+1)//2-1])
                temp_index.append(arr_index[(len(arr)+1)//2-1])

                for j in range((len(arr)+1)//2,len(arr),2):
                    k=gababo(arr[j],arr[j+1])
                    if k==1:
                        temp.append(arr[j])
                        temp_index.append(arr_index[j])
                    else:
                        temp.append(arr[j])
                        temp_index.append(arr_index[j])
        else:
            if (len(arr)//2)%2==1:
                for i in range(0,len(arr)//2-1,2):
                    k=gababo(arr[i],arr[i+1])
                    if k==1:
                        temp.append(arr[i])
                        temp_index.append(arr_index[i])
                    else:
                        temp.append(arr[i+1])
                        temp_index.append(arr_index[i+1])
                temp.append(arr[len(arr)//2-1])
                temp_index.append(arr_index[len(arr)//2-1])
                for j in range(len(arr)//2,len(arr)-1,2):
                    k=gababo(arr[j],arr[j+1])
                    if k==1:
                        temp.append(arr[j])
                        temp_index.append(arr_index[j])
                    else:
                        temp.append(arr[j+1])
                        temp_index.append(arr_index[j+1])
                temp.append(arr[-1])
                temp_index.append(arr_index[-1])
            else:
                for i in range(0,len(arr)//2,2):
                    k=gababo(arr[i],arr[i+1])
                    if k==1:
                        temp.append(arr[i])
                        temp_index.append(arr_index[i])
                    else:
                        temp.append(arr[i+1])
                        temp_index.append(arr_index[i+1])
                for j in range(len(arr)//2,len(arr),2):
                    k=gababo(arr[j],arr[j+1])
                    if k==1:
                        temp.append(arr[j])
                        temp_index.append(arr_index[j])
                    else:
                        temp.append(arr[j+1])
                        temp_index.append(arr_index[j+1])
        arr=temp[:]
        arr_index=temp_index[:]
    print('#{} '.format(tc),end='')
    if len(arr)==2:
        k=gababo(arr[0],arr[1])
        if k==1:
            print(arr_index[0])
        else:
            print(arr_index[1])
    else:
        print(arr_index[0])

                    