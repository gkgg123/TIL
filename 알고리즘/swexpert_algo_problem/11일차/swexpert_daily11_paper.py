# T=int(input())

# for tc in range(1,T+1):
#     N=int(input())
#     paper=[0,1,3]
#     cnt1=1
#     cnt2=1
#     for i in range(3,N//10+1):
#         if i%2==1:
#             paper.append(paper[i-2]+4**(cnt1))
#             cnt1+=1
#         else:
#             paper.append(paper[i-2]+2*4**(cnt2))
#             cnt2+=1
#     print('#{} {}'.format(tc,paper))



def getsome(x):
    if x==N:
        return 1
    elif x>N:
        return 0
    return getsome(x+10)+getsome(x+20)*2


for N in range(0,210,10):
    print(N,getsome(0))