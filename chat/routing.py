from channels.routing import route
from app.consumers import  ws_message, ws_disconnect, ws_connect, ws_add
channel_routing = [
    # Called when WebSockets connect
    route('websocket.connect', ws_add),
    # Called when WebSockets get sent a data frame
    route("websocket.receive", ws_message),


]
