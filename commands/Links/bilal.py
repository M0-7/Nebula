import nextcord
from nextcord.ext import commands

class Bilal(commands.Cog):
    def __init__(self, client): 
         self.client = client
    
    @commands.command(name = "bilal")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def bilal(self,ctx):
        await ctx.send("""Here is Bilal´s instagram account:
https://www.instagram.com/bilal_amin123/""")

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