from math import floor
import asyncio
import websockets
import datetime


class BuildBox:
  def __init__(self, room_name):
    self.room_name = room_name
    self.node = [0, 0, 0, 0, 0, 0]
    self.animation = [0, 0, 0, 0, 0, 0, 1, 0]
    self.boxes = []
    self.sentences = []
    self.size = 1
    self.build_interval = 0.01

  def set_node(self, x, y, z, pitch=0, yaw=0, roll=0):
    x, y, z = map(floor, [x, y, z])
    self.node = [x, y, z, pitch, yaw, roll]

  def animation_node(self, x, y, z, pitch=0, yaw=0, roll=0, scale=1, interval=10):
    x, y, z = map(floor, [x, y, z])
    self.animation = [x, y, z, pitch, yaw, roll, scale, interval]

  def create_box(self, x, y, z, r=1, g=1, b=1, alpha=1):
    x, y, z = map(floor, [x, y, z])
    self.boxes.append([x, y, z, r, g, b, alpha])


  def remove_box(self, x, y, z):
    x, y, z = [floor(val) for val in [x, y, z]]
    for box in self.boxes:
      if box[0] == x and box[1] == y and box[2] == z:
        self.boxes.remove(box)
        return True


  def set_box_size(self, box_size):
    self.size = box_size


  def set_build_interval(self, interval):
    self.build_interval = interval


  def clear_data(self):
    self.node = [0, 0, 0, 0, 0, 0]
    self.animatiion = [0, 0, 0, 0, 0, 0, 1, 0]
    self.boxes = []
    self.sentences = []
    self.size = 1
    self.build_interval = 0.01

  def write_sentence(self, sentence, x, y, z, r=1, g=1, b=1, alpha=1):
    x, y, z = map(str, map(floor, [x, y, z]))
    r, g, b = map(str, [r, g, b])
    self.sentences.append([sentence, x, y, z, r, g, b, alpha])

  def send_data(self):
    now = datetime.datetime.now()
    data_to_send = f"""
      {{
      "node": {self.node},
      "animation": {self.animation},
      "boxes": {self.boxes},
      "sentences": {self.sentences},
      "size": {self.size},
      "interval": {self.build_interval},
      "date": "{now}"
      }}
      """.replace("'", '"')

    async def sender(room_name):
      async with websockets.connect('wss://render-nodejs-server.onrender.com') as websocket:
        await websocket.send(room_name)
        print(f"Joined room: {room_name}")
        await websocket.send(data_to_send)
        print(data_to_send)
        print("Sent data to server")
        # self.clear_data()

    asyncio.get_event_loop().run_until_complete(sender(self.room_name))
