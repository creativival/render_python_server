import random
from build_box import BuildBox

# ルームネームを設定
room_name = "1000"
build_box = BuildBox(room_name)

# ボクセルのサイズと建設間隔を設定
build_box.set_box_size(0.5)
build_box.set_build_interval(0.01)

# ノードの設定
build_box.translate(0, 0, 0, pitch=0, yaw=0, roll=0)

# 空間の大きさを定義
space_size = 100

# ランダムな線を引く回数を定義
lines = 200

for _ in range(lines):
    # 開始位置と終了位置をランダムに選択
    x1, y1, z1 = [random.uniform(-space_size / 2, space_size / 2) for _ in range(3)]
    x2, y2, z2 = [random.uniform(-space_size / 2, space_size / 2) for _ in range(3)]

    # 線の色をランダムに選択
    r, g, b = [random.random() for _ in range(3)]

    # 線を引く
    build_box.draw_line(x1, y1, z1, x2, y2, z2, r, g, b, 1)

# データを送信
build_box.send_data()
