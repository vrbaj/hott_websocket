import asyncio
import websockets
import websocket
import json

from websocket import create_connection

json_text = """
{"method":"fetch_all","params":{"path":"measval/adcBinVal32"}}
"""


json_to_send = json.loads(json_text)
ws = create_connection("ws://10.0.0.46:8081")
ws.send(json.dumps(json_to_send))
#while True:

result = ws.recv()
print("result:" + result)
ws.close()