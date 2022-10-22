import nextcord
from nextcord import Interaction
from nextcord.ext import commands

class Moaz(commands.Cog):
    def __init__(self, client): 
         self.client = client
    
    @nextcord.slash_command(name="moaz")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def moaz(self, interaction:nextcord.Interaction):
        """My profile"""
        await interaction.response.send_message("https://moazlion.repl.co")

    @moaz.error
    async def moaz_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        em = nextcord.Embed(title=f"Woah Slow it down buckaroo!",description=f"Try again in **{error.retry_after:.2f}s**", color=0xe74c3c)
        await ctx.send(embed=em)
      else:
        emb = nextcord.Embed(title=f"Something went wrong!",description=f"Tell Moaz about this error if possible", color=0xe74c3c)
        await ctx.send(embed=emb)

def setup(client):
    client.add_cog(Moaz(client))