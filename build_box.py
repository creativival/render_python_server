from math import floor
import asyncio
import websockets
import datetime


class BuildBox:
  def __init__(self):
    self.boxes = []
    self.size = 1
    self.build_interval = 0.01

  def create_box(self, x, y, z, r, g, b):
    x, y, z = map(floor, [x, y, z])
    self.boxes.append([x, y, z, r, g, b])

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

  def clear_boxes(self):
    self.boxes = []
    self.size = 1
    self.build_interval = 0.01

  def send_data(self, room_name):
    now = datetime.datetime.now()
    data_to_send = f"""
      {{
      "boxes": {self.boxes},
      "size": {self.size},
      "interval": {self.build_interval},
      "date": "{now}"
      }}
      """

    async def sender(room_name):
      async with websockets.connect('wss://render-nodejs-server.onrender.com') as websocket:
        await websocket.send(room_name)
        print(f"Joined room: {room_name}")
        await websocket.send(data_to_send)
        print("Sent data to server")
        self.clear_boxes()

    asyncio.get_event_loop().run_until_complete(sender(room_name))
