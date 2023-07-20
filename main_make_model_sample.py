from build_box import BuildBox
from ply_util import get_boxes_from_ply

room_name = "1000"
build_box = BuildBox(room_name)

build_box.set_box_size(0.5)
build_box.set_build_interval(0.01)

ply_file_name = 'piyo.ply'

boxes = get_boxes_from_ply(ply_file_name)

for box in boxes:
    build_box.create_box(*box)

build_box.send_data()
