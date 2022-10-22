import nextcord
from nextcord import SlashOption,Interaction
from nextcord.ext import commands
from config import green

hug_gif = "https://media.giphy.com/media/SZ9PmtBJL2VRGvau1m/giphy.gif"

class Hug(commands.Cog):
    def __init__(self, client): 
         self.client = client
      
    @nextcord.slash_command(name = "hug")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def hug(self, interaction: nextcord.Interaction,arg: str = SlashOption(description="Add a person")):
        """Aww your feeling lonely?"""
        embed = nextcord.Embed(description=(f"{interaction.user.mention} *hugs* {arg} 🤗 "),colour=green)
        embed.set_image(url=hug_gif)
        await interaction.response.send_message(embed=embed)

    @hug.error
    async def hug_error(self, ctx, error):
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
    client.add_cog(Hug(client))