import discord
from discord.ext import commands


class Cog_Extension(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
def setup(bot):
    bot.add_cog(Cog_Extension(bot))