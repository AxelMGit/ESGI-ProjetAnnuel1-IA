import asyncio
import json
import websockets
from typing import Dict, Any

async def handle_client(websocket, path):
    while True:
        data = await websocket.recv()
        request = json.loads(data)
        if request["event"] == "send":
            response = await rasa_on_new_message(request["text"])
            await websocket.send(json.dumps({"event": "receive", "text": response}))

async def rasa_on_new_message(text: str) -> str:
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = f"q={text}"
    async with aiohttp.ClientSession() as session:
        async with session.post("http://localhost:5055/webhooks/rest/webhook", data=data, headers=headers) as resp:
            result = await resp.text()
            return json.loads(result)[0]["text"]

start_server = websockets.serve(handle_client, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()