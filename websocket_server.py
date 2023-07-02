import asyncio
import websockets
import json

rooms = {}  # To hold the mapping between room and clients

async def server(websocket, path):
    try:
        # Register client to a room
        room_name = await websocket.recv()
        if room_name not in rooms:
            rooms[room_name] = set()  # Create room if not exists
        rooms[room_name].add(websocket)
        print(f"Client joined room: {room_name}")

        async for message in websocket:
            print(f"Received message from client: {message}")
            # Broadcast the message to all other clients in the same room
            if room_name in rooms and len(rooms[room_name]) > 1:
                await asyncio.wait([client.send(f"Message from server: {message}") for client in rooms[room_name] if client != websocket])

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Unregister client
        rooms[room_name].remove(websocket)

start_server = websockets.serve(server, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
try:
    asyncio.get_event_loop().run_forever()
except KeyboardInterrupt:
    pass
