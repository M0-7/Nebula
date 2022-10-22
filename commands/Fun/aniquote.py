from nextcord import SlashOption,Interaction
import nextcord
from nextcord.ext import commands
from api.aniquote import character,quote
from config import green

class Aniquote(commands.Cog):
    def __init__(self, client): 
         self.client = client
    
    @nextcord.slash_command(name = 'aniquote')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def aniquote(self, interaction: nextcord.Interaction):
      """Sends an anime quote"""
      embed=nextcord.Embed(description=(f"**{quote}**"),color=green)
      embed.set_footer(text=f"~{character}")
      await interaction.response.send_message(embed=embed)

    @aniquote.error
    async def aniquote_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        em = nextcord.Embed(title=f"Woah Slow it down buckaroo!",description=f"Try again in **{error.retry_after:.2f}s**", color=0xe74c3c)
        await ctx.send(embed=em)
      else:
        emb = nextcord.Embed(title=f"Something went wrong!",description=f"Tell Moaz about this error if possible", color=0xe74c3c)
        await ctx.send(embed=emb)

def setup(client):
    client.add_cog(Aniquote(client)) 