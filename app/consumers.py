from django.http import HttpResponse, HttpResponseRedirect
from channels.handler import AsgiHandler
from channels import Group
from django.shortcuts import render, redirect
from pprint import pprint

def ws_receive(message):
    # All WebSocket frames have either a text or binary payload; we decode the
    # text part here assuming it's JSON.
    # You could easily build up a basic framework that did this encoding/decoding
    # for you as well as handling common errors.
    payload = json.loads(message['text'])
    payload['reply_channel'] = message.content['reply_channel']
    Channel("chat.receive").send(payload)

# Connected to websocket.receive
def ws_message(message):
    # ASGI WebSocket packet-received and send-packet message types
    pprint(message)
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

def ws_connect(message):
    Group('users').add(message.reply_channel)

# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)
