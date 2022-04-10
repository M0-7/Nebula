import nextcord
from nextcord.ext import commands
from config import green
import random
from Assets.enemy import locations

class Enemy(commands.Cog):
    def __init__(self, client): 
         self.client = client
    
    @commands.command(name = '#1')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def enemy(self, ctx):
        location = random.choice(locations)
        emk = nextcord.Embed(description=(f"Your public enemy number #1 is in {location}"),color=green)
        await ctx.send(embed=emk)

    @enemy.error
    async def enemy_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        em = nextcord.Embed(title=f"Woah Slow it down buckaroo!",description=f"Try again in **{error.retry_after:.2f}s**", color=0xe74c3c)
        await ctx.send(embed=em)
      else:
        emb = nextcord.Embed(title=f"Something went wrong!",description=f"Tell Moaz about this error if possible", color=0xe74c3c)
        await ctx.send(embed=emb)

def setup(client):
    client.add_cog(Enemy(client))