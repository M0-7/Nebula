import nextcord
from nextcord.ext import commands
from config import green

class Unilock(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @nextcord.ui.button(label="Unlock", style=nextcord.ButtonStyle.red)
    async def confirm(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        drole = nextcord.utils.get(ctx.guild.roles, name = 'Sasta Sherlock')
        await ctx.channel.set_permissions(drole, view_channel=True)
        await interaction.response.send_message("Channel unlocked, Shanny aka 🤡 can see you! Be careful out there.", ephemeral=True)
        self.value = True
        self.stop()

class Lock(commands.Cog):
    def __init__(self, client): 
         self.client = client
    
    @commands.command(name = 'lock')
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def lock(self, ctx):
        drole = nextcord.utils.get(ctx.guild.roles, name = 'Sasta Sherlock')
        await ctx.channel.set_permissions(drole, view_channel=False)
        embed = nextcord.Embed(title="Channel locked",description="Do *!unlock* to open the channel again or press the damn button below!",color = green)
        view=Unilock()
        msg = await ctx.send(embed=embed,view=view)
        await view.wait()
        await ctx.message.delete()
        await msg.delete()
        
    @lock.error
    async def lock_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        em = nextcord.Embed(title=f"Woah Slow it down buckaroo!",description=f"Try again in **{error.retry_after:.2f}s**", color=0xe74c3c)
        await ctx.send(embed=em)
      elif isinstance(error, commands.MissingPermissions):
        em = nextcord.Embed(title=f"Missing Perms",description=f"Change this in the channel or server", color=0xe74c3c)
        await ctx.send(embed=em)
      else:
        emb = nextcord.Embed(title=f"Something went wrong!",description=f"Tell Moaz about this error if possible", color=0xe74c3c)
        await ctx.send(embed=emb)

def setup(client):
    client.add_cog(Lock(client))
