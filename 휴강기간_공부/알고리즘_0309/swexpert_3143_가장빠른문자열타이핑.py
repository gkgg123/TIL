T=int(input())

for tc in range(1,T+1):
    A,B=list(input().split(' '))
    len_a=len(A)
    len_b=len(B)
    st=0
    cnt=0
    while st<=len_a-len_b:
      
        if A[st:st+len_b]==B:
            st+=len_b
            cnt+=1
        else:
            st+=1
    result=len_a-(len_b-1)*cnt
    print('#{} {}'.format(tc,result))
