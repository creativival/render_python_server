import csv
from math import floor


def get_boxes_from_text(text_file):
  box_positions = set()
  with open('text_file/' + text_file, 'r') as f:
    lines = csv.reader(f)

    for line in lines:
      if len(line) != 6:
        continue

      x = float(line[0])
      y = float(line[1])
      z = float(line[2])
      r = float(line[3]) / 255
      g = float(line[4]) / 255
      b = float(line[5]) / 255
      alpha = 1

      if z > 0:
        box_positions.add(
          (
            x,
            z,
            y,
            r,
            g,
            b,
            alpha
          )
        )

    print('before: ', len(box_positions))

    reduced_box_positions = remove_surrounded_voxels(box_positions)
    print('after: ', len(reduced_box_positions))

    return reduced_box_positions


def remove_surrounded_voxels(box_positions):
  # 各ボクセルの位置をキーとして使用し、値としてボクセル自体を含む辞書を作成
  box_dict = {(x, y, z): (r, g, b, alpha) for x, y, z, r, g, b, alpha, in box_positions}

  # 削除対象のボクセルリストを作成
  to_remove = []

  for (x, y, z) in box_dict:
    # ボクセルが他のボクセルに囲まれているかどうかを判断
    if all((nx, ny, nz) in box_dict for nx, ny, nz in
           [(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1)]):
      print('remove: ', x, y, z)
      to_remove.append((x, y, z))

  # 削除対象のボクセルを辞書から削除
  for voxel in to_remove:
    del box_dict[voxel]

  # 辞書をリストに変換して返す
  reduced_box_positions = [[x, y, z, r, g, b, alpha] for (x, y, z), (r, g, b, alpha) in box_dict.items()]

  return reduced_box_positions


if __name__ == '__main__':
  get_boxes_from_text('giza_128x128x29.txt')
