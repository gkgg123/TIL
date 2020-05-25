import socket
import time
import math

# User and Game Server Information
NICKNAME = 'mmm lee'
HOST = '127.0.0.1'
PORT = 1447 # Do not modify

# predefined variables(Do not modify these values)
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 5
HOLES = [ [0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127] ]

class Conn:
    def __init__(self):
        self.sock = socket.socket()
        print('Trying to Connect: ' + HOST + ':' + str(PORT))
        self.sock.connect((HOST, PORT))
        print('Connected: ' + HOST + ':' + str(PORT))
        send_data = '9901/' + NICKNAME
        self.sock.send(send_data.encode('utf-8'))
        print('Ready to play.\n--------------------')
    def request(self):
        self.sock.send('9902/9902'.encode())
        print('Received Data has been currupted, Resend Requested.')
    def receive(self):
        recv_data = (self.sock.recv(1024)).decode()
        print('Data Received: ' + recv_data)
        return recv_data
    def send(self, angle, power):
        merged_data = '%d/%d' % (angle, power)
        self.sock.send(merged_data.encode('utf-8'))
        print('Data Sent: ' + merged_data)
    def close(self):
        self.sock.close()

class GameData:
    def __init__(self):
        self.reset()
    def reset(self):
        self.balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]
    def read(self, conn):
        recv_data = conn.receive()
        split_data = recv_data.split('/')
        idx = 0    
        try:
            for i in range(NUMBER_OF_BALLS):
                for j in range(2):
                    self.balls[i][j] = int(split_data[idx])
                    idx += 1
        except:
            self.reset()
            conn.request()
            self.read(conn)
    def show(self):
        print('=== Arrays ===')
        for i in range(NUMBER_OF_BALLS):
            print('Ball%d: %d, %d' % (i, self.balls[i][0], self.balls[i][1]))
        print()

# 자신의 차례가 되어 게임을 진행해야 할 때 호출되는 Method

