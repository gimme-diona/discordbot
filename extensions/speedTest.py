import discord
from discord.ext import commands
import os
import speedtest   # 导入speedtest_cli
import threading
from cog_extension import Cog_Extension

class Speed():
  def __init__(self,per:bool=False):
      self.per=per
      print("准备测试ing...")
 
      # 创建实例对象
      self.test = speedtest.Speedtest()
      # 获取可用于测试的服务器列表
      self.test.get_servers()
      # 筛选出最佳服务器
      best = self.test.get_best_server()
       
      print("正在测试ing...")
      self.dl=[]
      self.ul=[]

  def per_speed(self):#slow
    if self.per:
      for i in range(3):
          download_speed = int(self.test.download() / 1024 / 1024)
          upload_speed = int(self.test.upload() / 1024 / 1024)
          self.dl.append(download_speed)
          self.ul.append(upload_speed)
    
      download_speed=0
      upload_speed=0
      for i in range(len(dl)):
        download_speed+=self.dl[i]
        upload_speed+=self.ul[i]
    
    
    # 输出结果
    return ("下载速度：" + str(download_speed/len(self.dl)) + " Mbits","上传速度：" + str(upload_speed/len(self.dl)) + " Mbits")
  
  
  def normal_speed(self):
    if not self.per:
      download_speed=int(self.test.download() / 1024 / 1024)
      upload_speed=int(self.test.upload() / 1024 / 1024)
      return ("下载速度：" + str(download_speed) + " Mbits","上传速度：" + str(upload_speed) + " Mbits")

class speedTest(Cog_Extension):
  @commands.command()
  async def speedtest(self,ctx,平均模式=0):
    if not isinstance(平均模式,int):
      ctx.channel.send("請輸入(0[off][default]/1[on]")
    if not bool(平均模式):
      speed=Speed().normal_speed()
    else:
      speed=Speed(True).normal_speed()
    if speed!=None:
      ctx.channel.sned(f"下載速度{speed[0]}Mbps\n上傳速度{speed[1]}Mbps")
    else:ctx.channel.send("系統錯誤[Not your problem.]")

def setup(bot):
  bot.add_cog(speedTest(bot))