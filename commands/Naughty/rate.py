import nextcord
from nextcord.ext import commands
from config import green
from nextcord import SlashOption,Interaction
import random

class Rate(commands.Cog):
    def __init__(self, client): 
         self.client = client
    
    @nextcord.slash_command(name = 'rate')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def rate(self, interaction:nextcord.Interaction, arg:str = SlashOption(description="WHat thing is it")):
        """Rates your waifu to settle the long debate"""
        rating = random.randint(1,10)
        emk = nextcord.Embed(description=(f"M'Lord {arg} is rated {rating}/10 👍"),color=green)
        await interaction.response.send_message(embed=emk)

    @rate.error
    async def rate_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        em = nextcord.Embed(title=f"Woah Slow it down buckaroo!",description=f"Try again in **{error.retry_after:.2f}s**", color=0xe74c3c)
        await ctx.send(embed=em)
      else:
        emb = nextcord.Embed(title=f"Something went wrong!",description=f"Tell Moaz about this error if possible", color=0xe74c3c)
        await ctx.send(embed=emb)

def setup(client):
    client.add_cog(Rate(client))