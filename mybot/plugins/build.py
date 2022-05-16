import os
from mybot.utils import paste
from .. import Turtle
from telethon import events

@Turtle.on(events.NewMessage(incoming=True, pattern="/build"))
async def build(event):
    merainput = event.raw_text
    all = merainput.split("/build")[1].split(" ")
    valueone = all[1]
    valuetwo = all[2]
    m = await event.reply("```Launching Env Command...```")
    os.system(f"echo bash envsetup.sh > ../elytra/build/pasteenv.sh")
    i = open("../elytra/build/pasteenv.sh", "r")
    envlink = await paste(i.read())
    final_envlink = f"Output For Environment is Pasted [Here ]({envlink})"
    await m.edit(final_envlink)
    n = await event.reply("```Saving Lunch params...```")
    os.system(f"echo lunch elytra_{valueone}-{valuetwo} > ../elytra/build/pastelunch.sh")
    i = open("../elytra/build/pastelunch.sh", "r")
    lunchlink = await paste(i.read())
    final_lunchlink = f"Output For Lunch Command Is Pasted [Here]({lunchlink})"
    await n.edit(final_lunchlink)
    o = await event.reply("```Launching Brunch Command```")
    os.system(f"echo brunch elytra_{valueone}-{valuetwo} > ../elytra/build/pastebrunch.sh")
    i = open("../elytra/build/pastebrunch.sh", "r")
    brunchlink = await paste(i.read())
    final_brunchlink = f"Output For brunch Command Is Pasted [Here]({brunchlink})"
    await o.edit(final_brunchlink)
