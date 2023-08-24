import noise
import numpy as np
from build_box import BuildBox

# ルームネームを設定
room_name = "1000"
build_box = BuildBox(room_name)

# ボクセルのサイズと建設間隔を設定
build_box.set_box_size(0.5)
build_box.set_build_interval(0.01)

# ノードの設定
build_box.translate(0, 0, 0, pitch=0, yaw=0, roll=0)

# 地形の大きさと細かさを定義
terrain_size = 100
terrain_resolution = 1

# 地形の起伏
terrain_amplitude = 10

# Perlinノイズのスケール
noise_scale = 0.1

# 地形を生成
for x in np.arange(-terrain_size / 2, terrain_size / 2, terrain_resolution):
    for z in np.arange(-terrain_size / 2, terrain_size / 2, terrain_resolution):
        # Perlinノイズによる高さと色の決定
        height = ((noise.pnoise2(x * noise_scale, z * noise_scale, octaves=6) + 1) / 2) * terrain_amplitude
        r, g, b = [(noise.pnoise3(x * noise_scale, height * noise_scale, z * noise_scale, octaves=3) + 1) / 2 for _ in range(3)]
        print(height)

        # ボクセルの作成
        build_box.create_box(x, height, z, r, g, b, 1)

# データを送信
build_box.send_data()
