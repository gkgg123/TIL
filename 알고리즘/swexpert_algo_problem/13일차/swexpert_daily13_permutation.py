def permu(mat,start,end):
    if start==end:
        print(mat)
    else:
        for i in range(start,end):
            arr[start],arr[i]=arr[i],arr[start]
            permu(arr,start+1,end)
            arr[start],arr[i]=arr[i],arr[start]


arr=list(range(1,5))

permu(arr,0,4)




# def backtrack(a,k,input):
#     global MAXCANDIDATES
#     c=[0]*MAXCANDIDATES
#     if k==input:
#         for i in range(1,k+1):
#             print(a[i],end=' ')
#         print()
#     else:
#         k+=1
#         ncandidates = construct_candidates(a,k,input,c)
#         for i in range(ncandidates):
#             a[k]=c[i]
#             backtrack(a,k,input)

# def construct_candidates(a,k,input,c):
#     in_perm=[False]*NMAX
#     for i in range(1,k):
#         in_perm[a[i]]=True
#     ncandidates=0
#     for i in range(1,input+1):
#         if in_perm[i]==False:
#             c[ncandidates]=i
#             ncandidates+=1
#     return ncandidates


# MAXCANDIDATES=100
# NMAX=100
# a=[0]*NMAX
# backtrack(a,0,3)



# import itertools

# a=list(range(1,5))


# for tt in range(1,5):
#     b=itertools.permutations(a,tt)
#     for i in b:
#         print(i)
#         sum=0
#         for k in i:
#             sum+=k
#         if sum==10:
#             print(i)
