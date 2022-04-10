import nextcord
from nextcord.ext import commands,tasks

class All_main(commands.Cog):
    def __init__(self, client):
      self.client = client
      self.checkmains.start()
         
    @tasks.loop(seconds=70.0)
    async def checkmains(self):
      await self.client.wait_until_ready()
      old_amnt = "5"
      guilds = self.client.get_guild(833931478298918923)
      role_main = guilds.get_role(875582281769701447)
      role_count = len(role_main.members)
      if old_amnt != role_count:
        old_amnt = role_count
        target = self.client.get_channel(875634241881391115)
        await target.edit(name=(f"👤・Mains: {role_count}"))

def setup(client):
  client.add_cog(All_main(client))