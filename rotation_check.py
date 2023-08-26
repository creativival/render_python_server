from time import sleep
from build_box import BuildBox

room_name = "1000"
build_box = BuildBox(room_name)

build_box.set_box_size(1)
build_box.set_build_interval(0.01)
build_box.set_command('axis')

for i in range(10):
  build_box.create_box(i, 0, 0, r=0, g=1, b=1, alpha=1)

build_box.translate(0, 0, 0, pitch=0, yaw=0, roll=0)
build_box.send_data()
sleep(0.5)

build_box.translate(0, 0, 0, pitch=0, yaw=30, roll=0)
build_box.send_data()
sleep(0.5)

build_box.translate(0, 0, 0, pitch=0, yaw=30, roll=30)
build_box.send_data()
sleep(0.5)

build_box.translate(0, 0, 0, pitch=30, yaw=30, roll=30)
build_box.send_data()
sleep(0.5)

# 初期化
build_box.clear_data()

build_box.set_box_size(1)
build_box.set_build_interval(0.01)
build_box.set_command('axis')

for i in range(10):
  build_box.create_box(i, 0, 0, r=1, g=0, b=1, alpha=1)

build_box.push_matrix()

build_box.translate(0, 0, -15, pitch=0, yaw=0, roll=0)
build_box.send_data()
sleep(0.5)

build_box.push_matrix()

build_box.translate(0, 0, 0, pitch=0, yaw=30, roll=0)
build_box.send_data()
sleep(0.5)

build_box.push_matrix()

build_box.translate(0, 0, 0, pitch=0, yaw=0, roll=30)
build_box.send_data()
sleep(0.5)

build_box.push_matrix()

build_box.translate(0, 0, 0, pitch=30, yaw=0, roll=0)
build_box.send_data()
sleep(0.5)