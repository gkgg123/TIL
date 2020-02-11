import sys
import copy
sys.stdin=open('omok.txt','r')
dx=[1,1,0,1]
dy=[0,1,1,-1]

result=[]
omok=[list(map(int,input().split())) for i in range(19)]
temp=[]
win=0
for i in range(19):
    j=0
    cnt=0
    while j<19:
        if omok[i][j]==1:
            temp.append([i,j])
            cnt=1
            for t in range(1,19):
                ny=j+dy[2]*t
                if 0<=ny<19:
                    if omok[i][ny]==1:
                        temp.append([i,ny])
                        cnt+=1
                    else:
                        if cnt==5:
                            result.append(temp[:])
                            temp=[]
                            win=1
                            break
                        else:                
                            temp=[]
                            break
            if cnt==5:
                result.append(temp[:])
                temp=[]
                win=1 
        j=j+1+cnt
        cnt=0
temp=[]
for j in range(19):
    i=0
    cnt=0
    while i<19:
        if omok[i][j]==1:
            temp.append([i,j])
            cnt=1
            for t in range(1,19):
                nx=i+dx[0]*t
                if 0<=nx<19:
                    if omok[nx][j]==1:
                        temp.append([nx,j])
                        cnt+=1
                    else:
                        if cnt==5:
                            result.append(temp[:])
                            temp=[]
                            win=1                            
                            break
                        else:                
                            temp=[]                            
                            break
            if cnt==5:
                result.append(temp[:])
                temp=[]
                win=1 
        i=i+1+cnt
        cnt=0
temp=[]
temp_omok=copy.deepcopy(omok)
for i in range(19):
    for j in range(19):
        if temp_omok[i][j]==1:
            temp.append([i,j])
            cnt=1
            for t in range(1,19):
                nx=i+dx[1]*t
                ny=j+dy[1]*t
                if 0<=nx<19 and 0<=ny<19:
                    if temp_omok[nx][ny]==1:
                        temp.append([nx,ny])
                        cnt+=1
                        temp_omok[nx][ny]=0
                    else:
                        if cnt==5:
                            result.append(temp[:])
                            temp=[]
                            win=1
                            break
                        else:
                            temp=[]
                            break
            if cnt==5:
                result.append(temp[:])
                temp=[]
                win=1

temp_omok=copy.deepcopy(omok)
for i in range(19):
    for j in range(19):
        if temp_omok[i][j]==1:
            temp.append([i,j])
            cnt=1
            for t in range(1,19):
                nx=i+dx[3]*t
                ny=j+dy[3]*t
                if 0<=nx<19 and 0<=ny<19:
                    if temp_omok[nx][ny]==1:
                        temp.append([nx,ny])
                        cnt+=1
                        temp_omok[nx][ny]=0
                    else:
                        if cnt==5:
                            result.append(temp[:])
                            temp=[]
                            win=1
                            break
                        else:
                            temp=[]
                            break
            if cnt==5:
                result.append(temp[:])
                temp=[]
                win=1
temp=[]
for i in range(19):
    j=0
    cnt=0
    while j<19:
        if omok[i][j]==2:
            temp.append([i,j])
            cnt=1
            for t in range(1,19):
                ny=j+dy[2]*t
                if 0<=ny<19:
                    if omok[i][ny]==2:
                        temp.append([i,ny])
                        cnt+=1
                    else:
                        if cnt==5:
                            result.append(temp[:])
                            temp=[]
                            win=2
                            break
                        else:                
                            temp=[]
                            break
            if cnt==5:
                result.append(temp[:])
                temp=[]
                win=2 
        j=j+1+cnt
        cnt=0
temp=[]
for j in range(19):
    i=0
    cnt=0
    while i<19:
        if omok[i][j]==2:
            temp.append([i,j])
            cnt=1
            for t in range(1,19):
                nx=i+dx[0]*t
                if 0<=nx<19:
                    if omok[nx][j]==2:
                        temp.append([nx,j])
                        cnt+=1
                    else:
                        if cnt==5:
                            result.append(temp[:])
                            temp=[]
                            win=2
                            break
                        else:                
                            temp=[]
                            break
            if cnt==5:
                result.append(temp[:])
                temp=[]
                win=2
        i=i+1+cnt
        cnt=0
temp=[]
temp_omok=copy.deepcopy(omok)
for i in range(19):
    for j in range(19):
        if temp_omok[i][j]==2:
            temp.append([i,j])
            cnt=1
            for t in range(1,19):
                nx=i+dx[1]*t
                ny=j+dy[1]*t
                if 0<=nx<19 and 0<=ny<19:
                    if temp_omok[nx][ny]==2:
                        temp.append([nx,ny])
                        cnt+=1
                        temp_omok[nx][ny]=0
                    else:
                        if cnt==5:
                            result.append(temp[:])
                            temp=[]
                            win=2
                            cnt=0
                            break
                        else:
                            temp=[]
                            cnt=0
                            break
            if cnt==5:
                result.append(temp[:])
                temp=[]
                win=2

temp_omok=copy.deepcopy(omok)
for i in range(19):
    for j in range(19):
        if temp_omok[i][j]==2:
            temp.append([i,j])
            cnt=1
            for t in range(1,19):
                nx=i+dx[3]*t
                ny=j+dy[3]*t
                if 0<=nx<19 and 0<=ny<19:
                    if temp_omok[nx][ny]==2:
                        temp.append([nx,ny])
                        cnt+=1
                        temp_omok[nx][ny]=0
                    else:
                        if cnt==5:
                            result.append(temp[:])
                            temp=[]
                            win=2
                            break
                        else:
                            temp=[]
                            break  
            if cnt==5:
                result.append(temp[:])
                temp=[]
                win=2     
print(win)
# print(result)
if win!=0:
    min_x=9999
    min_y=9999
    for i in result:
        for j in i:
            if min_y>j[1]:
                min_y=j[1]
                min_x=j[0]
            elif min_y==j[1]:
                if min_x>j[0]:
                    min_x=j[0]
                
    print(min_x+1,min_y+1)

