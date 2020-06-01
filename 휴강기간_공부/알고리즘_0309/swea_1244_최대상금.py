import sys

sys.stdin = open('swea_1244_최대상금.txt','r')

T = int(input())


def shuffle(array,cnt,value):
    global max_value,result

    flag = True
    ### 만약에 value와 max_value가 같고, 돌릴횟수가 짝수개가 남아있으면 최대값하고 동일하다.
    if max_value == value:
        if (N-cnt)%2 == 0:
            result = max_value
            return 

    ### 끝까지 왔을때 현재 result보다 value가 더 크면 바꿔준다.
    if cnt == N:
        if result < value:
            result = value
            return
        else:
            return 


    ### 리스트 내의 숫자끼리 비교를 해서 앞의 인덱스보다 뒤에 인덱스에 더 큰값이 있으면, 바꿔서 탐색을 해준다.
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            if array[i] < array[j]:
                new_arr = array[:]
                new_arr[i],new_arr[j] = new_arr[j],new_arr[i]
                new_value = int(''.join(new_arr))

                ### 그런데 이미 그 단계에서 탐색한 적이 있는지 확인해준다. 밑에 설명했듯이 같은걸 반복해서 탐색할 이유가 없다.
                if new_value not in dist[cnt]:
                    shuffle(new_arr,cnt+1,new_value)
                    dist[cnt].append(new_value)
                
                ### 이 flag는 최초에 최대값하고 동일해서 바꿀수 없을때를 알기 위해서 해놓은것이다.
                flag = False

    #### 만약 21 1 이라는 인풋이 들어오면 최대값이고, 뒤에 인덱스보다 앞의 인덱스의 값이 크므로 위의 반복문에서 진행이 안된다.
    #### 그런데 문제에서는 회수에 따라 강제적으로 바꿔서 탐색을해야한다.
    #### 그러므로 위에서 flag가 True이고, cnt = 0 일때 강제적으로 바꿔주는 과정을 포함시켰다.
    if flag and cnt ==0:
        for i in range(len(array)-1):
            for j in range(i+1,len(array)):
                new_arr = array[:]
                new_arr[i],new_arr[j] = new_arr[j],new_arr[i]
                new_value = int(''.join(new_arr))
                if new_value not in dist[cnt]:
                    shuffle(new_arr,cnt+1,new_value)
                    dist[cnt].append(new_value)
            


for tc in range(1,T+1):

    arr,N = input().split()
    N = int(N)
    #### N은 인트화, arr은 그냥 리스트만 한다. 왜냐하면, 정수로 했을시 다 더해서 계산하는게 귀찮으므로, join을 통해 합쳐서 int화를 시킬예정 
    arr = list(arr)
    #### 똑같은 횟수에서 같은걸 반복해서 찾을 필요가 없다.
    #### 만약 숫자가 3332 라고 있으면
    #### 1번째와 2번째를 바꾼 3332 와
    #### 2번째와 3번째를 바꾼 3332 는 동일하다.
    #### 그러니 중복된 수를 빼기 위해 백트래킹을 해주었다.
    dist = {i : [] for i in range(N+1)}
    #### cnt가 짝수개가 남았을때 최대값하고 똑같으면, 더이상 진행할 필요가 없으므로, max_value를 만들어주었다.
    max_value = int(''.join(sorted(arr,reverse=True)))
    ### result는 결과를 보기 위함이다.
    result = 0
    ### 입력으로 현재의 행렬, 현재의 cnt(바꾼횟수), 현재의 value를 넣어준다.
    shuffle(arr,0,int(''.join(arr)))
    print('#{} {}'.format(tc,result))
