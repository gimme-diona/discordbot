import discord
from discord.ext import commands
from cog_extension import Cog_Extension
import os
import random as rd

class wrong(BaseException):pass

anya=["https://c.tenor.com/bgiy5JigmaIAAAAd/anya-spy-x-family-anya.gif",
      "https://tenor.com/bRNlJ.gif",
      "https://tenor.com/bTVAE.gif","https://tenor.com/bTVoa.gif",
      "https://tenor.com/bTVkx.gif",
      "https://tenor.com/bS7XW.gif",
      "https://c.tenor.com/hd8ist3bcakAAAAd/spy-family-anya-anya-blame.gif",
      "https://c.tenor.com/otEuWXaV8JcAAAAS/spy-x-family-spy-family.gif"]
nyanpasu=["https://tenor.com/bmis5.gif",
"https://tenor.com/6s6m.gif",
"https://tenor.com/xr03.gif",
"https://tenor.com/bOUuM.gif",
"https://tenor.com/bCHcC.gif",
"https://i.giphy.com/media/W226lD4k0WFzTCgays/giphy.webp",
"https://c.tenor.com/Q9dlDoRZ9mYAAAAC/anime-renge.gif",
"https://c.tenor.com/6XcsVuluIsoAAAAC/renge-miyauchi-cute.gif",
"https://c.tenor.com/cCGBRRpZxqYAAAAC/anime-cute.gif",
"https://c.tenor.com/EYdQJlmPn9oAAAAC/renge-renge-miyauchi.gif",
"https://c.tenor.com/SIM7jWrQ8nAAAAAS/play-danse.gif",
"https://c.tenor.com/cz1ps28-53QAAAAS/horrified-shock.gif",
"https://c.tenor.com/niwymZnouL4AAAAC/renge-rage.gif",
"https://c.tenor.com/PW2agUueuUwAAAAC/renge.gif",
"https://c.tenor.com/WBwohKIJBggAAAAC/nonnonbiyori-renchon.gif",
"https://c.tenor.com/vBTcA_EnDKQAAAAd/anime-renge.gif",
"https://tenor.com/view/nyanpasu-gif-21749467"
]

class other(Cog_Extension):
  @commands.command()
  async def cringe(self,ctx):
    await ctx.message.delete()
    global nyanpasu
    for i in range(rd.randint(10,500)):
      rd.shuffle(nyanpasu)
    await ctx.send (nyanpasu[0])
    for i in range(rd.randint(10,500)):
      rd.shuffle(nyanpasu)
  @commands.command()
  async def kill(self,ctx,member="@s"):
      await ctx.channel.purge(limit=1)
      if member[1]=="@" or member=="@s":
        if member!="@s":user=member
        else:user="@"+ctx.author.name
        if rd.randint(0,1)==0:
          await ctx.send(f"{user}```fix\n掉到了世界外\n```")
        else:
          await ctx.send(f"{user}```fix\n被魔法殺死了\n```")
  @commands.command()
  async def anya(self,ctx):
    await ctx.message.delete()
    global anya
    for i in range(rd.randint(10,500)):
      rd.shuffle(anya)
    await ctx.send(anya[0])
    for i in range(rd.randint(10,500)):
      rd.shuffle(anya)
    
def setup(bot):
  bot.add_cog(other(bot))