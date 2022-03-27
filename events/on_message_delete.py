import nextcord
from nextcord.ext import commands
from config import teal
import datetime

class Delete(commands.Cog):
    def __init__(self, client): 
         self.client = client
    
    @commands.Cog.listener()
    async def on_message_delete(self, message):
      if message.author.bot:
        return
      embeder = nextcord.Embed(title=f"Message deleted in #{message.channel}",description=f"{message.content}",color=teal)
      embeder.set_author(name=f"{message.author.name}",icon_url=f"{message.author.avatar}")
      embeder.timestamp = datetime.datetime.utcnow()
      target = self.client.get_channel(878668000314654750)
      await target.send(embed=embeder)


def setup(client):
    client.add_cog(Delete(client))