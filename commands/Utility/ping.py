import nextcord
from nextcord.ext import commands
from config import green
import time
from datetime import datetime, timedelta
import psutil

class Ping(commands.Cog):
    def __init__(self, client): 
         self.client = client
    
    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def ping(self, ctx):
        await ctx.send("Retreaving the information..........⏳")
        info = f"""
__Ping:__  `{round(self.client.latency * 1000)}ms 📈`
__Users Managed:__ `{len(list(self.client.get_all_members()))} 🐵`
__CPU Speed:__ `{psutil.cpu_percent(4)} 🤓`
__Total RAM:__ `{str(psutil.virtual_memory().total)[0]} GB`
__Free Memory:__ `{int(100 - psutil.virtual_memory()[2])}%`
__Uptime:__ `{(datetime(1970,1,1) + timedelta(seconds=(time.time() - psutil.boot_time()))).time()} 🖕🏼`
"""
        
        pe = nextcord.Embed(title=f"**Backend Information**",description=info,color = green)
        await ctx.send('🏓 Pong!')
        await ctx.send(embed=pe)

    @ping.error
    async def inspire_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        em = nextcord.Embed(title=f"Woah Slow it down buckaroo!",description=f"Try again in **{error.retry_after:.2f}s**", color=0xe74c3c)
        await ctx.send(embed=em)
      else:
        emb = nextcord.Embed(title=f"Something went wrong!",description=f"Tell Moaz about this error if possible", color=0xe74c3c)
        await ctx.send(embed=emb)

def setup(client):
    client.add_cog(Ping(client))