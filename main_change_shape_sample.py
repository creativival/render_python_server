import time
from build_box import BuildBox

room_name = "1000"
build_box = BuildBox(room_name)

build_box.set_box_size(0.5)
build_box.set_build_interval(0.01)

for i in range(10):
  build_box.create_box(-1, i, 0, r=0, g=1, b=1, alpha=1)
  build_box.create_box(0, i, 0, r=1, g=0, b=0, alpha=1)
  build_box.create_box(1, i, 0, r=1, g=1, b=0, alpha=1)
  build_box.create_box(2, i, 0, r=0, g=1, b=1, alpha=1)

for i in range(5):
  build_box.remove_box(0, i * 2 + 1, 0)
  build_box.remove_box(1, i * 2, 0)

build_box.translate(0, 0, 0, pitch=0, yaw=0, roll=0)
build_box.send_data()

time.sleep(1)

build_box.translate(10, 0, 0, pitch=0, yaw=0, roll=0)
build_box.change_shape('sphere')
build_box.send_data()

time.sleep(1)

build_box.translate(20, 0, 0, pitch=0, yaw=0, roll=0)
build_box.change_shape('plane')
build_box.send_data()



build_box.send_data()
