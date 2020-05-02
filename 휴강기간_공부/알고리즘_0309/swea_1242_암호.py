import sys
sys.stdin=open('1242.txt','r')

num16_2={
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'A':'1010',
    'B':'1011',
    'C':'1100',
    'D':'1101',
    'E':'1110',
    'F':'1111',
}
password={

    '3211':0,
    '2221':1,
    '2122':2,
    '1411':3,
    '1132':4,
    '1231':5,
    '1114':6,
    '1312':7,
    '1213':8,
    '3112':9,
}

def b2_10(a,b,c):        #### 비율로 password를 알아내서 바꿔주는거,
    min_num=min(a,b,c)  ### 최소값으로 나누면, 각 비율이 된다. 그걸이용해서, 비밀먼호를 알아낸다.
    a//=min_num
    b//=min_num
    c//=min_num
    k=7-a-b-c
    return password[str(k)+str(c)+str(b)+str(a)]

def verify(total):  ### 제대로 된 암호코드인지 판별해주는거
    
    final_result=0
    for i in range(8):
        if i==7:
            final_result+=total[i]
        elif i%2==0:
            final_result+=3*total[i]
        else:
            final_result+=total[i]
    if final_result%10==0:
        return sum(total)
    else:
        return 0

        

                    








T=int(input())



for tc in range(1,T+1):
    N,M=map(int,input().split())
    password_set=set()
    for i in range(N):
        temp=input().strip()  ### 공백제거 밑
        if temp.count('0')!=M:  ### 전체가 0 인것은 password_set에 추가하지말고, 아닌것들은 추가해줘라
            password_set.add(temp)

    password_binary=[]
    for i in password_set:  ### 위에서 구한 password_set을 16진수에서 2진수로 바꿔준다.
        temp=''
        for num in i:
            temp+=num16_2[num]
        password_binary.append(temp)
    

    total=0
    visited=[]   ### 한번 들렸던 암호는 다시 안하기 위해서 만들어놓은 것.
    result=[]    ### 여기에는 암호를 10진수의 8글자로 바꿀것이다.
    for num in password_binary:
        ind=len(num)  #### num의 길이가 각각 다를수도 있으므로, len(num)으로 구해줬다.
        a=b=c=0       #### a,b,c는 비율을 세기 위해서 만들어놓은거.
        for x in range(ind-1,-1,-1):
            if b==0 and c==0 and num[x]=='1':  ### 우리가 만든 암호는 뒤에부터 보면 무조건 1로 끝난다. 그래서, b,c,가 0일때,
                a+=1                           ### 뒤에서 1을 만나면 a를 올려준다.
            elif a>0 and c==0 and num[x]=='0': ### a의 값이 올라간다가 0으로 값이 바뀌면, b의 값으로 해준다
                b+=1
            elif a>0 and b>0 and num[x]=='1':  ### b,a가 0보다 큰데, num의 값이 1로 바뀌면 c를 올려준다.
                c+=1

            if a>0 and b>0 and c>0 and num[x]=='0':  ### 그렇게 탐색을 하다가, a,b,c가 다 0보다 큰상태에서 0을만난것은 암호가 끝난것이기 때문에,
                result.append(b2_10(a,b,c))         ### 암호로 판별을 해준다.
                                                    ### [k,c,b,a] 으로 비를 나타낸것으로, 이것은 password 라는 디렉토리에 저장해줬다.
                a=b=c=0                             ### c,b,a를 최소값으로 나눠주면 비율로 나타난다. 이 문제의 비율은 다 더하면
                                                    ### 무조건 7인걸 이용해 k를 구하고, 'kcba'형태로 만들어서 password를 불러오자.
                                                    ### 그리고 a,b,c를 초기화 시켜준다.
            

            if len(result)==8:                   ### 그렇게 하다가 result가 길이가 8이되면, 인제 판별을 해줘야한다.
                result=result[::-1]             ### 우리는 뒤에서부터 탐색하다보니, 순서가 반대가 됬을것이기 때문에, 순서를 바꿔준다.
                if result not in visited:       ### 우리가 한번도 방문하지않은 암호에 대해서만 더해준다.
                    total+=verify(result)       ### verify라는 함수를 통해, 암호가 맞는기 확인하고 더해준다.
                visited.append(result)          ### 그리고 우리가 방문한 result를 visted에 추가해서 중복해서 들리지않게 해준다.
                result=[]                       ### 그리고 result를 초기화 시켜준다.
    print('#{} {}'.format(tc,total))