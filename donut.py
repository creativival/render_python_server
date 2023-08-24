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

for j in range(repeat_count):
    angle_j = diff_angle * j
    # color = [c / 255 for c in hue_circle_colors[angle_j // color_range]]
    radius = base_radius + amplitude_radius * cos(radians(angle_j))
    y0 = amplitude_radius * sin(radians(diff_angle * j))
    for i in range(repeat_count):
        angle_i = diff_angle * i
        angle_i_plus_one = diff_angle * (i + 1)
        x1 = radius * cos(radians(angle_i))
        y1 = y0
        z1 = radius * sin(radians(angle_i))
        x2 = radius * cos(radians(angle_i_plus_one))
        y2 = y0
        z2 = radius * sin(radians(angle_i_plus_one))
        color = [c / 255 for c in hue_circle_colors[angle_i // color_range]]
        build_box.draw_line(x1, y1, z1, x2, y2, z2, color[0], color[1], color[2], 1)

build_box.translate(0, 50, 0, pitch=0, yaw=0, roll=0)
build_box.send_data()
