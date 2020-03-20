# import sys
# sys.stdin=open('3378.txt','r')
# ### 복잡하게 푼 방식 ####

def solve_RCS(ix,co):
    result=[[] for _ in range(3)]

    #### R,C,S의 값을 찾아내주는 방식이다.
    for R in range(1,21):
        for C in range(1,21):
            for S in range(1,21):
                cnt=0
                for i in range(1,N):
                    temp=R*(ix[i-1][0])+C*(ix[i-1][1])+S*(ix[i-1][2])
                    if temp==co[i]:
                        cnt+=1
                if cnt==N-1: ### 해당 r,c,s가 모든 경우에 맞으면 값을 추가해준다.
                    if R not in result[0]:
                        result[0].append(R)
                    if C not in result[1]:
                        result[1].append(C)
                    if S not in result[2]:
                        result[2].append(S)
    for i in range(3):
        if len(result[i])!=1:  ## 근데 중복된게 있으면, 길이가 1 이상이므로 그때는 -1로 해준다.
            result[i]=-1
        else:
            result[i]=result[i][0]

    return result


                


T=int(input())
list_index=['(',')','{','}','[',']']
for tc in range(1,T+1):
    N,M=map(int,input().split())
    arr1=[input() for _ in range(N)]
    arr2=[input() for _ in range(M)]
    arr_index=[[0]*3 for _ in range(N)]
    arr_come=[0]*N
    for i in range(N):
        flag=False
        for ind,k in enumerate(arr1[i]):
            if k in list_index:
                temp=list_index.index(k)
                inx=temp//2        #### () 이면 inx=0 {} 이면 inx=1 []이면 inx=2로 매칭해준다.
                sub=temp%2         #### 만약 sub=1이면 닫힌 괄호이므로, arr_index에서 -1 해주고,
                if sub:            #### sub=0이면 열린괄호이므로 arr_index에서 +1 해준다.
                    arr_index[i][inx]-=1
                else:
                    arr_index[i][inx]+=1
                flag=False
            elif k=='.' and ind==0:  ### 가장 처음에 온점(.)이면 flag를 True로 해준다.
                arr_come[i]+=1
                flag=True
            elif k=='.' and flag:    ### 그리고 그 다음것도 온점(.) 이면 arr_come을 추가해준다.
                arr_come[i]+=1
            else:
                flag=False          ### 만약 온점(.)이 아니면 flag를 False로 해서 더는 안더해준다.
    
    for i in range(N-1):
        for k in range(3):
            arr_index[i+1][k]+=arr_index[i][k]
    ### arr_index는 현재 위치의 (),{},[]의 개수를 누적해주기 위해서, 위와 같은 방식으로 해주었다.
    total=solve_RCS(arr_index,arr_come)

    result=[0]*M
    arr2_index=[[0]*3 for _ in range(M)]
    ################# 위와 똑같은 방식으로 내가 들여쓰기를 해야할것에도, 똑같이 괄호의 숫자를 세주었다. ####
    for i in range(M):
        for k in arr2[i]:
            if k in list_index:
                temp=list_index.index(k)
                inx=temp//2
                sub=temp%2
                if sub:
                    arr2_index[i][inx]-=1
                else:
                    arr2_index[i][inx]+=1 
    for i in range(M-1):
        for k in range(3):
            arr2_index[i+1][k]+=arr2_index[i][k]
    #################################################################################################



    for i in range(M-1):
        temp1=arr2_index[i][0]*total[0]
        temp2=arr2_index[i][1]*total[1]
        temp3=arr2_index[i][2]*total[2]
        if temp1>=0 and temp2>=0 and temp3>=0:   ### 3개의 R,C,S를 곱한 값이 전부 0 이상이면, 중복된거와 상관없으므로,
            result[i+1]=temp1+temp2+temp3       ### 바로 대입을 해준다.
        else:
            ### 기존의 R,C,S로 못푸는거면, 위의 arr1에서 똑같은 값이 나왔을때를 판별해주면,
            ### 똑같이 들여쓰기를 해줄수 있다. 
            ### 그걸 판별해주는 과정이지만,
            ### 좀 더 많은 테스트 케이스가 있으면 실패할 가능성이 큰 방법이다.
            ### 만약 [1,1,0] 일때 들여쓰기가 2라면
            ### [2,2,0]도 들여쓰기가 4로 하면 되는데, 지금과 같은 방식으로는 판별해줄수없다.
            cnt_temp=0
            cnt_Flag=True
            temp_result=[]
            for ind1,k in enumerate(arr_index):   
                if k[0]==arr2_index[i][0] and k[1]==arr2_index[i][1] and k[2]==arr2_index[i][2]:
                    #### 만약 arr1에서 똑같은 들여쓰기를 가지는 arr_index가 있으면
                    #### temp_result에 값을 추가해준다. 
                    cnt_temp+=1
                    temp_result.append(arr_come[ind1+1])
            if cnt_temp==1:
                ### 만약 똑같은 경우가 1번밖에 없다면 바로 집어넣어준다.
                result[i+1]=temp_result[0]
            elif cnt_temp>1:
                ### 만약 2개 이상일때 ####
                ### temp_result에 저장된 값이 상이하면, -1을 집어넣어준다.
                for sol in range(len(temp_result)-1):
                    if temp_result[sol]!=temp_result[sol+1]:
                        cnt_Flag=False
                if cnt_Flag:
                    result[i+1]=temp_result[0]
                else:
                    result[i+1]=-1
            else:
                ### 1번도 없으면 바로 -1을 넣어준다.
                result[i+1]=-1

    print('#{} '.format(tc),end='')
    print(*result)




