import nextcord
from nextcord.ext import commands
from config import gold,userlogs
import datetime
import asyncio

cooldown = []
calldown = []

class Member(commands.Cog):
    def __init__(self, client): 
         self.client = client
    
    @commands.Cog.listener()
    async def on_member_update(self,before,after):
      if before.display_name != after.display_name:
        emb = nextcord.Embed(title="Nickname Updated",color=gold,description=f"""
    **Before: **{before.display_name}
**+After: **{after.display_name}""")
        emb.set_author(name = f"{before.name}",icon_url=f"{before.avatar}")
        emb.set_thumbnail(url=f"{before.guild.icon}")
        emb.timestamp = datetime.datetime.utcnow()
        user = self.client.get_channel(userlogs)
        await user.send(embed=emb)

############ROLE
      if len(before.roles) < len(after.roles):
        global cooldown
        if before in cooldown:
          return
        cooldown.append(before)
        await asyncio.sleep(15)
        cooldown.remove(before)
        emb = nextcord.Embed(description=f'**Role updated of - {before.mention}**', colour=gold)
        emb.set_thumbnail(url=before.guild.icon)
        emb.set_author(name =f"{before.name}",icon_url=f"{before.avatar}")
        emb.timestamp = datetime.datetime.utcnow()
        changed_roles = []
        for role in before.roles:
          if role in after.roles:
            pass
          else:
            changed_roles.append(role)

        for role in after.roles:
          if role in before.roles:
            pass
          else:
            if role in changed_roles:
              pass
            else:
              changed_roles.append(role)

        text = "_ _"
        blacklist=[850294117010636820] 
        for role in changed_roles:
          if role.id in blacklist:
            return
          text = text + role.mention
        emb.add_field(name="Added roles", value=text, inline=False)
        async for event in before.guild.audit_logs(limit=1, action=nextcord.AuditLogAction.member_role_update):
          if getattr(event.target, "id", None) != before.id:
            continue
          break
        
        channel = self.client.get_channel(userlogs)
        await channel.send(embed=emb)

      if len(before.roles) > len(after.roles):
        global calldown
        if before in calldown:
          return
        calldown.append(before)
        await asyncio.sleep(15)
        calldown.remove(before)
        emi = nextcord.Embed(description=f'**Role updated of - {before.mention}**', colour=gold)
        emi.set_thumbnail(url=before.guild.icon)
        emi.set_author(name =f"{before.name}",icon_url=f"{before.avatar}")
        emi.timestamp = datetime.datetime.utcnow()
        changed_roles = []
        for role in before.roles:
          if role in after.roles:
            pass
          else:
            changed_roles.append(role)

        for role in after.roles:
          if role in before.roles:
            pass
          else:
            if role in changed_roles:
              pass
            else:
              changed_roles.append(role)

        text = "_ _"
        blacklist=[850294117010636820] 
        for role in changed_roles:
          if role.id in blacklist:
            return
          text = text + role.mention
        emi.add_field(name="Removed roles", value=text, inline=False)
        async for event in before.guild.audit_logs(limit=1, action=nextcord.AuditLogAction.member_role_update):
          if getattr(event.target, "id", None) != before.id:
            continue
          break
        
        channel = self.client.get_channel(userlogs)
        await channel.send(embed=emi)


def setup(client):
    client.add_cog(Member(client))