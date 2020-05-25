T=int(input())
# dx = [0,0,-1,1]
# dy = [1,-1,0,0]


def crash(ar):
    result=[]
    for i in range(len(ar)-1):
        for j in range(i+1,len(ar)):
            dx = ar[i][0]-ar[j][0]
            dy = ar[i][1]-ar[j][1]
            dire1 = ar[i][2]
            dire2 = ar[j][2]
            if dx == 0 :
                if dy > 0:
                    if dire1 == 1 and dire2 == 0 : 
                        result.append([i, j , abs(dy)//2])
                else:
                    if dire1 == 0 and dire2 == 1 :
                        result.append([i , j , abs(dy)//2])
            elif dy == 0 :
                if dx > 0 :
                    if dire1 == 2 and dire2 == 3:
                        result.append([i,j,abs(dx)//2])
                else:
                    if dire1 == 3 and dire2 == 2:
                        result.append([i,j,abs(dx)//2])
            elif dx == dy :
                if dx < 0: 
                    if (dire1 == 3 and dire2 == 1) or (dire1 == 0 and dire2 == 2):
                        result.append([i, j, abs(dx)])
                else: 
                    if (dire1 == 2 and dire2 == 0) or (dire1 == 1 and dire2 == 3):
                        result.append([i, j, abs(dx)])
            elif dx == -dy:
                if dx < 0: # 우, 상 또는 하, 좌 조합일 때 충돌
                    if (dire1 == 3 and dire2 == 0) or (dire1 == 1 and dire2 == 2):
                        result.append([i, j, abs(dx)])
                else: # 좌, 하 또는 상, 우 조합일 때 충돌
                    if (dire1 == 2 and dire2 == 1) or (dire1 == 0 and dire2 == 3):
                        result.append([i, j, abs(dx)])    
            else:
                continue
    
    visited = [True]*len(ar)
    result.sort(key= lambda x : -x[2])
    energy = 0
    while result:
        loop_time = result[-1][2]
        temp=set()
        while loop_time == result[-1][2]:
            ind1,ind2,time = result.pop()
            if visited[ind1]==False or visited[ind2] == False:
                if result:
                    continue
                else:
                    break
            else:
                temp.add(ind1)
                temp.add(ind2)
            if len(result)==0:
                break
        for ind in temp:
            visited[ind]=False
            energy+=ar[ind][3]
    return energy
        









for tc in range(1,T+1):
    N=int(input())
    arr=[]
    for _ in range(N):
        temp=list(map(int,input().split()))
        temp[0]=temp[0]*2
        temp[1]=temp[1]*2
        arr.append(temp)
    

    result=crash(arr)
    print('#{} {}'.format(tc,result))