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
    os.system(f"cd ../elytra && bash build/envsetup.sh > pasteenv.txt")
    i = open("../elytra/pasteenv.txt", "r")
    envlink = await paste(i.read())
    final_envlink = f"Output For Environment is Pasted [Here ]({envlink})"
    await m.edit(final_envlink)
    os.remove("../elytra/pasteenv.txt")
    n = await event.reply("```Launching Lunch command...```")
    os.system(f"bash launchlunch.sh {valueone} {valuetwo} > pastelunch.txt")
    i = open("pastelunch.txt", "r")
    lunchlink = await paste(i.read())
    final_lunchlink = f"Output For Lunch Command Is Pasted [Here]({lunchlink})"
    await n.edit(final_lunchlink)
    os.remove("pastelunch.txt")
    o = await event.reply("```Launching Brunch Command```")
    os.system(f"bash launchbrunch.sh {valueone} {valuetwo} > pastebrunch.txt")
    i = open("pastebrunch.txt", "r")
    brunchlink = await paste(i.read())
    final_brunchlink = f"Output For brunch Command Is Pasted [Here]({brunchlink})"
    await o.edit(final_brunchlink)
    os.remove("pastebrunch.txt")