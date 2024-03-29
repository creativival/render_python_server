import csv
from build_box import BuildBox

# ルームネームを設定
room_name = "1000"
build_box = BuildBox(room_name)
build_box.set_box_size(0.1)
build_box.set_build_interval(0.01)
build_box.set_command('liteRender')
build_box.set_command('float')
build_box.set_frame_fps(2)
build_box.set_frame_repeats(10)

zoom_rate = 10

for i in range(1, 10):
    # フレームイン
    build_box.frame_in()

    build_box.translate(0, 10, 0)

    with open(f'obj_model/whale_animation0{i}.csv') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            position = map(lambda x: x * zoom_rate, map(float, row))
            build_box.create_box(*position, r=1, g=0, b=1, alpha=1)

    # フレームアウト
    build_box.frame_out()

# データを送信
build_box.send_data()
build_box.clear_data()
