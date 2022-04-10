import nextcord
from nextcord.ext import commands
from config import red,joinLeave
import datetime

class Leave(commands.Cog):
    def __init__(self, client): 
         self.client = client
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
      embedml=nextcord.Embed(title="GoodBye!", colour=red, description=f"**{member.name}** left the server. Everyone in this server hopes that this nigga gets run over by a truck.")
      embedml.set_thumbnail(url=f"{member.guild.icon}")
      embedml.set_author(name=f"{member.name}", icon_url=f"{member.avatar}")
      embedml.set_footer(text="Server owner is Reyan On Coke#2556")
      embedml.timestamp = datetime.datetime.utcnow()
      leave = self.client.get_channel(joinLeave)
      await leave.send(embed=embedml)


def setup(client):
    client.add_cog(Leave(client))