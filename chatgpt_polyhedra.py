from build_box import BuildBox
from polyhedra_data import polyhedra

# ルームネームを設定
room_name = "1000"
build_box = BuildBox(room_name)

# 正多面体を描画
size = 20

for name, poly in polyhedra.items():
  vertices = poly['vertices']
  edges = poly['edges']
  color = poly['color']
  offset = poly['offset']

  # ボクセルのサイズと建設間隔を設定
  build_box.set_box_size(0.1)
  build_box.set_build_interval(0.01)

  # ノードの設定
  offset_x, offset_y, offset_z = offset[0] * size, offset[1] * size, offset[2] * size
  build_box.translate(offset_x, offset_y, offset_z, pitch=60, yaw=0, roll=0)
  build_box.animate(0, 0, 0, pitch=0, yaw=180, roll=0, scale=1, interval=5)

  for edge in edges:
    start, end = vertices[edge[0]], vertices[edge[1]]
    start = map(lambda x: x * size, start)
    end = map(lambda x: x * size, end)
    build_box.draw_line(*start, *end, *color)

  # データを送信
  build_box.send_data()
  build_box.clear_data()
