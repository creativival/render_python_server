import time
from build_box import BuildBox

room_name = "1000"
build_box = BuildBox(room_name)

rotations = [
  [0, 0, 0],
  [30, 0, 0],
  [0, 30, 0],
  [0, 0, 30],
]

build_box.set_box_size(0.5)
build_box.set_build_interval(0.01)

for i in range(10):
  build_box.create_box(-1, i, 0, r=0, g=1, b=1)
  build_box.create_box(0, i, 0, r=1, g=0, b=0)
  build_box.create_box(1, i, 0, r=1, g=1, b=0)
  build_box.create_box(2, i, 0, r=0, g=1, b=1)

for i in range(5):
  build_box.remove_box(0, i * 2 + 1, 0)
  build_box.remove_box(1, i * 2, 0)

for rotation in rotations:
  pitch = rotation[0]
  yaw = rotation[1]
  roll = rotation[2]

  build_box.set_node(0, 0, 0, pitch=pitch, yaw=yaw, roll=roll)

  build_box.send_data()
  time.sleep(1)
