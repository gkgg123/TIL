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
    best=[0, 0, 0,0,0]  ### 볼 번호, 홀까지 각도, 거리 
    for ind,bb in enumerate(b):
        b_x=bb[0]
        b_y=bb[1]
        if b_x <= 0 and b_y <= 0:
            continue
        else:
            for h_x,h_y in HOLES:
                len_c=math.sqrt((main_ball[0]-b_x)**2 +(main_ball[1]-b_y)**2)
                len_b=math.sqrt((h_x-b_x)**2 +(h_y-b_y)**2)
                len_a=math.sqrt((main_ball[0]-h_x)**2 +(main_ball[1]-h_y)**2)
                if abs(len_b**2+len_c**2-len_a**2)/(2*len_b*len_c)<1:
                    rad=math.acos((len_b**2+len_c**2-len_a**2)/(2*len_b*len_c))
                else:
                    if ((len_b**2+len_c**2-len_a**2)/(2*len_b*len_c))>0:
                        rad=math.acos(1)
                    else:
                        rad=math.acos(-1)
                deg=math.degrees(rad)



                if len_c>2.86:
                    ang_var=math.degrees(math.asin(2.86/len_c))
                else:
                    ang_var=0
                if abs(180-deg)<abs(180-best[0]):
                    ####
                    if b_x>=main_ball[0] and b_y>=main_ball[1]:
                        temp_x=b_x-main_ball[0]
                        temp_y=b_y-main_ball[1]
                        temp_hx=h_x-main_ball[0]
                        temp_hy=h_y-main_ball[1]
                        print('1사분면')
                        if temp_x:
                            temp_deg=math.atan(temp_y/temp_x)
                        else:
                            temp_deg=math.pi/2
                        temp_h_deg=math.atan(temp_hy/temp_hx)
                        if temp_deg>temp_h_deg:
                            shoot_ang=90-math.degrees(temp_deg)-(math.floor(ang_var*((180-deg)/180)))
                        else:
                            shoot_ang=90-math.degrees(temp_deg)+(math.floor(ang_var*((180-deg)/180)))


                    elif b_x>=main_ball[0] and b_y<main_ball[1]:
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
                        print('2사분면')
                        if temp_x:
                            temp_deg=math.atan(temp_y/temp_x)
                        else:
                            temp_deg=math.pi
                        if temp_deg>temp_h_deg:
                            shoot_ang=90+math.degrees(temp_deg)+(math.floor(ang_var*((180-deg)/180)))
                        else:
                            shoot_ang=90+math.degrees(temp_deg)-(math.floor(ang_var*((180-deg)/180)))
                    
                    elif b_x<main_ball[0] and b_y>=main_ball[1]:
                        temp_x=main_ball[0]-b_x
                        temp_y=b_y-main_ball[1]
                        temp_hx=main_ball[0]-h_x
                        temp_hy=h_y-main_ball[1]
                        temp_deg=math.atan(temp_y/temp_x)
                        temp_h_deg=math.atan(temp_hy/temp_hx)
                        print('4사분면')
                        if temp_deg>temp_h_deg:
                            shoot_ang=270+math.degrees(temp_deg)-(math.floor(ang_var*((180-deg)/180)))
                        else:
                            shoot_ang=270+math.degrees(temp_deg)+(math.floor(ang_var*((180-deg)/180)))
                    else:
                        temp_x=main_ball[0]-b_x
                        temp_y=main_ball[1]-b_y
                        temp_hx=main_ball[0]-h_x
                        temp_hy=main_ball[1]-h_y
                        temp_deg=math.atan(temp_y/temp_x)
                        temp_h_deg=math.atan(temp_hy/temp_hx)
                        print('열외')
                        if temp_deg>temp_h_deg:
                            shoot_ang=270-math.degrees(temp_deg)-(math.floor(ang_var*((180-deg)//180)))
                        else:
                            shoot_ang=270-math.degrees(temp_deg)+(math.floor(ang_var*((180-deg)//180)))
                    ####

                    best[0]=deg
                    best[1]=[len_c,len_b]
                    best[2]=[shoot_ang,ang_var]
                    best[3]=[b_x,b_y]
                    best[4]=[h_x,h_y]

            break
        

    print(best)
    angle=best[2][0]

    power=best[1][0]//3+best[1][0]*2//9
    if power<10:
        power=25
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
