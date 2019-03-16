from channels import route
from channels import include
from .consumers import (
    chat_connect, chat_receive, chat_disconnect, loadhistory_connect,
    loadhistory_receive, loadhistory_disconnect
    )

chat_routing = [
    route('websocket.connect', chat_connect),
    route('websocket.receive', chat_receive),
    route('websocket.disconnect', chat_disconnect),
    ]

loadhistory_routing = [
    route('websocket.connect', loadhistory_connect),
    route('websocket.receive', loadhistory_receive),
    route('websocket.disconnect', loadhistory_disconnect),
    ]

channel_routing = [
    include(chat_routing, path=r'^/ws/$'),
    include(loadhistory_routing, path=r'^/loadhistory/$'),
    ]
