import nextcord
from nextcord.ext import commands
import datetime
from config import teal,msglogs

class Edit(commands.Cog):
    def __init__(self, client):
         self.client = client
      
    @commands.Cog.listener()
    async def on_message_edit(self, message_before,message_after):
      #Removes bot from logs
      if message_before.author.bot:
        return
      embedk = nextcord.Embed(title=f"Message edited in #{message_before.channel}",description=f"""
    **Before: **{message_before.content}
**+After: **{message_after.content}""",color=teal)
      embedk.set_author(name=f'{message_before.author.name}',icon_url=message_before.author.avatar)
      embedk.timestamp = datetime.datetime.utcnow()
      target = self.client.get_channel(msglogs)
      await target.send(embed=embedk)

def setup(client):
    client.add_cog(Edit(client))