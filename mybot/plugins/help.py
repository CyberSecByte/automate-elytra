from .. import Turtle
from telethon import events

@Turtle.on(events.NewMessage(incoming=True, pattern="/help"))
async def help(event):
    helptext = f"Below are the list of all the commands\n/start to check the bot status\n/help to view this :p\n/build devicename typeofbuild"
    await event.reply(helptext)
