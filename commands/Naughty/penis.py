import nextcord
from nextcord.ext import commands
from config import green
from nextcord import Interaction
import random

class Penis(commands.Cog):
    def __init__(self, client): 
         self.client = client
    
    @nextcord.slash_command(name = 'penis')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def penis(self, interaction:nextcord.Interaction):
        """Find out how long your shalonga balonga is"""
        rank = random.randint(1,10)
        penis = "="
        ema = nextcord.Embed(description=(f"Your penis 8{penis*rank}D, {rank} inches"),color=green)
        await interaction.response.send_message(embed=ema)

    @penis.error
    async def penis_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        em = nextcord.Embed(title=f"Woah Slow it down buckaroo!",description=f"Try again in **{error.retry_after:.2f}s**", color=0xe74c3c)
        await ctx.send(embed=em)
      else:
        emb = nextcord.Embed(title=f"Something went wrong!",description=f"Tell Moaz about this error if possible", color=0xe74c3c)
        await ctx.send(embed=emb)

def setup(client):
    client.add_cog(Penis(client))