import asyncio
from . import *
from userbot.cmdhelp import CmdHelp
@bot.on(admin_cmd(pattern="chidori"))
async def naruto(ult):
	await ult.edit("Hello")
	await asyncio.sleep(1)
	await ult.edit("Im Kakashi You May Know Me As Copy Ninja ")
	await asyncio.sleep(3)
	await ult.edit("You Are Gonna Pay For What You Did To My Comrades")
	await asyncio.sleep(2)
	await ult.edit("( ◗_ ╂ ) ☞✹)Chidori ")
	await asyncio.sleep(1)
	await ult.edit("You:(✖﹏✖)")
CmdHelp("chidori").add_command(
	'chidori', None, 'Use and See'
).add()