import nextcord
from nextcord.ext import commands
from config import red,serverlogs
import datetime

class Ch_delete(commands.Cog):
    def __init__(self, client): 
         self.client = client
    
    @commands.Cog.listener()
    async def on_guild_channel_delete(self,channel):
      embed = nextcord.Embed(title="Channel Deleted",description=(f"#{channel.name}"),color=red)
      target = self.client.get_channel(serverlogs)
      embed.set_thumbnail(url=f"{channel.guild.icon}")
      embed.timestamp = datetime.datetime.utcnow()
    
      await target.send(embed=embed)

def setup(client):
    client.add_cog(Ch_delete(client))