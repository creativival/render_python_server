import asyncio
import websockets

async def receiver(room_name):
    async with websockets.connect('wss://render-nodejs-server.onrender.com') as websocket:
        # First, join the room
        await websocket.send(room_name)
        print(f"Joined room: {room_name}")
        # Then, continuously receive messages
        while True:
            try:
                response = await websocket.recv()
                print(f"Received message: {response}")
            except websockets.exceptions.ConnectionClosed:
                print("Connection was closed.")
                break

asyncio.get_event_loop().run_until_complete(receiver("1000"))
