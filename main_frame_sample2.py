from build_box import BuildBox
from polyhedra_data import polyhedra

# ルームネームを設定
room_name = "1000"
build_box = BuildBox(room_name)
build_box.set_box_size(0.1)
build_box.set_build_interval(0.01)
build_box.set_command('float')

# 正多面体を描画
size = 20

for name, poly in polyhedra.items():
    # フレームイン
    build_box.frame_in()

    vertices = poly['vertices']
    edges = poly['edges']
    color = poly['color']
    offset = poly['offset']

    # # ノードの設定
    offset_x, offset_y, offset_z = offset[0] * size, offset[1] * size, offset[2] * size

    for edge in edges:
        start, end = vertices[edge[0]], vertices[edge[1]]
        start = list(map(lambda x: x * size, start))
        end = list(map(lambda x: x * size, end))
        offset_start = [start[0] + offset_x, start[1] + offset_y, start[2] + offset_z]
        offset_end = [end[0] + offset_x, end[1] + offset_y, end[2] + offset_z]
        build_box.draw_line(*offset_start, *offset_end, *color)

    # フレームアウト
    build_box.frame_out()

# データを送信
build_box.send_data()
build_box.clear_data()
