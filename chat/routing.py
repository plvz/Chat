from channels.routing import route
from app.consumers import ws_message
channel_routing = [
    route("http.request", "app.consumers.http_consumer"),
    route("websocket.receive", ws_message),
]
