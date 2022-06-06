import discord
from discord.ext import commands
import json
from cog_extension import Cog_Extension

class Purge(Cog_Extension):
    @commands.command()
    async def purge(self,ctx,欲刪訊息數):
        limits=int(欲刪訊息數)
        await ctx.channel.send("即將開始掃地. .. ...")
        await ctx.channel.purge(limit=limits+2)
        
def setup(bot):
    bot.add_cog(Purge(bot))
