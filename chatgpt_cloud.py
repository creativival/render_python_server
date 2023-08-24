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

# 雲の大きさと細かさを定義
cloud_size = 100
cloud_resolution = 1

# 雲の高さ範囲
cloud_min_height = 30
cloud_max_height = 50

# 雲の最大の厚み
cloud_max_thickness = 20

# Perlinノイズのスケール
noise_scale = 0.1

# パステルカラーの係数（大きいほど色が薄くなる）
pastel_factor = 0.5

# 雲の生成の閾値
cloud_threshold = 0

# 雲を生成
for x in np.arange(-cloud_size / 2, cloud_size / 2, cloud_resolution):
  for z in np.arange(-cloud_size / 2, cloud_size / 2, cloud_resolution):
    # Perlinノイズによる高さと色の決定
    base_height_noise = noise.pnoise2(x * noise_scale, z * noise_scale, octaves=6)
    top_height_noise = noise.pnoise2((x + cloud_size) * noise_scale, (z + cloud_size) * noise_scale, octaves=6)
    print(base_height_noise, top_height_noise)

    # 雲の基本高さと上部の高さ
    base_height = ((base_height_noise + 1) / 2) * (cloud_max_height - cloud_min_height) + cloud_min_height
    top_height = ((top_height_noise + 1) / 2) * (cloud_max_height - cloud_min_height) + cloud_min_height
    # print(base_height - cloud_min_height, top_height - cloud_min_height)

    # 雲の生成の閾値を適用
    if base_height_noise < cloud_threshold and top_height_noise < cloud_threshold:
      continue

    # 上部の高さが基本高さより低い場合は、上部の高さを基本高さに合わせる
    if top_height < base_height:
      top_height = base_height

    r, g, b = [(pastel_factor + (1 - pastel_factor) * (
          noise.pnoise3(x * noise_scale, base_height * noise_scale, z * noise_scale, octaves=3) + 1) / 2) for _ in
               range(3)]

    for y in np.arange(base_height, top_height, cloud_resolution):
      # ボクセルの作成
      build_box.create_box(x, y, z, r, g, b, 1)

# データを送信
build_box.send_data()
