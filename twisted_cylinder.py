from math import sin, cos, radians

from build_box import BuildBox

room_name = "6328"
build_box = BuildBox(room_name)

build_box.set_box_size(0.3)
build_box.set_build_interval(0.01)
build_box.change_shape('sphere')
build_box.set_command('float')

bottom_radius = 6
top_radius = 10
cylinder_height = 30
twist_count = 8
diff_angle = 15
repeat_count = 360 // diff_angle  # 24
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
    bottom_angle_i = diff_angle * i
    bottom_angle_i_plus_one = diff_angle * (i + 1)
    top_angle_i = diff_angle * (i + twist_count)
    top_angle_i_plus_one = diff_angle * (i + twist_count + 1)
    x1 = bottom_radius * cos(radians(bottom_angle_i))
    y1 = 0
    z1 = bottom_radius * sin(radians(bottom_angle_i))
    next_x1 = bottom_radius * cos(radians(bottom_angle_i_plus_one))
    next_y1 = 0
    next_z1 = bottom_radius * sin(radians(bottom_angle_i_plus_one))
    x2 = top_radius * cos(radians(top_angle_i))
    y2 = cylinder_height
    z2 = top_radius * sin(radians(top_angle_i))
    next_x2 = top_radius * cos(radians(top_angle_i_plus_one))
    next_y2 = cylinder_height
    next_z2 = top_radius * sin(radians(top_angle_i_plus_one))
    color = [c / 255 for c in hue_circle_colors[bottom_angle_i // color_range]]
    # 側面
    build_box.draw_line(x1, y1, z1, x2, y2, z2, color[0], color[1], color[2], 1)
    # 底面
    build_box.draw_line(x1, y1, z1, next_x1, next_y1, next_z1, color[0], color[1], color[2], 1)
    # 上面
    build_box.draw_line(x2, y2, z2, next_x2, next_y2, next_z2, color[0], color[1], color[2], 1)

# build_box.translate(0, 50, 0, pitch=0, yaw=0, roll=0)
build_box.send_data()
