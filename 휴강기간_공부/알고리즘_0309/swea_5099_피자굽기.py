import sys
sys.stdin=open('5099.txt','r')

T=int(input())

for tc in range(1,T+1):
    N,M=map(int,input().split())
    pizza=list(map(int,input().split()))
    arr=pizza[:N]   ### 처음에 N개의 피자만 화덕에 들어갈수 있으므로, N개만 넣어줬다.
    arr_index=list(range(N))   ### 들어간 피자의 index를 저장해주기 위함.
    ind=N   ### 다음 피자를 넣어주기 위한 index이다. N개의 피자가 먼저 들어가므로, 다음 피자는 index로 따지면 N이기 때문이다.
    result=0
    while True:
        for i in range(N):
            temp_c=arr[i]//2   #### 치즈가 줄어드는 양이다.
            if temp_c==0:     #### 만약에 치즈가 0이 되었으면 교체를 해줘야하는데,
                if ind<M:     #### 피자가 남아있으면 
                    arr[i]=pizza[ind]     #### 치즈가 0이된 위치에 pizza 다음것을 넣어준다.
                    result=arr_index[i]+1   #### 그리고 그때 0이된 피자의 index를 result에 넣어준다. index와 몇번째는 1개 차이가 나므로 +1을 해준거다.
                    arr_index[i]=ind      #### 그리고 arr_index도 새로 들어간 pizza의 index를 넣어준다.
                    ind+=1                #### 그리고 index를 +1 해준다.
                else:
                    arr[i]=0       ### 만약 M개의 피자를 다 넣었으면 arr[i]에는 아무것도 안 들어가므로 0을 넣어준다.
                    if arr_index[i]!=-1:    ### 그리고 밑에 보면 초과된 피자에는 index를 -1을 넣어줬다. 그래서 arr_index=-1인 값은
                        result=arr_index[i]+1   ### 실제 피자가 아니므로, arr_index가 -1이 아닌경우에만 들어와서 result 값을 갱신해준다.
                    arr_index[i]=-1    
            else:
                arr[i]=temp_c    #### 치즈가 다 안녹았다면 그대로 temp_c를 넣어준다.
        if sum(arr)==0:   #### 그리고 모든피자가 다 녹았다면 다 더하면 0이므로 그때 멈춰준다.
            break
    print('#{} {}'.format(tc,result))
    