import nextcord
from nextcord import Interaction
from nextcord.ext import commands

url = "https://www.instagram.com/bilal_amin123/"

class Insta(nextcord.ui.View):
  def __init__(self):
    super().__init__(timeout=90)
    self.add_item(nextcord.ui.Button(style=nextcord.ButtonStyle.link,label="Open", url=url))


class Bilal(commands.Cog):
    def __init__(self, client): 
         self.client = client
    
    @nextcord.slash_command(name = "bilal")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def bilal(self,interaction:nextcord.Interaction):
        """Bilal's profile"""
        view = Insta()
        await interaction.response.send_message(url,view=view)

    @bilal.error
    async def bilal_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        em = nextcord.Embed(title=f"Woah Slow it down buckaroo!",description=f"Try again in **{error.retry_after:.2f}s**", color=0xe74c3c)
        await ctx.send(embed=em)
      else:
        emb = nextcord.Embed(title=f"Something went wrong!",description=f"Tell Moaz about this error if possible", color=0xe74c3c)
        await ctx.send(embed=emb)

def setup(client):
    client.add_cog(Bilal(client))