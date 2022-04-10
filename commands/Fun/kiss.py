import nextcord
from nextcord.ext import commands
from config import green

kiss_gif = "https://media.giphy.com/media/LJOW8CJOpyjeybrxhb/giphy.gif"

class Kiss(commands.Cog):
    def __init__(self, client): 
         self.client = client
    
    @commands.command(name = 'kiss')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def kiss(self, ctx,Member):
      embed = nextcord.Embed(description=(f"{ctx.author.mention} *kisses* {Member} 😘  "),colour=green)
      embed.set_image(url=kiss_gif)
      await ctx.send(embed=embed)

    @kiss.error
    async def kiss_error(self, ctx, error):
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
    client.add_cog(Kiss(client))