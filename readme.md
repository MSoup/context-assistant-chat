# Context Assistant Chat

##

FastAPI
A web framework for building APIs

Uvicorn
Uvicorn is an ASGI web server implementation

websockets
For building websocket servers and clients

## Using websockets

```
Here’s an echo server with the asyncio API:

#!/usr/bin/env python

import asyncio
from websockets.server import serve

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
Here’s how a client sends and receives messages with the threading API:

#!/usr/bin/env python

import asyncio
from websockets.sync.client import connect

def hello():
    with connect("ws://localhost:8765") as websocket:
        websocket.send("Hello world!")
        message = websocket.recv()
        print(f"Received: {message}")

hello()
Don’t worry about the opening and closing handshakes, pings and pongs, or any other behavior described in the WebSocket specification. websockets takes care of this under the hood so you can focus on your application!

Also, websockets provides an interactive client:

python -m websockets ws://localhost:8765/
Connected to ws://localhost:8765/.
> Hello world!
< Hello world!
Connection closed: 1000 (OK).
```

UUIDs just lets us handle different identifiers
