T=int(input())


for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]

    
    visited=[0]*201

    ### 방을 200개 만들어주는데 0번방은 그냥 숫자를 맞춰주기 위해서 만들어줬다.
    for lower,upper in arr: 
        if lower>upper:   ### 번호가 낮은 방에서 큰방으로 가고 싶은데, 숫자가 역으로 들어올수 있으니 확인해준다.
            lower,upper=upper,lower
        if lower%2:       ### 3,4->2번방 5,6->3번방 7,8->4번방 식으로 바꿔주고 싶어서 홀수일때는 +1을 해주고,
            lower+=1      ### 2를 나눈 몫을 구해서 start와 end을 구해주었고
        if upper%2:   
            upper+=1
        start=lower//2
        end=upper//2
        for k in range(start,end+1):       ### 그 방을 지나갈때마다 +1을 해줬다.
            visited[k]+=1  

    print('#{} {}'.format(tc,max(visited)))   ### 이중에 제일 큰 값이 그 방앞을 여러명이 겹쳐서 지나가야하므로 그 횟수만큼 나눠서 
                                              ### 옮겨가야하기 때문에 max값을 구해줬다.

