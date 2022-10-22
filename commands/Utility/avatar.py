import nextcord
from nextcord.ext import commands
from config import green

class Avatars(commands.Cog):
    def __init__(self, client): 
         self.client = client
    
    @commands.command(name = "avatar")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def avatar(self,ctx,*,avamember:nextcord.Member=None):
      """Returns the avatar of the user"""
      pfp = avamember.avatar
      embed = nextcord.Embed(title=f"Avatar of {avamember}",color=green)
      embed.set_image(url=pfp)
      await ctx.send(embed=embed)

    @avatar.error
    async def avatar_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        em = nextcord.Embed(title=f"Woah Slow it down buckaroo!",description=f"Try again in **{error.retry_after:.2f}s**", color=0xe74c3c)
        await ctx.send(embed=em)
      else:
        emb = nextcord.Embed(title=f"Missing Argument",description=f"Mention a user for the avatar command", color=0xe74c3c)
        emb.set_footer(text="If error persists tell Moaz")
        await ctx.send(embed=emb)
    
def setup(client):
    client.add_cog(Avatars(client))