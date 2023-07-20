from random import random, uniform
from build_box import BuildBox

room_name = "1000"
build_box = BuildBox(room_name)

build_box.set_box_size(0.3)
build_box.set_build_interval(0.01)
build_box.set_node(0, 30, 0)

for i in range(100):
  x = uniform(-30, 30)
  y = uniform(-30, 30)
  z = uniform(-30, 30)
  r = random()
  g = random()
  b = random()
  build_box.draw_line(0, 0, 0, x, y, z, r=r, g=g, b=b, alpha=1)

build_box.send_data()
