import discord
from discord.ext import commands
from cog_extension import Cog_Extension
import os


class command_load(Cog_Extension):
    def __init__(self,bot):
      super().__init__(bot)
      self.banlist=["command_load"]
      self.administrator=[374555292601679872]
    @commands.command()
    async def load(self,ctx,extension):
      if ctx.author.id in self.administrator:
        self.bot.load_extension("extensions.%s"%(extension))
        await ctx.send("Loaded %s"%(extension))
      else:
        await ctx.send("NOT AN ADMIN OF ME")
   #---------------------------------------------------------------------------------    
    @commands.command()
    async def unload(self,ctx,extension):
      if ctx.author.id in self.administrator:
        self.bot.unload_extension("extensions.%s"%(extension))
        await ctx.send("Un-Loaded %s"%(extension))
      else:
        await ctx.send("NOT AN ADMIN OF ME")
   #---------------------------------------------------------------------------------    
    @commands.command()
    async def reload(self,ctx,extension):
      if ctx.author.id in self.administrator:
        self.bot.reload_extension("extensions.%s"%(extension))
        await ctx.send("Re-Loaded %s"%(extension))
      else:
        await ctx.send("NOT AN ADMIN OF ME")
   #---------------------------------------------------------------------------------    
    @commands.command()
    async def reloadall(self,ctx):
      if ctx.author.id in self.administrator:
        for extension in os.listdir("./extensions"):
          if extension.endswith(".py"):
            extension=extension[:-3]
            if not extension in self.banlist:
                self.bot.reload_extension("extensions.%s"%(extension))
        await ctx.send("Re-loaded all")
      else:
        await ctx.send("NOT AN ADMIN OF ME")
        
   #---------------------------------------------------------------------------------    
    @commands.command()
    async def unloadall(self,ctx):
      if ctx.author.id in self.administrator:
        for extension in os.listdir("./extensions"):
          if extension.endswith(".py"):
            extension=extension[:-3]
            if not extension in self.banlist:
                self.bot.unload_extension("extensions.%s"%(extension))
        await ctx.send("Un-loaded all")
      else:
        await ctx.send("NOT AN ADMIN OF ME")
        
   #--------------------------------------------------------------------------------- 
    @commands.command()
    async def loadall(self,ctx):
      if ctx.author.id in self.administrator:
        for extension in os.listdir("./extensions"): 
          if extension.endswith(".py"):
            extension=extension[:-3]
            if not extension in self.banlist:
                self.bot.load_extension("extensions.%s"%(extension))
        await ctx.send("loaded all")
      else:
        await ctx.send("NOT AN ADMIN OF ME")

  
def setup(bot):
    bot.add_cog(command_load(bot))