import nextcord
from nextcord.ext import commands
from config import green,help_img
import datetime

class Help(commands.Cog): 
    def __init__(self, client): 
         self.client = client
    
    @nextcord.slash_command(name = "help")
    @commands.cooldown(1, 10, commands.BucketType.guild)
    async def help(self, interaction: nextcord.Interaction):
      """Shows the commands for the bot"""
      ehelp=nextcord.Embed(title="**Nebula Commands**",description="__Boku Wa Tobi__ **:)**", color=green)
      ehelp.set_image(url=help_img)
      ehelp.add_field(name="😊 **Fun[4]**", value="`aniquote`, `hug`, `kiss`, `8ball`", inline=False)
      ehelp.add_field(name="😏 **Naughty[4]**", value="`penis`, `gtest` , `rate`, `spank`", inline=False)
      ehelp.add_field(name="🧩 **Utility[6]**", value="`ping`, `lock`, `unlock`, `help`, `avatar`, `restart`", inline=False)
      ehelp.timestamp = datetime.datetime.utcnow()
      ehelp.set_thumbnail(url=interaction.guild.icon)
      await interaction.response.send_message(embed=ehelp)

    @help.error
    async def help_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        em = nextcord.Embed(title=f"Woah Slow it down buckaroo!",description=f"Try again in **{error.retry_after:.2f}s**", color=0xe74c3c)
        await ctx.send(embed=em)
      else:
        emb = nextcord.Embed(title=f"Something went wrong!",description=f"Tell Moaz about this error if possible", color=0xe74c3c)
        await ctx.send(embed=emb)
    

def setup(client):
    client.add_cog(Help(client))