from time import sleep
from build_box import BuildBox

room_name = "1000"
build_box = BuildBox(room_name)

build_box.set_box_size(3)
build_box.set_build_interval(0.01)

for i in range(10):
  build_box.create_box(-1, i, 0, r=0, g=1, b=1, alpha=1)
  build_box.create_box(0, i, 0, r=1, g=0, b=0, alpha=1)
  build_box.create_box(1, i, 0, r=1, g=1, b=0, alpha=1)
  build_box.create_box(2, i, 0, r=0, g=1, b=1, alpha=1)

for i in range(5):
  build_box.remove_box(0, i * 2 + 1, 0)
  build_box.remove_box(1, i * 2, 0)

node_positions = [
  [0, 0, 0],
  [-10, 0, 0],
  [10, 0, 0],
  [0, -20, 0],
  [0, 20, 0],
  [0, 0, -10],
  [0, 0, 10]

]

for x, y, z in node_positions:
  build_box.translate(x, y, z, pitch=0, yaw=0, roll=0)
  build_box.send_data()
  sleep(1)

build_box.animate_global(0, 0, 0, 0, 180, 0, 1, 100)
build_box.send_data()
