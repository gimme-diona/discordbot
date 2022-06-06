import discord
from discord.ext import commands
import os
import speedtest   # 导入speedtest_cli
import threading
from cog_extension import Cog_Extension

class speedTest(Cog_Extension):
    @commands.command()
    async def speedtest(self,ctx):
        await ctx.send("測試正在準備. .. ...")
        # 创建实例对象
        test = speedtest.Speedtest()
        # 获取可用于测试的服务器列表
        test.get_servers()
        # 筛选出最佳服务器
        test.get_best_server()
        await ctx.send("準備完成..\n正在開始測試. .. ...")
        download_speed=int(test.download() / 1024 / 1024)
        upload_speed=int(test.upload() / 1024 / 1024)
        await ctx.send(f"下载速度：{str(download_speed)} Mbits"，上传速度： {str(upload_speed)} Mbits")

def setup(bot):
  bot.add_cog(speedTest(bot))
