import os
from mybot.utils import paste
from .. import Turtle
from telethon import events


@Turtle.on(events.NewMessage(incoming=True, pattern="/test"))
async def test(event):
    m = await event.reply("```Pasting ⏳ ⌛️...```")
    os.system('ls > paste.txt')
    i = open("paste.txt", "r")
    link = await paste(i.read())
    final_link = f"Output Pasted [here ]({link})"
    await m.edit(final_link)
    os.remove("paste.txt")