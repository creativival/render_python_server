from build_box import BuildBox
import math

# ルームネームを設定
room_name = "1000"
build_box = BuildBox(room_name)

# ボクセルのサイズと建設間隔を設定
build_box.set_box_size(0.1)
build_box.set_build_interval(0.01)

# ノードの設定
build_box.set_node(0, 0, 0, pitch=0, yaw=0, roll=0)

# 円状のパターンを作成
for degree in range(360):
  radian = math.radians(degree)
  radius = 50  # 円の半径
  x = radius * math.cos(radian)
  z = radius * math.sin(radian)
  y = degree % 100  # ボクセルを高さ方向に配置

  # ボクセルの色を設定（スペクトラムのように）
  r = (math.sin(radian) + 1) / 2
  g = (math.sin(radian + 2 * math.pi / 3) + 1) / 2
  b = (math.sin(radian + 4 * math.pi / 3) + 1) / 2

  # ボクセルを作成
  build_box.create_box(x, y, z, r, g, b, 1)

# データを送信
build_box.send_data()
