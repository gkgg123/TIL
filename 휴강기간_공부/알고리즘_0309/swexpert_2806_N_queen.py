import sys
sys.stdin=open('2806.txt','r')

T=int(input())
def backtracking(x):
    global cnt
    for i in range(x+1):  ### 만약 지금까지 백트링 한 범위안에
        if x!=i:         ### x!-i 일때
            if (visited[i]==visited[x]) or (abs(visited[i]-visited[x])==abs(i-x)):
                #### 같은 열에 위치하거나 ###      #### 대각선에 똑같이 위치하면 ####
                return   ### 검사를 중지하고 돌아간다.###
    if x==N-1:    ### 끝까지 왔으면 검사종료 #####
        cnt+=1
        return
    for i in range(N):   #### N까지 가면서
        visited[x+1]=i   #### visited[x+1]에 i값을 집어넣는다.
        backtracking(x+1)   #### 그리고 백트래킹을 한다.




for tc in range(1,T+1):
    N=int(input())
    cnt=0
    visited=[-1]*11  ## 제일 큰 N이 10이니 11개 만들어줌
    for i in range(N):
        visited[0]=i    ### 0번째 행에 i열에 위치시킨다고 가정
        backtracking(0)   ### 그리고 백 트래킹

    print('#{} {}'.format(tc,cnt))