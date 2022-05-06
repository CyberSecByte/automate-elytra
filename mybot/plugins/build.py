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
    f = await event.reply("```Setting up the variables...```")
    os.system(f"echo -e DEVICE={valueone}\nBUILD_TYPE={valuetwo} > inputvars.conf")
    i = open("../elytra/pasteenv.txt", "r")
    varslink = await paste(i.read())
    final_varslink = f"Output For Environment is Pasted [Here ]({varslink})"
    await m.edit(final_varslink)
    m = await event.reply("```Launching Env Command...```")
    os.system(f"bash jenkin.sh > jenkins.txt")
    i = open("jenkins.txt", "r")
    envlink = await paste(i.read())
    final_envlink = f"Build Process is [Here ]({envlink})"
    await m.edit(final_envlink)
    os.remove("jenkins.txt")
   
