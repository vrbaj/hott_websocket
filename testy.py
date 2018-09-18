import asyncio
import websockets
import websocket
import json

from websocket import create_connection

json_text = """
{"method":"fetch_all","params":{"path":"measval/adcBinVal32"}}
"""


json_to_send = json.loads(json_text)
ws = create_connection("ws://10.0.0.44:8081")
while True:

    ws.send(json.dumps(json_to_send))

    result = ws.recv()
    print("result:" + result)
ws.close()

# async def hello():
#     async with websockets.connect(
#             'ws://clipx:8081') as websocket:
#         # name = input("What's your name? ")
#         name = json.dumps({"method":"fetch_all"})
#         print("presend")
#         websockets.send(name)
#         print("send")
#         websockets.recv()
#         print("receive:")
#         print(f"< {greeting}")
#
# asyncio.get_event_loop().run_until_complete(hello())