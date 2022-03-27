import nextcord
from nextcord.ext import commands
from config import teal
import datetime

class Rl_create(commands.Cog):
    def __init__(self, client): 
         self.client = client
    
    @commands.Cog.listener()
    async def on_guild_role_create(self,role):
      embed = nextcord.Embed(title="Role created",description=(f"{role.mention}"),color=teal)
      embed.add_field(name="Color",value=(f"**{role.color}**"),inline=False)
      chan = self.client.get_channel(835037950777360404)
      embed.set_thumbnail(url=f"{role.guild.icon}")
      embed.timestamp = datetime.datetime.utcnow()
    
      await chan.send(embed=embed)

def setup(client):
    client.add_cog(Rl_create(client))