import nextcord
from nextcord.ext import commands
from config import dark_red,serverlogs
import datetime

class Rl_delete(commands.Cog):
    def __init__(self, client): 
         self.client = client
    
    @commands.Cog.listener()
    async def on_guild_role_delete(self,role):
      embed = nextcord.Embed(title="Role Deleted",description=(f"@{role.name}"),color=dark_red)
      embed.add_field(name="Color",value=(f"**{role.color}**"),inline=False)
      chan = self.client.get_channel(serverlogs)
      embed.set_thumbnail(url=f"{role.guild.icon}")
      embed.timestamp = datetime.datetime.utcnow()
    
      await chan.send(embed=embed)

def setup(client):
    client.add_cog(Rl_delete(client))