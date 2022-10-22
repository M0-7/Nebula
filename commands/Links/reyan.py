import nextcord
from nextcord.ext import commands

class Reyan(commands.Cog):
    def __init__(self, client):
         self.client = client

    @commands.command(name = "reyan")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def reyan(self, ctx):
        """Reyan's profile"""
        await ctx.send("""Here is Reyan's disqus account link used for commenting under anime episodes:
https://disqus.com/by/disqus_3jpJF1dk1P""")

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