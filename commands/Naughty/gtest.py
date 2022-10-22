import nextcord
from nextcord.ext import commands
from config import green
from nextcord import Interaction
import random

class Gtest(commands.Cog):
    def __init__(self, client): 
         self.client = client
    
    @nextcord.slash_command(name = "gtest")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def gtest(self, interaction:nextcord.Interaction):
        """Test how much of a faggot you are"""
        number = random.randint(1,100)
        em = nextcord.Embed(description=(f"You are {number}% gay 🏳️‍🌈"),color=green)
        await interaction.response.send_message(embed=em)

    @gtest.error
    async def gtest_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        em = nextcord.Embed(title=f"Woah Slow it down buckaroo!",description=f"Try again in **{error.retry_after:.2f}s**", color=0xe74c3c)
        await ctx.send(embed=em)
      else:
        emb = nextcord.Embed(title=f"Something went wrong!",description=f"Tell Moaz about this error if possible", color=0xe74c3c)
        await ctx.send(embed=emb)

def setup(client):
    client.add_cog(Gtest(client))