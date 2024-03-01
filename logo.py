from build_box import BuildBox

room_name = "1000"
build_box = BuildBox(room_name)

build_box.set_box_size(5)
build_box.set_build_interval(0.01)

logo = [
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
]
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
color_count = len(hue_circle_colors)

base_height = 5

for i in range(24):
    color = [c / 255 for c in hue_circle_colors[i % color_count]]
    # print(i % len(hue_circle_colors), color)
    for j in range(8):
        x = i - 12
        y = 7 - j + base_height
        z = 0

        if logo[j][i] == 0:
            build_box.create_box(x, y, z, color[0], color[1], color[2], 1)
        else:
            build_box.create_box(x, y, z, 0, 0, 0, 1)

build_box.change_material(is_metallic=True, roughness=0)
build_box.send_data()
