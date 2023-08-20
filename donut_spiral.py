from math import sin, cos, radians

from build_box import BuildBox

room_name = "1000"
build_box = BuildBox(room_name)

build_box.set_box_size(0.3)
build_box.set_build_interval(0.01)

amplitude_radius = 5
base_radius = 20
diff_angle = 5
repeat_count = 360 // diff_angle
hue_circle_colors = [
    [255, 0, 0],
    [255, 127, 0],
    [255, 255, 0],
    [127, 255, 0],
    [0, 255, 0],
    [0, 255, 127],
    [0, 255, 255],
    [0, 127, 255],
    [0, 0, 255],
    [127, 0, 255],
    [255, 0, 255],
    [255, 0, 127],
]
color_count = len(hue_circle_colors)  # 12
color_range = 360 // color_count  # 30

for i in range(repeat_count):
    angle_i = diff_angle * i
    angle_i_plus_one = diff_angle * (i + 1)
    radius_i = base_radius + amplitude_radius * cos(radians(angle_i * 4))
    radius_i_plus_one = base_radius + amplitude_radius * cos(radians(angle_i_plus_one * 4))
    y_i = amplitude_radius * sin(radians(angle_i * 4))
    y_i_plus_one = amplitude_radius * sin(radians(angle_i_plus_one * 4))
    color = [c / 255 for c in hue_circle_colors[angle_i // color_range]]
    x1 = radius_i * cos(radians(angle_i))
    y1 = y_i
    z1 = radius_i * sin(radians(angle_i))
    x2 = radius_i_plus_one * cos(radians(angle_i_plus_one))
    y2 = y_i_plus_one
    z2 = radius_i_plus_one * sin(radians(angle_i_plus_one))
    build_box.draw_line(x1, y1, z1, x2, y2, z2, color[0], color[1], color[2], 1)

for i in range(6):
    yaw = 15 * i
    build_box.set_node(0, 50, 0, pitch=0, yaw=yaw, roll=0)
    build_box.send_data()
