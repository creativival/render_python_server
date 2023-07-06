import asyncio
import websockets
import datetime

now = datetime.datetime.now()

room_name = "1000"
jsonString = f"""
{{
"boxes": [
[0,0,0,1,0,0],
[0,1,0,0,1,0],
[0,2,0,0,0,1],
[0,3,0,1,0,1],
[0,4,0,0,1,1],
[0,5,0,1,1,0],
[0,6,0,1,1,1]
],
"data": "{now}"
}}
"""
async def sender(room_name):
    async with websockets.connect('wss://render-nodejs-server.onrender.com') as websocket:
        # First, join the room
        await websocket.send(room_name)
        print(f"Joined room: {room_name}")
        # Then, continuously send messages
        # while True:
        #     message = input("Enter your message: ")
        #     await websocket.send(message)
        await websocket.send(jsonString)

asyncio.get_event_loop().run_until_complete(sender(room_name))
