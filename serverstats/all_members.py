import nextcord
from nextcord.ext import commands,tasks

class All_memb(commands.Cog):
    def __init__(self, client): 
         self.client = client
         
         self.checkallmembers.start()
    
    @tasks.loop(seconds=70.0)
    async def checkallmembers(self):
      await self.client.wait_until_ready()
      old_amount = "2"
      guilds = self.client.get_guild(833931478298918923)
      members_count = len(guilds.members)
      if old_amount != members_count:
        old_amount = members_count
        target = self.client.get_channel(850316481391624202)
        await target.edit(name=(f"👁・All Members: {members_count}"))

def setup(client):
  client.add_cog(All_memb(client))