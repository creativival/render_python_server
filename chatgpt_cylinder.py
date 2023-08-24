from build_box import BuildBox
import math

# ルームネームを設定
room_name = "1000"
build_box = BuildBox(room_name)

# ボクセルのサイズと建設間隔を設定
build_box.set_box_size(0.5)
build_box.set_build_interval(0.01)

# ノードの設定
build_box.translate(0, 0, 0, pitch=0, yaw=0, roll=0)

# 円柱のパターンを作成
radius = 15  # 円柱の半径
height = 50  # 円柱の高さ
for degree in range(360):
  for y in range(height):
    radian = math.radians(degree)
    x = radius * math.cos(radian)
    z = radius * math.sin(radian)

    # ボクセルの色を設定（スペクトラムのように）
    r = (math.sin(radian + y * 0.01) + 1) / 2
    g = (math.sin(radian + y * 0.01 + 2 * math.pi / 3) + 1) / 2
    b = (math.sin(radian + y * 0.01 + 4 * math.pi / 3) + 1) / 2

    # ボクセルを作成
    build_box.create_box(x, y, z, r, g, b, 1)

# データを送信
build_box.send_data()
