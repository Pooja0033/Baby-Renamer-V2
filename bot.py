import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "")

API_ID = int(os.environ.get("API_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

STRING = os.environ.get("STRING", "BQCZjHaI5owWW9XSa-4ihcMIFq-wOsSSXtoFaTTJHX0qYKPHiIsAbgOkrtCogeGws6gfAiu1KrwYgY1Yd9WOynFWGYJJ7RliTKYnhe0mKTeREUUGbmoXtCxeqLflVZ4ALXhndmnvUJdG2DoIsxQg1_RhwkPNPRXisXBW3V0euY8YK0tWTBr4MxONqFdRaWiD8e8uMTxKHsiXo4dZ53HHLWqnkkIz_qZQl6UwJYGC4HIIk6BYOxt7XFEtYl1_wn2aWNdaj5vuiNM4oN828_lO_bvBt5Oti-FyuIWEuX8g_eR0oHQfonC1Feb6jXc7v886gRs45oxBXZ00CnZMWYzpLpDnAAAAAVVV7xkA")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
