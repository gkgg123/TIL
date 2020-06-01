for tc in range(int(input())):
  n = int(input())
  data = list(map(int,input().split()))
  start, end, cus = data[0:2], data[2:4], data[4:]
  cus = [(cus[i*2], cus[i*2+1]) for i in range(n)]
  dis_s = [9999]+[abs(start[0]-cus[i][0])+abs(start[1]-cus[i][1]) for i in range(n)]+[9999]
  dis_e = [9999]+[abs(end[0]-cus[i][0])+abs(end[1]-cus[i][1]) for i in range(n)]+[9999]
  dis = [dis_s] + [[dis_s[i+1]]+[abs(cus[i][0]-cus[j][0])+abs(cus[i][1]-cus[j][1]) for j in range(n)]+[dis_e[i+1]] for i in range(n)] + [dis_e]
  print(dis)
  for i in range(n+2):
    dis[i][i] = 9999
 
  min_ = min(dis_s)
  greedVisit = [dis_s.index(min_)]
  for _ in range(n-1):
    tmpMin = 999
    for i in range(1,n+1):
      if i not in greedVisit:
        tmpMin = min(dis[greedVisit[-1]][i], tmpMin)
    greedVisit.append(dis[greedVisit[-1]].index(tmpMin))
    min_ += tmpMin
  min_ += dis_e[greedVisit[-1]]
  print(min_)
  for i in range(1,n+1):
    stack = []
    stack.append([[i],dis_s[i]])
    while stack:
      visit, n_dis = stack.pop()
      if len(visit) == n:
        n_dis = n_dis+dis_e[visit[-1]]
        min_ = min(n_dis, min_)
        continue
      for i in range(1,n+1):
        if i not in visit:
          min__ = sum([min(dis[i]) for i in range(1,n+1) if i not in visit])+dis[visit[-1]][i]
          if n_dis+min__ < min_:
            stack.append([visit[:]+[i],n_dis+dis[visit[-1]][i]])
  print(f'#{tc+1} {min_}')