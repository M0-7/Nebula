import nextcord
from nextcord.ext import commands
from nextcord import Interaction

url = "https://disqus.com/by/disqus_3jpJF1dk1P"

class Disqus(nextcord.ui.View):
  def __init__(self):
    super().__init__(timeout=90)
    self.add_item(nextcord.ui.Button(style=nextcord.ButtonStyle.link,label="Open", url=url))

class Reyan(commands.Cog):
    def __init__(self, client):
         self.client = client

    @nextcord.slash_command(name = "reyan")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def reyan(self, interaction:nextcord.Interaction):
        """Reyan's profile"""
        view=Disqus()
        await interaction.response.send_message(url,view=view)

    @reyan.error
    async def reyan_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        em = nextcord.Embed(title=f"Woah Slow it down buckaroo!",description=f"Try again in **{error.retry_after:.2f}s**", color=0xe74c3c)
        await ctx.send(embed=em)
      else:
        emb = nextcord.Embed(title=f"Something went wrong!",description=f"Tell Moaz about this error if possible", color=0xe74c3c)
        await ctx.send(embed=emb)

def setup(client):
    client.add_cog(Reyan(client))