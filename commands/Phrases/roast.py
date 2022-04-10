import nextcord
from nextcord.ext import commands
import random
from Assets.roasts import roasts

class Roast(commands.Cog):
    def __init__(self, client): 
         self.client = client
    
    @commands.command(name = 'roast')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def roast(self, ctx):
        await ctx.message.delete()
        await ctx.send(random.choice(roasts))

    @roast.error
    async def roast_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        em = nextcord.Embed(title=f"Woah Slow it down buckaroo!",description=f"Try again in **{error.retry_after:.2f}s**", color=0xe74c3c)
        await ctx.send(embed=em)
      else:
        emb = nextcord.Embed(title=f"Something went wrong!",description=f"Tell Moaz about this error if possible", color=0xe74c3c)
        await ctx.send(embed=emb)

def setup(client):
    client.add_cog(Roast(client))