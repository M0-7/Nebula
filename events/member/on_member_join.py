import nextcord
from nextcord.ext import commands
from config import blurple,joinLeave,white
import datetime

class Join(commands.Cog):
    def __init__(self, client): 
         self.client = client
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
      role = nextcord.utils.get(member.guild.roles, id=850279899989278741)
      brole = nextcord.utils.get(member.guild.roles, id=850315785133883433)
      pos = int(18)
    
      embedmr=nextcord.Embed(title="A New Member!", colour=blurple, description="Welcome to **Bois Empire 👑!** Get your roles at <#963100249864417331> , Make sure you check the <#850736448793083954> and <#881234365131161640> regularly!")
      embedmr.set_image(url="https://cdn.discordapp.com/attachments/649907682035367957/896620790634651679/Server_Banner.jpg")
      embedmr.set_thumbnail(url=f"{member.guild.icon}")
      embedmr.set_author(name=f"{member.name}", icon_url=f"{member.avatar}")
      embedmr.set_footer(text="Server owner is Reyan On Coke#2556")
      embedmr.timestamp = datetime.datetime.utcnow()
      if member.bot:
        roles = ""
        for role in member.roles:
            roles = nextcord.utils.get(member.guild.roles, id=role.id)
        await roles.edit(colour = white,position=pos)
        await member.add_roles(brole)
        target = self.client.get_channel(joinLeave)
        await target.send(embed=embedmr)
      else:
        await member.add_roles(role)
        target = self.client.get_channel(joinLeave)
        await target.send(embed=embedmr)

def setup(client):
    client.add_cog(Join(client))