import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user

from helper.progress import humanbytes

@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ ʙᴏᴛ ☞ <a href='https://t.me/Prv_35Bot'>𝙷𝚘𝚗𝚎𝚢 𝚁𝚘𝚜𝚎 💞</a>\nCreater :- <a href='https://t.me/Owner_PM_Bot'>👑Developer👑</a>\nLanguage :- Python3\nLibrary :- Pyrogram 2.0\nServer :- KOYEB\nTotal Renamed File :- {total_rename}\nTotal Size Renamed :- {humanbytes(int(total_size))} \n\n Thank you **<a href='https://t.me/Owner_PM_Bot'>ρ𝘳ꪖꪀꪖꪜ🧞‍♂️</a>** for your hard work \n\n❤️ we love you <a href='https://t.me/mRiderDM'>**LazyDeveloper**</a> ❤️",quote=True)
