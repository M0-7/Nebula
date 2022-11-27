import nextcord
from nextcord.ext import commands
from config import blurple,joinLeave,white,chatchannel,announcement,bot_role,member_role,join_img
import datetime

class Join(commands.Cog):
    def __init__(self, client): 
         self.client = client
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
      role = nextcord.utils.get(member.guild.roles, id=member_role)
      brole = nextcord.utils.get(member.guild.roles, id=bot_role)

      #Creates the embed
      embedmr=nextcord.Embed(title="A New Member!", colour=blurple, description=f"Welcome to **Soul Society 👹!**; Start waffling at <#{chatchannel}> and make sure to check <#{announcement}> regularly!!!")
      embedmr.set_image(url=join_img)
      embedmr.set_thumbnail(url=f"{member.guild.icon}")
      embedmr.set_author(name=f"{member.name}", icon_url=f"{member.avatar}")
      embedmr.set_footer(text="Owned by soul society")
      embedmr.timestamp = datetime.datetime.utcnow()

      #Checks if the member is bot or not
      if member.bot:
        for role in member.roles:
            roles = nextcord.utils.get(member.guild.roles, id=role.id)
        await roles.edit(colour = white)
        await member.add_roles(brole)
        target = self.client.get_channel(joinLeave)
        await target.send(embed=embedmr)
      else:
        await member.add_roles(role)
        target = self.client.get_channel(joinLeave)
        await target.send(embed=embedmr)

def setup(client):
    client.add_cog(Join(client))
