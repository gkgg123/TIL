T=int(input())

for tc in range(1,T+1):
    arr=list(input())
    st=0
    cnt=0
    pipe=0
    while True:
        if st==len(arr):
            break
        if arr[st]=="(":
            if arr[st+1]==")":
                cnt+=pipe
                st+=2
            else:
                pipe+=1
                st+=1
        else:
            pipe-=1
            cnt+=1
            st+=1
    print(cnt)
