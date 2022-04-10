import nextcord
from nextcord.ext import commands
import asyncio
from api.joke import get_joke

class Joke(commands.Cog):
    def __init__(self, client):
         self.client = client
    
    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def joke(self, ctx):
        setup,punchline = get_joke()
        await ctx.send(setup)
        await asyncio.sleep(3)
        await ctx.send(punchline)

    @joke.error
    async def joke_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        em = nextcord.Embed(title=f"Woah Slow it down buckaroo!",description=f"Try again in **{error.retry_after:.2f}s**", color=0xe74c3c)
        await ctx.send(embed=em)
      else:
        emb = nextcord.Embed(title=f"Something went wrong!",description=f"Tell Moaz about this error if possible", color=0xe74c3c)
        await ctx.send(embed=emb)

def setup(client):
    client.add_cog(Joke(client))