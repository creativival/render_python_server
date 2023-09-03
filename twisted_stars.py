from math import sin, cos, radians
from time import sleep
from build_box import BuildBox

room_name = "1000"
radius = 10
inner_radius = 5
angle_num = 5
height = 100

build_box = BuildBox(room_name)
build_box.set_box_size(0.3)
build_box.set_build_interval(0.01)
build_box.set_command('float')

for i in range(angle_num):
    x1 = radius * cos(radians(i * 360 / angle_num))
    y1 = 0
    z1 = radius * sin(radians(i * 360 / angle_num))
    x2 = radius * cos(radians((i + 1) * 360 / angle_num))
    y2 = 0
    z2 = radius * sin(radians((i + 1) * 360 / angle_num))
    x3 = inner_radius * cos(radians((i + 0.5) * 360 / angle_num))
    y3 = 0
    z3 = inner_radius * sin(radians((i + 0.5) * 360 / angle_num))

    build_box.draw_line(x1, y1, z1, x3, y3, z3, r=0, g=1, b=1, alpha=1)
    build_box.draw_line(x3, y3, z3, x2, y2, z2, r=1, g=1, b=0, alpha=1)
    # build_box.draw_line(x2, y2, z2, x1, y1, z1, r=1, g=0, b=0, alpha=1)

for i in range(height):
    rotation_angle = i * 720 / height
    build_box.translate(0, i * 2, 0, pitch=0, yaw=rotation_angle, roll=0)
    build_box.send_data()
    sleep(1)
