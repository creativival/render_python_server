from math import pi
from build_box import BuildBox
from turtle import Turtle

room_name = "1000"
build_box = BuildBox(room_name)

build_box.set_box_size(0.3)
build_box.set_build_interval(0)
t = Turtle(build_box)

colors = [
  [0, 0, 0, 1],
  [1, 0, 0, 1],
  [0, 1, 0, 1],
  [0, 0, 1, 1],
  [1, 1, 0, 1],
  [0, 1, 1, 1],
  [1, 0, 1, 1],
  # [1, 1, 1, 1],
  # [0.5, 0, 0, 1],
  # [0, 0.5, 0, 1],
  # [0, 0, 0.5, 1],
  # [0.5, 0.5, 0, 1],
  # [0, 0.5, 0.5, 1],
  # [0.5, 0, 0.5, 1],
  # [0.5, 0.5, 0.5, 1],
]

for j, color in enumerate(colors):
  polar_phi = j * 180 / len(colors)
  t.reset()
  t.set_color(*color)
  t.set_pos(j, 0, 0)
  t.up(4)

  for i in range(180):
    t.forward(3)
    t.left(6)

build_box.send_data()