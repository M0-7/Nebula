import nextcord
from nextcord.ext import commands
from config import green
import os,sys

class Restart(commands.Cog):
    def __init__(self, client): 
         self.client = client
    
    @commands.command(name = 'restart')
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def restart(self, ctx):
        embed = nextcord.Embed(title="Restarting myself ⏳",description="Give  me a couple of seconds :).<#870316216571543552> for status.",color = green)
        await ctx.send(embed=embed)
        os.system("clear")
        os.execv(sys.executable, ['python'] + sys.argv)
        
        
    @restart.error
    async def restart_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        em = nextcord.Embed(title=f"Woah Slow it down buckaroo!",description=f"Try again in **{error.retry_after:.2f}s**", color=0xe74c3c)
        await ctx.send(embed=em)
      elif isinstance(error, commands.MissingPermissions):
        em = nextcord.Embed(title=f"Missing Perms",description=f"You arent allowed to do this", color=0xe74c3c)
        await ctx.send(embed=em)
      else:
        emb = nextcord.Embed(title=f"Something went wrong!",description=f"Tell Moaz about this error if possible", color=0xe74c3c)
        await ctx.send(embed=emb)

def setup(client):
    client.add_cog(Restart(client))