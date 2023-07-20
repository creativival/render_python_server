import time
import matplotlib.pyplot as plt
import numpy as np
from build_box import BuildBox

room_name = "1000"
build_box = BuildBox(room_name)

build_box.set_box_size(0.3)
build_box.set_build_interval(0.01)

loop_count = 8
root_color = [0.5, 0, 0, 1]
branch_color = [0, 1, 0, 1]

def get_color(n):
    r = (root_color[0] - branch_color[0]) * (n / loop_count) + branch_color[0]
    g = (root_color[1] - branch_color[1]) * (n / loop_count) + branch_color[1]
    b = (root_color[2] - branch_color[2]) * (n / loop_count) + branch_color[2]

    return r, g, b

def draw_tree(n, position, length, angle):
    if n > 0:
        # 描画する線の座標を計算
        x0, y0 = position  # 前の線の終点が新たな線の始点
        x1, y1 = x0 + (length * np.cos(np.radians(angle))), y0 + (length * np.sin(np.radians(angle)))  # 線の終点を計算
        # print(x0, y0, x1, y1)
        r, g, b = get_color(n)
        build_box.draw_line(x0, y0, 0, x1, y1, 0, r=r, g=g, b=g, alpha=1)

        # 次の線を描画
        length *= 0.8
        draw_tree(n-1, [x1, y1], length, angle - 20)  # 左側の枝
        draw_tree(n-1, [x1, y1], length, angle + 20)  # 右側の枝

draw_tree(loop_count, position=[0, 0], length=20, angle=90)  # angle=90で上方向へ描画開始
build_box.send_data()

time.sleep(3)

build_box.set_node(0, 0, 0, 0, 45, 0)
build_box.send_data()

time.sleep(3)

build_box.set_node(0, 0, 0, 0, 90, 0)
build_box.send_data()
