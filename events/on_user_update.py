import nextcord
from nextcord.ext import commands
from config import blue
import datetime

class User(commands.Cog):
    def __init__(self, client): 
         self.client = client
    
    @commands.Cog.listener()
    async def on_user_update(self, before,after):
      if before.name != after.name:
        emkr = nextcord.Embed(title="Username update",description=(f"""
    **Before: **{before.name}
**+After: **{after.name}"""),color=blue)
        emkr.set_thumbnail(url=before.avatar)
        emkr.set_author(name =f"{before.name}",icon_url=f"{before.avatar}")
        emkr.timestamp = datetime.datetime.utcnow()
        user = self.client.get_channel(898787267034902549)
        await user.send(embed=emkr)
        

      elif before.discriminator != after.discriminator:
        emsh = nextcord.Embed(title="Discriminator update",description=(f"""
    **Before: **{before.name}#{before.discriminator}
**+After: **{after.name}#{after.discriminator}"""),color=blue)
        emsh.set_thumbnail(url=before.avatar)
        emsh.set_author(name =f"{before.name}",icon_url=f"{before.avatar}")
        emsh.timestamp = datetime.datetime.utcnow()
        user = self.client.get_channel(898787267034902549)
        await user.send(embed=emsh)

      elif before.avatar != after.avatar:
        if before.name == "Aki":
          return
        eml = nextcord.Embed(title="Avatar update",color=blue)
        eml.set_thumbnail(url=after.avatar)
        eml.set_author(name =f"{before.name}",icon_url=f"{before.avatar}")
        eml.timestamp = datetime.datetime.utcnow()
        user = self.client.get_channel(898787267034902549)
        await user.send(embed=eml)
        
def setup(client):
    client.add_cog(User(client))