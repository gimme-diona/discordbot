import discord
from discord.ext import commands
import json
import os
from webserver import keep_alive,run
from threading import Thread

TOKEN = os.environ['token']
'''
with open("settings.json",mode="r",encoding="utf8") as jfile:
    jdata=json.load(jfile)
'''
bot = commands.Bot(command_prefix="/")

@bot.event
async def on_ready():
    print(">>>LogIn as :",bot)

for filename in os.listdir("./extensions"):
  if filename.endswith(".py"):
    bot.load_extension(f"extensions.{filename[:-3]}")
  
t = Thread(target=run)
@bot.command()
async def shutdown(ctx,confirm):
  #try: 
    if confirm.lower()=="y":
      await ctx.channel.send("即將停止機器人. .. ...")
      global t
      t.join()
      exit()
    else:
      if not isinstance(confirm,str):
        await ctx.channel.send("請輸入(y/n)")
  #except:await ctx.channel.send("關機失敗")

      
if __name__=="__main__":
  keep_alive(t)
  bot.run(TOKEN)