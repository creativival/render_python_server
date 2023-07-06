import asyncio
import websockets

rooms = {}

async def handle_connection(websocket, path):
    room_name = None

    async for message in websocket:
        if not room_name:
            room_name = message
            if room_name not in rooms:
                rooms[room_name] = set()
            rooms[room_name].add(websocket)
            print(f"Client joined room: {room_name}")
        else:
            print(f"Received message from client: {message}")
            # Broadcast the message to all other clients in the same room
            if room_name in rooms:
                for client in rooms[room_name]:
                    if client != websocket and client.open:
                        await client.send(message)

    if room_name:
        rooms[room_name].discard(websocket)

start_server = websockets.serve(handle_connection, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