def play(conn, gameData):

    main_ball=gameData.balls[0]
    b=gameData.balls[1:]
    best=[0, 0, 0,0,0]  ### 1. 사이각 2. 수구하고 목적구와의 거리, 목적구와 홀까지의 거리, 3. 발사각도, 발사각도 조절가능 범위 4.목적구의 좌표 5. 홀의 좌표
    for ind,bb in enumerate(b):
        b_x=bb[0]
        b_y=bb[1]
        if b_x <= 0 and b_y <= 0:  ### 볼이 들어갔을때에는 필요없으므로, 빼줬다. 볼의 0,0 이나 -1,-1에 위치하면 볼이 없는것으로 판별했다.
            continue
        else:
            for h_x,h_y in HOLES:
                len_c=math.sqrt((main_ball[0]-b_x)**2 +(main_ball[1]-b_y)**2)   ### 수구하고 목적구의 거리
                len_b=math.sqrt((h_x-b_x)**2 +(h_y-b_y)**2)                     ### 목적구와 홀의 거리
                len_a=math.sqrt((main_ball[0]-h_x)**2 +(main_ball[1]-h_y)**2)   ### 수구하고 홀의 거리
                if abs(len_b**2+len_c**2-len_a**2)/(2*len_b*len_c)<1:           ### 코사인 제2법칙을 하는데, cos은 1초과가 나올수 없는데. 1초과가 나오는경우가 발생할경우를 대비
                    rad=math.acos((len_b**2+len_c**2-len_a**2)/(2*len_b*len_c))  ### 1미만일때에는 원래의 코사인 제2 법칙으로, 목적구의 사이각을 구해준다.
                else:
                    if ((len_b**2+len_c**2-len_a**2)/(2*len_b*len_c))>0:      ### 1 이상 -1 미만이 나왔을때 1 이상이면 0도를 하기 위해 acos1
                        rad=math.acos(1)                                      ### -1 미만이면 180도가 나오기 위해, -1
                    else:
                        rad=math.acos(-1)
                deg=math.degrees(rad)                                     ##### 라디안을 각도로 변환 ####



                if len_c>2.86:
                    ang_var=math.degrees(math.asin(2.86/len_c))                #### 수구하고 목적구의 거리가 반지름보다 크면 asin으로 발사각도 조절가능범위를 구해준다.
                else:
                    ang_var=0                                                ### 반지름보다 작거나 같으면 발사각도 조절범위를 0으로 하낟.
                
                
                if abs(180-deg)<abs(180-best[0]):            ### 최상의 각도를 찾는 방법을, 목적구의 사이각이 180도와 가장 가까운걸 best로 했다.
                    ####
                    
                    if b_x>=254 or b_x<=0 or b_y>=127 or b_y<=0:         ### 게임 특성상 정해진 범위인 x좌표 0~254 y좌표 0~127을 넘는 홀 안에서 멈추는 경우가 발생한다.
                        if b_x>=main_ball[0] and b_y>=main_ball[1]:      ### 그럴때에는 직선타를 날려줘야하므로 따로 해줬고, 수구를 기준으로 목적구의 위치가 1,2,3,4 분면에
                                temp_x=b_x-main_ball[0]                  ### 위치할때를 구분해서 나눠준거다.
                                temp_y=b_y-main_ball[1]
                                if temp_x:                               ### 목적구의 x좌표와 수구의 x좌표가 같을때에는 atan이 안되므로 예외처리를 해줬다.
                                    temp_deg=math.atan(temp_y/temp_x)
                                else:
                                    temp_deg=math.pi/2
                                
                                shoot_ang=90-math.degrees(temp_deg)                     
        


                        elif b_x>=main_ball[0] and b_y<main_ball[1]:
                            temp_x=b_x-main_ball[0]
                            temp_y=main_ball[1]-b_y
                      
                            if temp_x:
                                temp_deg=math.atan(temp_y/temp_x)
                            else:
                                temp_deg=math.pi
                            shoot_ang=90+math.degrees(temp_deg)
                        
                        elif b_x<main_ball[0] and b_y>=main_ball[1]:
                            temp_x=main_ball[0]-b_x
                            temp_y=b_y-main_ball[1]
                            temp_deg=math.atan(temp_y/temp_x)
                     
                            shoot_ang=270+math.degrees(temp_deg)
                        else:
                            temp_x=main_ball[0]-b_x
                            temp_y=main_ball[1]-b_y
                            
                            temp_deg=math.atan(temp_y/temp_x)
                            
                            
                            shoot_ang=270-math.degrees(temp_deg)
                            ################################################################ 위에까지가 홀에 끼었을시 직선타를 해주는거다. ##########################

                    else: 
                        ###### 여기서 부터 일반적으로 샷을 하는 경우를 대비하여 변수들을 만들어주는거다.
                        if h_x != b_x:                        #### 홀의 x좌표와 목적구의 x좌표가 같으면 atan이 안되므로, 예외처리를 해줬다.
                            k=(h_y-b_y)/(h_x-b_x)            ### 홀과 목적구를 직선연결을 하면, 기울기가 나오는데, 
                            k_deg=abs(math.atan(k))         ### 기울기 k를 이용해서 홀과 목적구의 직선의 각도를 구해줬다.
                        else:
                            k='si'

                        if k != 'si':  #### 홀의 x좌표와 목적구의 x좌표가 같지 않을시에,정상시행했다. 
                            if b_x >h_x and b_y>= h_y:      ### 여기도 1,2,3,4 분면을 나눠서 시행을 해줬고 똑같다.
                                dx = 5*math.cos(k_deg)      ### 위에서 구한 직선의 각도를 이용해, dx,dy를 구해줬다. 
                                dy = 5*math.sin(k_deg)     ### 여기서 5는 원래 구의 지름이 되어야하는데, 구의 지름으로 할시 스쳐지나가므로 5로 낮춰줬다.
                                move_b = [b_x+dx,b_y+dy]    ### move_b는 수구가 여기로 와야지, 목적구를 칠수있는 위치이다.
                            elif b_x>h_x and b_y<h_y: 
                                dx = 5*math.cos(k_deg)      ### 이게 가능한 이유는 당구의 원리 중 목적구와 수구의 중심축을 이었을때의 방향으로 당구공이 진행하기 때문에,
                                dy = 5*math.sin(k_deg)      ### 그 방향을 홀의 방향으로 먼저 설정을 해줬고, 거기에 수구가 오도록 만들어준 방법이다.
                                move_b = [b_x+dx,b_y-dy]
                            elif b_x<h_x and b_y<h_y:
                                dx = 5*math.cos(k_deg)
                                dy = 5*math.sin(k_deg)
                                move_b = [b_x-dx,b_y-dy]
                            elif b_x<h_x and b_y>=h_y:
                                dx = 5*math.cos(k_deg)
                                dy = 5*math.sin(k_deg)
                                move_b = [b_x-dx,b_y+dy]
                  
                       
                        else: ### 이 부분은 홀의 x좌표와 목적구의 x좌표가 같다는것은 목적구의 상하에 위치하는것이기 때문에, 수구도 목적구의 상항에 위치하도록 만들어준것이다.

                            if b_y<h_y: 
                                move_b=[b_x,b_y-5.6]
                            else:
                                move_b=[b_x,b_y+5.6]
    
                             ####################################################여기 까지가 일반적인 방법으로 치는경우를 대비해서 값을 뽑아낸 곳이다.

                        
                        
                        ####### 여기는 우리가 움직여야할 위치인 move_b 와 수구의 위치인 main_ball을 이용해, 두 x,y좌표끼리의 각각의 길이를 ㄱ ㅜ해서,
                        ##### atan을 이용해 각도를 구하고 그것을 기반으로 발사각도를 구하는것이다.
                        temp_x=abs(main_ball[0]-move_b[0])
                        temp_y=abs(main_ball[1]-move_b[1])
                        if len_c>5.72: #### 일반적으로 치는경우에는 수구와 목적구의 위치가 당구공의 반지름 이상에서야 효과가 있으므로, 구분을 해줬다.

                            if main_ball[0]<move_b[0] and main_ball[1]<=move_b[1]: ### 여기서부터는 1,2,3,4분면에 따라 방법이 바뀌는거다.
                                temp_deg=math.atan(temp_y/temp_x)
                                shoot_ang=90-math.degrees(temp_deg)


                            elif main_ball[0]<move_b[0] and main_ball[1]>move_b[1]:
                                temp_deg=math.atan(temp_y/temp_x)
                                shoot_ang=90+math.degrees(temp_deg)

                            elif main_ball[0]>move_b[0] and main_ball[1]<=move_b[1]:
                                temp_deg=math.atan(temp_y/temp_x)
                                shoot_ang=270+math.degrees(temp_deg)

                            elif main_ball[0]>move_b[0] and main_ball[1]>move_b[1]:
                                temp_deg=math.atan(temp_y/temp_x)
                                shoot_ang=270-math.degrees(temp_deg)
                            else:
                                    ### 마지막은 수구와 x좌표와 move_B의 x좌표가 같을시 0도 아니면 180도로 발사해야하므로 예외처리를 해줬다.
                                if main_ball[1]<move_b[1]:
                                    shoot_ang=0
                                else:
                                    shoot_ang=180
