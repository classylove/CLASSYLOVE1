import asyncio
from . import *
@bot.on(admin_cmd(pattern="happybirthday"))
async def _(event):
	await asyncio.sleep(1)
	await event.edit("""
  ^_^)
.................^v^
⋱ ⋮ ⋰
⋯ ◯ ⋯¨. ︵ ..............................................^v^
¨︵¸︵( ░░ )︵.︵.︵..............^v^
... (´░░░░░░ ') ░░░' )
´︶´¯︶´︶´︶´︶.....^v^..........^v^
....^v^....▄▀▀──▄▀▀▄─▄▀▀▄─█▀▄....^v^....
....^v^....█─▀█─█──█─█──█─█─█....^v^....
....^v^....─▀▀───▀▀───▀▀──▀▀─....^v^....
....^v^........^v^........^v^........^v^........^v^....
█▄─▄█─▄▀▀▄─█▀▄─█▄─█─█─█▄─█─▄▀▀─
█─▀─█─█──█─██▀─█─▀█─█─█─▀█─█─▀█
▀───▀──▀▀──▀─▀─▀──▀─▀─▀──▀──▀▀─ 
""")
CmdHelp("goodmorning").add_command(
	'gm', None, 'Use and See'
).add()
