import nextcord
from nextcord.ext import commands,tasks

class Only_bots(commands.Cog):
    def __init__(self, client): 
      self.client = client
      self.checkbots.start()
      
    @tasks.loop(seconds=70.0)
    async def checkbots(self):
      await self.client.wait_until_ready()
      old_amount = "2"
      guilds = self.client.get_guild(833931478298918923)
      role_bot = guilds.get_role(850315785133883433)
      true_bot_count = len(role_bot.members)
      if old_amount != true_bot_count:
        old_amount = true_bot_count
        target = self.client.get_channel(850316487095877682)
        await target.edit(name=(f"🤖・Bots: {true_bot_count}"))

def setup(client):
  client.add_cog(Only_bots(client))