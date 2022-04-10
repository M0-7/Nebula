import nextcord
from nextcord.ext import commands
from config import red,userlogs
import datetime

class Ban(commands.Cog):
    def __init__(self, client): 
         self.client = client
    
    @commands.Cog.listener()
    async def on_member_ban(self,guild,user):
      embeder = nextcord.Embed(title=f"Member Banned", description=f"{user.name}",color=red)
      embeder.set_author(name=f"{user.name}",icon_url=f"{user.avatar}")
      embeder.timestamp = datetime.datetime.utcnow()
      embeder.set_thumbnail(url=f"{guild.icon}")
      target = self.client.get_channel(userlogs)
      await target.send(embed=embeder)


def setup(client):
    client.add_cog(Ban(client))