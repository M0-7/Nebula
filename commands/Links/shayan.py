import nextcord
from nextcord.ext import commands
from nextcord import Interaction

url = "https://www.roblox.com/users/1895622949/profile"

class Roblox(nextcord.ui.View):
  def __init__(self):
    super().__init__(timeout=90)
    self.add_item(nextcord.ui.Button(style=nextcord.ButtonStyle.link,label="Open", url=url))

class Shayan(commands.Cog):
    def __init__(self, client): 
         self.client = client
    
    @nextcord.slash_command(name = "shayan")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def roblox(self, interaction:nextcord.Interaction):
        """Shayan's profile"""
        view = Roblox()
        await interaction.response.send_message(url,view=view)

    @roblox.error
    async def roblox_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        em = nextcord.Embed(title=f"Woah Slow it down buckaroo!",description=f"Try again in **{error.retry_after:.2f}s**", color=0xe74c3c)
        await ctx.send(embed=em)
      else:
        emb = nextcord.Embed(title=f"Something went wrong!",description=f"Tell Moaz about this error if possible", color=0xe74c3c)
        await ctx.send(embed=emb)

def setup(client):
    client.add_cog(Shayan(client))