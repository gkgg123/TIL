import math


main_ball=[247,70]
move_b=[226.98648161512205, 119.63257503888575]
temp_x=abs(main_ball[0]-move_b[0])
temp_y=abs(main_ball[1]-move_b[1])

temp_deg=math.atan(temp_x/temp_y)
print(temp_x)
print(temp_y)
shoot_ang=360-math.degrees(temp_deg)

print(math.degrees(temp_deg))
print(shoot_ang)