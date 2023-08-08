from build_box import BuildBox

room_name = "1000"
build_box = BuildBox(room_name)

build_box.set_command('axis')
build_box.set_box_size(1)
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

build_box.set_light(1, 1, 0, r=1, g=0, b=0, alpha=1, intensity=20000, interval=1)
build_box.set_light(0, 1, 1, r=0, g=1, b=0, alpha=1, intensity=20000, interval=1.5)

build_box.send_data()
