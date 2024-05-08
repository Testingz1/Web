from websocket import create_connection

ws = create_connection("wss://territorial.io/s52/")
print("Sending")
ws.send("yes")
print("Sent")
print("Receiving...")
result =  ws.recv()
print("Received '%s'" % result)
ws.close()