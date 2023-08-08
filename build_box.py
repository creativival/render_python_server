from math import floor
import asyncio
import websockets
import datetime
import re


class BuildBox:
  def __init__(self, room_name):
    self.room_name = room_name
    self.global_animation = [0, 0, 0, 0, 0, 0, 1, 0]
    self.node = [0, 0, 0, 0, 0, 0]
    self.animation = [0, 0, 0, 0, 0, 0, 1, 0]
    self.boxes = []
    self.sentence = []
    self.lights = []
    self.commands = []
    self.size = 1
    self.shape = 'box'
    self.build_interval = 0.01

  def animate_global(self, x, y, z, pitch=0, yaw=0, roll=0, scale=1, interval=10):
    self.clear_data()
    x, y, z = map(floor, [x, y, z])
    self.global_animation = [x, y, z, pitch, yaw, roll, scale, interval]

  def set_node(self, x, y, z, pitch=0, yaw=0, roll=0):
    x, y, z = map(floor, [x, y, z])
    self.node = [x, y, z, pitch, yaw, roll]

  def animate_node(self, x, y, z, pitch=0, yaw=0, roll=0, scale=1, interval=10):
    x, y, z = map(floor, [x, y, z])
    self.animation = [x, y, z, pitch, yaw, roll, scale, interval]

  def create_box(self, x, y, z, r=1, g=1, b=1, alpha=1):
    x, y, z = map(floor, [x, y, z])
    # 重ねておくことを防止
    self.remove_box(x, y, z)
    self.boxes.append([x, y, z, r, g, b, alpha])

  def remove_box(self, x, y, z):
    x, y, z = [floor(val) for val in [x, y, z]]
    for box in self.boxes:
      if box[0] == x and box[1] == y and box[2] == z:
        self.boxes.remove(box)

  def set_box_size(self, box_size):
    self.size = box_size

  def set_build_interval(self, interval):
    self.build_interval = interval

  def clear_data(self):
    self.global_animation = [0, 0, 0, 0, 0, 0, 1, 0]
    self.node = [0, 0, 0, 0, 0, 0]
    self.animation = [0, 0, 0, 0, 0, 0, 1, 0]
    self.boxes = []
    self.sentence = []
    self.lights = []
    self.commands = []
    self.size = 1
    self.shape = 'box'
    self.build_interval = 0.01

  def write_sentence(self, sentence, x, y, z, r=1, g=1, b=1, alpha=1):
    x, y, z = map(str, map(floor, [x, y, z]))
    r, g, b, alpha = map(str, [r, g, b, alpha])
    self.sentence = [sentence, x, y, z, r, g, b, alpha]

  def set_light(self, x, y, z, r=1, g=1, b=1, alpha=1, intensity=1000, interval=1):
    x, y, z = map(floor, [x, y, z])
    self.lights.append([x, y, z, r, g, b, alpha, intensity, interval])

  def set_command(self, command):
    self.commands.append(command)

  def draw_line(self, x1, y1, z1, x2, y2, z2, r=1, g=1, b=1, alpha=1):
    x1, y1, z1 = map(floor, [x1, y1, z1])
    x2, y2, z2 = map(floor, [x2, y2, z2])
    diff_x = x2 - x1
    diff_y = y2 - y1
    diff_z = z2 - z1
    max_length = max(abs(diff_x), abs(diff_y), abs(diff_z))
    # print(x2, y2, z2)

    if diff_x == 0 and diff_y == 0 and diff_z == 0:
      return False

    if abs(diff_x) == max_length:
      if x2 > x1:
        for x in range(x1, x2 + 1):
          y = y1 + (x - x1) * diff_y / diff_x
          z = z1 + (x - x1) * diff_z / diff_x
          self.create_box(x, y, z, r, g, b, alpha)
      else:
        for x in range(x1, x2 - 1, -1):
          y = y1 + (x - x1) * diff_y / diff_x
          z = z1 + (x - x1) * diff_z / diff_x
          self.create_box(x, y, z, r, g, b, alpha)
    elif abs(diff_y) == max_length:
      if y2 > y1:
        for y in range(y1, y2 + 1):
          x = x1 + (y - y1) * diff_x / diff_y
          z = z1 + (y - y1) * diff_z / diff_y
          self.create_box(x, y, z, r, g, b, alpha)
      else:
        for y in range(y1, y2 - 1, -1):
          x = x1 + (y - y1) * diff_x / diff_y
          z = z1 + (y - y1) * diff_z / diff_y
          self.create_box(x, y, z, r, g, b, alpha)
    elif abs(diff_z) == max_length:
      if z2 > z1:
        for z in range(z1, z2 + 1):
          x = x1 + (z - z1) * diff_x / diff_z
          y = y1 + (z - z1) * diff_y / diff_z
          self.create_box(x, y, z, r, g, b, alpha)
      else:
        for z in range(z1, z2 - 1, -1):
          x = x1 + (z - z1) * diff_x / diff_z
          y = y1 + (z - z1) * diff_y / diff_z
          self.create_box(x, y, z, r, g, b, alpha)

  def change_shape(self, shape):
    self.shape = shape

  def send_data(self):
    now = datetime.datetime.now()
    data_to_send = f"""
      {{
      "globalAnimation": {self.global_animation},
      "node": {self.node},
      "animation": {self.animation},
      "boxes": {self.boxes},
      "sentence": {self.sentence},
      "lights": {self.lights},
      "commands": {self.commands},
      "size": {self.size},
      "shape": "{self.shape}",
      "interval": {self.build_interval},
      "date": "{now}"
      }}
      """.replace("'", '"')

    async def sender(room_name):
      async with websockets.connect('wss://websocket.voxelamming.com') as websocket:
        await websocket.send(room_name)
        print(f"Joined room: {room_name}")
        await websocket.send(data_to_send)
        # print(data_to_send)
        print(re.sub(r'\n      ', ' ', data_to_send.replace('"', '\\"')))
        print("Sent data to server")
        # self.clear_data()

    asyncio.get_event_loop().run_until_complete(sender(self.room_name))
