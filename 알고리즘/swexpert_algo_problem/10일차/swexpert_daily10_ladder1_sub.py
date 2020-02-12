# def ladder(y):
#     result=0
#     x=0
#     while True:
#         if x==99 and arr[x][y]==2:
#             return 0
#         elif x==99:
#             return result
#         for t in [1,-1]:
#             if arr[x][y+t]:
#                 while arr[x][y+t]:
#                     y+=t
#                     result+=1
#                 break
#         x+=1
#         result+=1
    




# for tc in range(1,11):
#     input()
#     arr=[[0]+list(map(int,input().split()))+[0] for i in range(100)]
#     result=[]
#     for i in range(101):
#         if arr[0][i]==1:
#             result.append([ladder(i),i-1])
#     a=min(result)
#     print(a[1])
import sys

sys.stdin=open('ladder.txt','r')


for tc in range(1,11):
    int(input())

    arr=[list(map(int,input().split())) for i in range(100)]
    a=99
    result=0

    for y in range(100):
        if arr[a][y]==2:
            while a>0:
                if arr[a][y-1]==1 and 0<=y-1<=99:
                    while arr[a][y-1]:
                        y-=1
                elif 0<=y+1<=99 and arr[a][y+1]==1:
                    while 0<=y+1<=99 and arr[a][y+1]:
                        y+=1                        
                a-=1
            result=y

    print(result)



