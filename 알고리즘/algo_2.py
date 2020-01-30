arr=[int(x) for x in input()]

cnt=[0]*10
for i in arr:
    cnt[i]=arr.count(i)
6
total=0
i=0

while i<len(cnt):

    if cnt[i]>=3:
        print('triplet')
        cnt[i]-=3
        total+=1
        continue
    if i<8:
        if cnt[i]>=1 and cnt[i+1]>=1 and cnt[i+2]>=1:
            print('run')
            cnt[i]-=1
            cnt[i+1]-=1
            cnt[i+2]-=1
            total+=1
            continue
    i+=1
# for i in range(10):
#     if cnt[i]>=3:
#         print('triplet')
#         cnt[i]-=3
#         total+=1
#         if cnt[i]>=3:
#             print('triplet')
#             cnt[i]-=3
#             total+=1
#     if i>=8:
#         continue7
#     if cnt[i]>=1 and cnt[i+1]>=1 and cnt[i+2]>=1:
#         print('run')
#         cnt[i]-=1
#         cnt[i+1]-=1
#         cnt[i+2]-=1
#         total+=1
#     if cnt[i]>=1 and cnt[i+1]>=1 and cnt[i+2]>=1:
#         print('run')
#         cnt[i]-=1
#         cnt[i+1]-=1
#         cnt[i+2]-=1
#         total+=1
if total==2:
    print('babyjin')
else:
    print('babyjin이 아닙니다')
