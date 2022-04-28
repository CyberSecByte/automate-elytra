import requests
import os
from .. import Turtle
from PIL import Image
from telethon import events

myimage = "https://telegra.ph/file/0a943172f34b271534e44.jpg"
startmessage = "Hey There ! I Am Alive"

@Turtle.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    r = requests.get(myimage, allow_redirects=True)
    open('alive.jpg', 'wb').write(r.content)

    await Turtle.send_file(event.chat_id, 'alive.jpg', caption=startmessage, link_preview=False)
