from math import sin, cos, tan, radians
from build_box import BuildBox

room_name = "1000"
build_box = BuildBox(room_name)

build_box.set_box_size(0.05)
build_box.set_build_interval(0.01)

amplitude = 120

for i in range(-360, 361):
  for j in range(5):
    build_box.create_box(i, amplitude * sin(radians(i)) + j, 0, r=1, g=0, b=0, alpha=1)
    build_box.create_box(i, amplitude * cos(radians(i)) + j, -1, r=0, g=1, b=0, alpha=1)
    if i % 90 != 0:
      build_box.create_box(i, amplitude * tan(radians(i)) + j, -2, r=0, g=0, b=1, alpha=1)

build_box.send_data()
