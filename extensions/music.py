import discord
from discord.ext import commands
from cog_extension import Cog_Extension
import os
import nacl
import ffmpeg

class music(Cog_Extension):
  def __init__(self,bot):
    super().__init__(bot)
    self.vclients={}
  def music(self):
      os.chdir("./extensions/musics")
      with open("TEST.mp3") as music:
        return music
  @commands.command()
  async def join(self,ctx):
    guild =ctx.guild
    vc=ctx.author.voice.channel
    if vc!=None:
      try:
        await ctx.send("Count me in!")
        await vc.connect()
        self.vclients[guild]=self.bot.voice_clients[-1]
      except discord.errors.ClientException:
        await ctx.send("""Already IN A VOICE CHANNEL!!!
I DO NOT HAVE TWINS!
AND WE HAVE A COMMAND CALLED "MOVE" !!!
                     """)
    else:await ctx.send("YOU ARE NOT IN A CHANNEL, AND YOU WANT ME TO IN?")
#---------------------------------------------------            
  @commands.command()
  async def play(self,ctx):
    guild =ctx.guild
    vc=ctx.author.voice.channel
    if vc!=None:
      try:
        await vc.connect()
        self.vclients[guild]=self.bot.voice_clients[-1]
        vclient=self.vclients[guild]
        vclient.play(discord.FFmpegPCMAudio(self.music()))
      except discord.errors.ClientException:
        vclient=self.vclients[guild]
        vclient.play(discord.FFmpegPCMAudio(os.path.abspath("./musics/test.mp3")))
    else:await ctx.send("YOU ARE NOT IN A CHANNEL, AND YOU WANT ME TO PLAY WHAT?")
        
#---------------------------------------------------
  @commands.command()
  async def leave(self,ctx):
    guild =ctx.guild
    if guild in self.vclients:
      vc=self.vclients[guild]
      await vc.disconnect()
      await ctx.send("I QUIT!")
    else:
      await ctx.send("I AM NOT IN A CHANNEL, DUDE")
#---------------------------------------------------
  @commands.command()
  async def move(self,ctx):
    guild =ctx.guild
    
            
    

def setup(bot):
  bot.add_cog(music(bot))
