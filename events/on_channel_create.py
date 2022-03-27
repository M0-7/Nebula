import nextcord
from nextcord.ext import commands
from config import teal
import datetime

class Ch_create(commands.Cog):
    def __init__(self, client): 
         self.client = client
    
    @commands.Cog.listener()
    async def on_guild_channel_create(self,channel):
      embed = nextcord.Embed(title="Channel Created",description=(f"{channel.mention}"),color=teal)
      chan = self.client.get_channel(835037950777360404)
      embed.set_thumbnail(url=f"{channel.guild.icon}")
      embed.timestamp = datetime.datetime.utcnow()
    
      await chan.send(embed=embed)

def setup(client):
    client.add_cog(Ch_create(client))