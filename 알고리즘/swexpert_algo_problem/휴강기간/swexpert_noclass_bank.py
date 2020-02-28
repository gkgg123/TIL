T=int(input())
### 이 문제는 하나하나 다 바꿔서 비교를 해봤다.##
bit_list=[0,1]  ## 2진수에서 나올수 있는 수###
tit_list=[0,1,2]  ### 3진수에서 나올수 있는 수###

def calc(temp,k):  ### 2,3진수를 게산해주기 위한 함수이다. ####
    if k==0:
        res=0
        for t in range(len(temp)):
            res+=temp[t]*(2**two_squre[t])
        return res
    else:
        res=0
        for t in range(len(temp)):
            res+=temp[t]*(3**three_squre[t])
        return res



for tc in range(1,T+1):
    two_bit=list(map(int,list(input())))
    three_bit=list(map(int,list(input())))
    two_squre=list(range(len(two_bit)-1,-1,-1))
    three_squre=list(range(len(three_bit)-1,-1,-1))
    a_list=[]
    b_list=[]
   
    for i in range(len(two_bit)):
        for j in bit_list:
            temp_2bit=two_bit[:]
            if j!=temp_2bit[i]:
                temp_2bit[i]=j
                a_list.append(calc(temp_2bit,0))
    for i in range(len(three_bit)):
        for j in tit_list:
            temp_3bit=three_bit[:]
            if j!=temp_3bit[i]:
                temp_3bit[i]=j
                b_list.append(calc(temp_3bit,1))
    ans=0
    for i in a_list:
        for j in b_list:
            if i==j:
                ans=i

    print('#{} {}'.format(tc,ans))
                    

