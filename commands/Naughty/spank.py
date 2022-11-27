import nextcord
from nextcord.ext import commands
from config import green,spank_gif
from nextcord import SlashOption,Interaction

class Spank(commands.Cog):
    def __init__(self, client): 
         self.client = client
    
    @nextcord.slash_command(name = 'spank')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def spank(self, interaction:nextcord.Interaction,arg:str = SlashOption(description="Who is it")):
      """Hits someone in the ass"""
      embed = nextcord.Embed(description=(f"{interaction.user.mention} *spanks* {arg} 😏"),color=green)
      embed.set_image(url=spank_gif)
      await interaction.response.send_message(embed=embed)

    @spank.error
    async def spank_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        em = nextcord.Embed(title=f"Woah Slow it down buckaroo!",description=f"Try again in **{error.retry_after:.2f}s**", color=0xe74c3c)
        await ctx.send(embed=em)
      elif isinstance(error,commands.MissingRequiredArgument):
        er = nextcord.Embed(title="Missing Argument",description=f"Missing a required argument: {error.param}",color=0xe74c3c)
        await ctx.send(embed=er)
      else:
        emb = nextcord.Embed(title=f"Something went wrong!",description=f"Tell Moaz about this error if possible", color=0xe74c3c)
        await ctx.send(embed=emb)
        
def setup(client):
    client.add_cog(Spank(client))