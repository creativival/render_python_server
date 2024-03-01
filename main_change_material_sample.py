from time import sleep
from build_box import BuildBox

room_name = "1000"
build_box = BuildBox(room_name)

build_box.set_box_size(2)
build_box.set_build_interval(0.01)

colors = [
  [0, 0, 0],
  [1, 0, 0],
  [0, 1, 0],
  [0, 0, 1],
  [1, 1, 0],
  [1, 0, 1],
  [0, 1, 1],
  [1, 1, 1],
  [0.5, 0.5, 0.5],
  [0.5, 0, 0],
  [0, 0.5, 0],
  [0, 0, 0.5],
  [0.5, 0.5, 0],
  [0.5, 0, 0.5],
]

for i, color in enumerate(colors):
  build_box.create_box(0, i, 0, *color, alpha=1)

for i in range(5):
  build_box.change_material(is_metallic=False, roughness=0.25 * i)
  build_box.translate(i, 0, 0, pitch=0, yaw=0, roll=0)
  build_box.send_data()
  sleep(0.5)


for i in range(5):
  build_box.change_material(is_metallic=True, roughness=0.25 * i)
  build_box.translate(5 + i, 0, 0, pitch=0, yaw=0, roll=0)
  build_box.send_data()
  sleep(0.5)
