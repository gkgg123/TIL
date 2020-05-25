import sys
def find(ar,ind):
    global N,L
    visited = [0]*N
    num=0
    ##### 탐색하는 index는 ind 이고, 그 열을 검색하기 위해서 num 인덱스를 통해 바꿔준다.
    prev=ar[num][ind]
    ##### 최초값을 prev이라 한다.
    cnt=1
    #### 그리고 경사로를 놓을수 있는 땅을 cnt라 지정했고, 처음에 1 이므로, cnt을 1로 했다.
    while num+1<=N-1: ##### 전체 인덱스 가능범위는 num+1 <=N-1까지 탐색을 하면 된다.
        nex = ar[num+1][ind]
        ##### prev의 다음위치의 값이다.
        if prev != nex:  #### 만약 prev와 nex가 다르면 경사로를 놓아야하므로 탐색해야한다.

            if prev <nex:  #### nex가 더 높은경우
                if prev+1 != nex:  #### 고도차이가 1보다 크면 중지하고 0을 반환해준다.
                    return 0

                else:

                    if cnt>= L: #### 그리고 놓을수 있는 땅이 L보다 크거나 같으면 놓을 가능성이 있으니 
                        for i in range(L):
                            if visited[num-i] != 0:
                                ### 경사로를 놓은적이 있는지 확인한다. 만약 놓았으면 길이 안되므로 0을 반환해준다.
                                return 0
                        for i in range(L):
                            ###### 경사로를 놓을수 있으면 놓아준다.
                            visited[num-i] = 1
                            cnt=0
                            #### 그리고 cnt를 0으로 초기화 해준다.
                    else:
                        #### 놓을수 있는 땅이 L보다 작으면 0을 반환해준다.
                        return 0
            else:
                if prev - 1 != nex:
                    #### 격차가 1보다 크면 0을 반환해준다.
                    return 0
                else:
                    if num+L > N-1:
                        ##### 경사로가 범위를 넘어갈경우 0을 반환해준다.
                        return 0
                    for i in range(L):                        
                        if ar[num+1+i][ind] != nex or visited[num+1+i]!=0:
                            ##### 경사로를 놓는 공간에서 nex의 값과 동일하지않으면 같은 높이가 아니라서 문제가 발생한다.
                            #### 그리고 경사로가 놓여져있으면 문제가 발생하므로, 확인해준다.
                            return 0
                    for i in range(L):
                        ### 그리고 검사가 완료되면 경사로를 깔아준다.
                        visited[num+1+i]=1
                    ### 그리고 cnt를 0으로 초기화해준다.
                    cnt=0

        prev = nex
        cnt += 1
        num += 1
    return 1
        








N,L = map(int,input().split())

arr_vertical = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
#### 원래 행렬

arr_horiz = list(map(list,list(zip(*arr_vertical))))
#### 행렬의 열과 행을 교체해준다.
result=0
for i in range(N):
    result+=find(arr_vertical,i)
    ##### 세로를 탐색한다.
    result+=find(arr_horiz,i)
    #### 가로를 탐색하는거와 동일하다.
print(result)


