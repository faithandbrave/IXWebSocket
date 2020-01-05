#!/usr/bin/env python

# WS server example

import asyncio
import websockets


async def echo(websocket, path):
    msg = await websocket.recv()
    print(f'Received {len(msg)} bytes')
    await websocket.send(msg)


print('Serving on localhost:8766')
start_server = websockets.serve(echo, 'localhost', 8766, max_size=2 ** 25)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
