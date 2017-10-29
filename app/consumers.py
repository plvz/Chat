from channels import Group

# Connected to websocket.receive
def ws_message(message):
    # ASGI WebSocket packet-received and send-packet message types
    content = message.content['text']
    Group("chat").send({
        "text": "%s" % content,
    })

# Connected to websocket.connect
def ws_add(message):
    # Accept the incoming connection
    message.reply_channel.send({"accept": True})
    # Add them to the chat group
    Group("chat").add(message.reply_channel)
