from build_box import BuildBox
from text_util import get_boxes_from_text

room_name = "1000"
build_box = BuildBox(room_name)

build_box.set_box_size(0.1)
build_box.set_build_interval(0)

text_file_name = 'giza_128x128x29.txt'
# text_file_name = 'giza_49x49x12.txt'
pyramid_color = [0.8, 0.8, 0, 1]

boxes = get_boxes_from_text(text_file_name)

for box in boxes:
  x, y, z, _, _, _, _ = box
  if y > 3:  # ボクセル数を減らすため、床面より上のボクセルのみを描画
    build_box.create_box(x, y, z, *pyramid_color)

build_box.send_data()
