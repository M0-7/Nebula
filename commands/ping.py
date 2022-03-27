import nextcord
from nextcord.ext import commands
from config import green

class Ping(commands.Cog):
    def __init__(self, client): 
         self.client = client
    
    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def ping(self, ctx):
        pe = nextcord.Embed(description=(f"🏓 Pong! {round(self.client.latency * 1000)}ms 📈"),color = green)
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