################################################ 위에까지가 일반적으로 치는 경우이다. ##########################3

                        else: #### 수구와 목적구의 거리가 지름 미만일시에는 다른방법으로 치는것이다.
                              ### 수구와 목적구와 홀의 사이각을 알고, 위에서 구한 발사각도의 조절범위를 아니깐, 그것을 이용해서 결정해줬다. 
                            if b_x>=main_ball[0] and b_y>=main_ball[1]: ### 1사분면에서 하는 방법이다.
                                temp_x=b_x-main_ball[0] 
                                temp_y=b_y-main_ball[1]
                                temp_hx=h_x-main_ball[0]
                                temp_hy=h_y-main_ball[1]
           
                                if temp_x:           ###### atan을 이용하므로 temp_x가 0이되면 안 구해지므로, 구분을 해주는거다.
                                    temp_deg=math.atan(temp_y/temp_x)
                                else:
                                    temp_deg=math.pi/2


                                if temp_hx: ## temp_hx도 위와 동일 
                                    temp_h_deg=math.atan(temp_hy/temp_hx)
                                else:
                                    if h_y>main_ball[1]:   ### 홀의 위치에 따라 0도 180도를 정해준거다.
                                        temp_h_deg=0
                                    else:
                                        temp_h_deg=math.pi


                        
                                if temp_deg>temp_h_deg:    ### 1사분면에 홀과 목적구가 위치할때, 

                                    shoot_ang=90-math.degrees(temp_deg)-(math.floor(ang_var*((180-deg)/180)))
                                    ###목적구와 수구의 절대각도가 홀과 수구의 절대각도보다 큰  경우에는 목적구의 위쪽을 쳐야 홀로 갈수 있으므로, 각도를 빼줬고,
                                else:
                                    shoot_ang=90-math.degrees(temp_deg)+(math.floor(ang_var*((180-deg)/180)))  ### 각도를 더해줬다.,
                                    ### 또한 사이각이 클수록 홀이 상대적으로 평평한 위치에 있으므로, 얉게 쳐야하므로 (180-deg)에 비례해서 발사각도를 조정해줬다.


                            elif b_x>=main_ball[0] and b_y<main_ball[1]: ### 밑에는 같은 원리이고 2사분면이다.
                                temp_x=b_x-main_ball[0]
                                temp_y=main_ball[1]-b_y
                                temp_hx=h_x-main_ball[0]
                                temp_hy=main_ball[1]-h_y
                                if temp_hx:
                                    temp_h_deg=math.atan(temp_hy/temp_hx)
                                else:
                                    if h_y>main_ball[1]:
                                        temp_h_deg=0
                                    else:
                                        temp_h_deg=math.pi
            
                                if temp_x:
                                    temp_deg=math.atan(temp_y/temp_x)
                                else:
                                    temp_deg=math.pi
                                if temp_deg>temp_h_deg:
                                    shoot_ang=90+math.degrees(temp_deg)+(math.floor(ang_var*((180-deg)/180)))
                                else:
                                    shoot_ang=90+math.degrees(temp_deg)-(math.floor(ang_var*((180-deg)/180)))
                            
                            elif b_x<main_ball[0] and b_y>=main_ball[1]:   ### 여기는 4 사분면이다.
                                temp_x=main_ball[0]-b_x
                                temp_y=b_y-main_ball[1]
                                temp_hx=main_ball[0]-h_x
                                temp_hy=h_y-main_ball[1]
                                temp_deg=math.atan(temp_y/temp_x)
                                if temp_hx:
                                    temp_h_deg=math.atan(temp_hy/temp_hx)
                                else:
                                    if h_y>main_ball[1]:
                                        temp_h_deg=0
                                    else:
                                        temp_h_deg=math.pi

                                if temp_deg>temp_h_deg:
                                    shoot_ang=270+math.degrees(temp_deg)-(math.floor(ang_var*((180-deg)/180)))
                                else:
                                    shoot_ang=270+math.degrees(temp_deg)+(math.floor(ang_var*((180-deg)/180)))
                            
                            
                            
                            else:  ##################### 여기는 3사분면이다.
                                temp_x=main_ball[0]-b_x
                                temp_y=main_ball[1]-b_y
                                temp_hx=main_ball[0]-h_x
                                temp_hy=main_ball[1]-h_y
                                temp_deg=math.atan(temp_y/temp_x)
                                if temp_hx:
                                    temp_h_deg=math.atan(temp_hy/temp_hx)
                                else:
                                    if h_y>main_ball[1]:
                                        temp_h_deg=0
                                    else:
                                        temp_h_deg=math.pi

                                if temp_deg>temp_h_deg:
                                    shoot_ang=270-math.degrees(temp_deg)-(math.floor(ang_var*((180-deg)//180)))
                                else:
                                    shoot_ang=270-math.degrees(temp_deg)+(math.floor(ang_var*((180-deg)//180)))
                        
                    ##################### 이렇게 구한것을 best에 저장을 시켜줬다.
                    best[0]=deg
                    best[1]=[len_c,len_b]
                    best[2]=[shoot_ang,ang_var]
                    best[3]=[b_x,b_y]
                    best[4]=[h_x,h_y]

            break ### 우리는 낮은번호부터 쳐야하므로, 볼이 들어가지 않았을때, 딱1번 시행을 하고 break로 나오도록 설정해줬다.
        

    angle=round(best[2][0])  ### 위에서 구한 발사각도를 반올림을 해줬다. 왜냐하면 여기서는 int형이기때문에 최대한 비슷한 각도로 보내기 위해서다.
    
    power=best[1][0]//3+best[1][0]*4//14  ### 수구와 목적구의 거리를 3으로 나눈몫을 하면 딱 달라붙을 정도의 파워가 나온다. 
                                          ### 하지만 그럴시에는 공을 집어넣을수 없으므로, 목적구와 홀까지의 거리에 따라 파워를 조정하도록 했다.

    if power<=25:             #### 그리고 필연상 수구와 목적구의 거리, 목적구와 홀의 거리가 낮을시 너무 낮은 파워가 되는데. 

        power=50*(power/30)+25   ### 그때는 오히려 파워가 필요한 경우도 있고, 교착상태에 빠질수도 있으므로, 파워를 더 크게해서 만들어줬다.

        
    ######################################################################################
    # 주석을 지우고, 이 곳에 주어진 정보를 바탕으로 게임 로직을 구현하여 자동으로 플레이할 수 있도록 구현합니다.
    # 필요한 결괏값은 방향(angle)과 세기(power)로 두 변수의 값이 결정되도록 만들어야 합니다.
    ######################################################################################
    conn.send(angle, power)


def main():
    conn = Conn()
    gameData = GameData()
    while True:
        gameData.read(conn)
        gameData.show()
        if gameData.balls[0][0] == 9909:
            break
        play(conn, gameData)        
    conn.close()
    print('Connection Closed')

if __name__ == '__main__':
    main()
