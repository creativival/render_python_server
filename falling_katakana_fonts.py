import time
from random import shuffle, randint
from math import atan2, degrees
import csv
from build_box import BuildBox

font_file = 'misaki_mincho.bdf.csv'
font_size = 8
first_katakana_id = 9505
last_katakana_id = 9590


def get_katakana_font_dict(file):
    font_dict = {}
    with open(f'font_data/{file}', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            font_id = int(row[0])
            if first_katakana_id <= font_id <= last_katakana_id:
                # print(font_id)
                font_dict[font_id] = row[2:]

        return font_dict


katakana_font_dict = get_katakana_font_dict(font_file)
katakana_list = list(range(first_katakana_id, last_katakana_id + 1))
shuffle(katakana_list)

room_name = "2536"
build_box = BuildBox(room_name)

build_box.set_box_size(0.3)
build_box.set_build_interval(0)

for i in range(len(katakana_list)):
    character = katakana_list[i]
    # print(character)
    bitmap_data = katakana_font_dict[character]
    # print(bitmap_data)
    bitmap_data = ['{0:0>8}'.format(bin(int(bits, 16))[2:]) for bits in bitmap_data]

    for j in range(font_size):
        for k in range(font_size):
            if bitmap_data[j][k] == '1':
                x = k
                y = -j - font_size * i
                z = 0
                # print(x, y, z)
                build_box.create_box(x, y, z, r=0, g=1, b=0, alpha=0.8)

for _ in range(3):
    x = randint(-50, 50)
    y = randint(0, 100)
    z = randint(-50, 0)
    yaw = degrees(atan2(x, 100 - z))
    build_box.translate(x, font_size * len(katakana_list) + y, z, pitch=0, yaw=yaw, roll=0)
    build_box.send_data()
    time.sleep(1)

build_box.animate_global(0, -1000, 0, 0, 0, 0, 1, 100)
build_box.send_data()


