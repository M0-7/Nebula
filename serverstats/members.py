import nextcord
from nextcord.ext import commands,tasks

class Only_memb(commands.Cog):
    def __init__(self, client): 
         self.client = client
         
         self.checkmembers.start()
    
    @tasks.loop(seconds=70.0)
    async def checkmembers(self):
      await self.client.wait_until_ready()
      old_amount = "2"
      guilds = self.client.get_guild(833931478298918923)
      true_member_count = len([m for m in guilds.members if not m.bot])
      if old_amount != true_member_count:
        old_amount = true_member_count
        target = self.client.get_channel(850316483850666015)
        await target.edit(name=(f"👀・Members: {true_member_count}"))

def setup(client):
  client.add_cog(Only_memb(client))