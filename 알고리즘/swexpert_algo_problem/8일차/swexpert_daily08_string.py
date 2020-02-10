# T=int(input())


# for tc in range(1,T+1):
#     str1=input()
#     str2=input()

#     le_str1=len(str1)
#     le_str2=len(str2)
#     res=0

#     for i in range(le_str2-le_str1+1):
#         if str2[i:i+le_str1]==str1:
#             res=1
#             break
#     print('#{} {}'.format(tc,res))

T=int(input())

for tc in range(1,T+1):
    str1=input()
    str2=input()

    le_str1=len(str1)
    le_str2=len(str2)
    str_list=[]
    res=0

    for i in range(le_str2-le_str1+1):
        if str2[i]==str1[0]:
            str_list.append(i)
    k=0
    
    while k<len(str_list):
        ind=str_list[k]
        if str2[ind:ind+le_str1]==str1:
            res=1
        k+=1

    print('#{} {}'.format(tc,res))
        
