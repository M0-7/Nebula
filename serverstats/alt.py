import nextcord
from nextcord.ext import commands,tasks

class All_alt(commands.Cog):
    def __init__(self, client): 
         self.client = client
         
         self.checkalt.start()
    
    @tasks.loop(seconds=70.0)
    async def checkalt(self):
      await self.client.wait_until_ready()
      old_amount = "2"
      guilds = self.client.get_guild(833931478298918923)
      role_alt = guilds.get_role(855407744748224522)
      role_count = len(role_alt.members)
      if old_amount != role_count:
        old_amount = role_count
        target = self.client.get_channel(855408883626672148)
        await target.edit(name=(f"👥・Alts: {role_count}"))

def setup(client):
  client.add_cog(All_alt(client))