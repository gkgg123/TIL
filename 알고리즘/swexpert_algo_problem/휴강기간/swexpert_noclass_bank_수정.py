T=int(input())
### 이 문제는 하나하나 다 바꿔서 비교를 해봤다.##
bit_list=[0,1]  ## 2진수에서 나올수 있는 수###
tit_list=[0,1,2]  ### 3진수에서 나올수 있는 수###

def calc(temp,k):  ### 2,3진법을 10진법으로 계산해주기 위한 함수이다. ####
    res=0          ### k는 몇진법인지 나타낸것이다.###
    for t in range(len(temp)):
        res+=temp[t]*(k**(len(temp)-t-1))
    return res



for tc in range(1,T+1):
    two_bit=list(map(int,list(input())))
    three_bit=list(map(int,list(input())))
    a_list=[]
    b_list=[]
   
    for i in range(len(two_bit)): ## 각 자리마다 돌아가면서 
        for j in bit_list:       ### bit_list을 전부 돌리면서
            temp_2bit=two_bit[:]
            if j!=temp_2bit[i]:     ### 현재위치의 값과 bit_list의 값이 다를경우를 전부 계산을 해주었다.
                temp_2bit[i]=j      ### 다른값을 대입해주고,
                a_list.append(calc(temp_2bit,2))   ### 그 값을 10진법으로 변환해서 list에 저장해 두었다.
   
    for i in range(len(three_bit)):
        for j in tit_list:
            temp_3bit=three_bit[:]
            if j!=temp_3bit[i]:
                temp_3bit[i]=j
                b_list.append(calc(temp_3bit,3))
    ans=0
    for i in a_list:   ### 저장된 리스트들이 같은 값을 가지는 것을 찾아서, ans에 저장해 주었다.
        for j in b_list: 
            if i==j:
                ans=i

    print('#{} {}'.format(tc,ans))
                    

