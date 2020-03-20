
def solve_RCS(ix,co):
    result=[]

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
                    result.append((R,C,S))
    return result


                


T=int(input())
list_index=['(',')','{','}','[',']']
for tc in range(1,T+1):
    N,M=map(int,input().split())
    arr1=[input() for _ in range(N)]
    arr2=[input() for _ in range(M)]
    arr_index=[[0]*3 for _ in range(N)]
    arr_come=[0]*N
    rcs_count=[0,0,0]
    for i in range(N):
        for k in arr1[i]:
            if k in list_index:
                temp=list_index.index(k)
                inx=temp//2       
                sub=temp%2         
                if sub:      
                    rcs_count[inx]-=1
                else:
                    rcs_count[inx]+=1
        arr_index[i]=rcs_count[:]
    for i in range(N):
        cnt=0
        while arr1[i][cnt]=='.':
            cnt+=1
        arr_come[i]=cnt
    

    total=solve_RCS(arr_index,arr_come)
   

    result=[-987654321]*M
    result[0]=0
    arr2_index=[[0]*3 for _ in range(M)]
    rcs_count2=[0,0,0]
    ################# 위와 똑같은 방식으로 내가 들여쓰기를 해야할것에도, 똑같이 괄호의 숫자를 세주었다. ####
    for i in range(M):
        for k in arr2[i]:
            if k in list_index:
                temp=list_index.index(k)
                inx=temp//2
                sub=temp%2
                if sub:
                    rcs_count2[inx]-=1
                else:
                    rcs_count2[inx]+=1 
            arr2_index[i]=rcs_count2[:]

    for r,c,s in total:
        for ind in range(M-1):
            temp=arr2_index[ind][0]*r+arr2_index[ind][1]*c+arr2_index[ind][2]*s
            if result[ind+1]==-987654321:
                result[ind+1]=temp
            elif result[ind+1]!=temp:
                result[ind+1]=-1

    
    print('#{} '.format(tc),end='')
    print(*result)




