from build_box import BuildBox
import numpy as np
import math

# ルームネームを設定
room_name = "1000"
build_box = BuildBox(room_name)

# ボクセルのサイズと建設間隔を設定
build_box.set_box_size(0.5)
build_box.set_build_interval(0.01)

# ノードの設定
build_box.translate(0, 0, 0, pitch=0, yaw=0, roll=0)

# 円柱の設定
radius = 5
height = 100
num_turns = 1  # 円柱が絡み合う回数
thickness = 6  # 円柱の太さ

# 円柱の生成
for y in np.arange(0, height, 0.1):
  for i in range(2):  # 2本の円柱
    theta = y * num_turns * 2 * np.pi / height + i * np.pi  # 角度（螺旋を生成するためにyに依存）
    for t in np.arange(0, thickness, 0.5):  # 太さを考慮
      x = (radius + t) * np.cos(theta)
      z = (radius + t) * np.sin(theta)

      if i == 0:  # 1本目の円柱は白色
        r, g, b = 1, 1, 1
      else:  # 2本目の円柱は赤色
        r, g, b = 1, 0, 0

      # ボクセルを作成
      build_box.create_box(x, y, z, r, g, b, 1)

# データを送信
build_box.send_data()
