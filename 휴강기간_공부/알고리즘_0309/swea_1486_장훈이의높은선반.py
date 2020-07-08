### 장훈이의 높은선반  (조합 활용)###
T = int(input())

def combi(currind,value):
    global min_value,H,N
    ### min_value가 0이면 제일 적은것이므로 0이되면 계속 return 해준다.
    if min_value == 0:
        
        return
    ### value가 min_value보다 클때에 return해준다.
    if value > min_value:
        return
    ### 전체 크기만큼 도착하면,
    if currind == N:
        ### 크기를 비교해주고, value가 0보다 크거나 같을때에만 값을 교체해준다.
        if min_value > value and value>=0:
            min_value = value
        return
    ### 더하고 안더했을때 계속 재귀를 돌린다.
    combi(currind+1,value+arr[currind])
    combi(currind+1,value)
    return

for tc in range(1,T+1):
    N,H = map(int,input().split())
    arr = list(map(int,input().split()))
    ### min_value는 전체 합에서 장훈이의 키를 뺀것이 제일 큰 격차이므로, 이렇게 정했다.
    min_value = sum(arr)-H
    ### 계산의 편의성을 위해 0, -H을 초기값으로 했다. 0은 ind위치, -H는 계산값이다.
    combi(0,-H)
    print('#{} {}'.format(tc,min_value))