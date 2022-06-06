import discord
from discord.ext import commands
import json
from cog_extension import Cog_Extension

class ping(Cog_Extension):
  @commands.command()
  async def ping(self,ctx):
    await ctx.channel.send("ping! LOLI!\n",(str(round(self.bot.latency*1000))+"ms"))
                           
def setup(bot):
  bot.add_cog(ping(bot))