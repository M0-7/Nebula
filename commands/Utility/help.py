import nextcord
from nextcord.ext import commands
from config import green
import datetime

help_image = "https://media.discordapp.net/attachments/870316216571543552/927992961646616636/IMG_2763.jpg"

class Help(commands.Cog): 
    def __init__(self, client): 
         self.client = client
    
    @commands.command(name = "help")
    @commands.cooldown(1, 10, commands.BucketType.guild)
    async def help(self,ctx):
      ehelp=nextcord.Embed(title="**Mai Commands**", description="__Boku Wa Tobi__ **:)**", color=green)
      ehelp.set_footer(text="For more help dm Moaz#3688", icon_url=f"{ctx.author.avatar}")
      ehelp.set_image(url=help_image)
      ehelp.add_field(name="📚 **Phrases[4]**",value="`!aniquote`, `!quote`, `!joke`, `!roast`", inline=False)
      ehelp.add_field(name="😊 **Fun[5]**", value="`!hug`, `!kiss`, `!8ball`, `!meme`, `!#1`", inline=False)
      ehelp.add_field(name="😏 **Naughty[5]**", value="`!penis`, `!gtest` , `!rate`, `!spank`, `!#69`", inline=False)
      ehelp.add_field(name="🔗 **Links[5]**", value="`!moaz`, `!reyan`, `!bilal`, `!shayan`, `!avatar`", inline=False)
      ehelp.add_field(name="🧩 **Utility[4]**", value="`!ping`, `!lock`, `!unlock`, `!help`")
      ehelp.timestamp = datetime.datetime.utcnow()
      ehelp.set_thumbnail(url=ctx.guild.icon)
      await ctx.send(embed=ehelp)

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