import nextcord
from nextcord.ext import commands
from config import red
import datetime

class Ch_delete(commands.Cog):
    def __init__(self, client): 
         self.client = client
    
    @commands.Cog.listener()
    async def on_guild_channel_delete(self,channel):
      embed = nextcord.Embed(title="Channel Deleted",description=(f"#{channel.name}"),color=red)
      chan = self.client.get_channel(835037950777360404)
      embed.set_thumbnail(url=f"{channel.guild.icon}")
      embed.timestamp = datetime.datetime.utcnow()
    
      await chan.send(embed=embed)

def setup(client):
    client.add_cog(Ch_delete(client))