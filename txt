import nextcord
from nextcord.ext import commands
msg = []

class Purge(commands.Cog):
    def __init__(self, client): 
         self.client = client
    
    @commands.command(pass_context=True, aliases = ['purge'])
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount:int,purmember: nextcord.Member=None,):
      amount = amount + 1 
      if amount > 1500:
        return await ctx.send("You cant purge more than 1500 messages")
      eif not purmember:
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"Purged {amount-1} messages by {ctx.author.mention}",delete_after=3)
      elif async for m in ctx.channel.history():
        if len(msg) == amount:
          break
        if m.author == member:
          msg.append(m)
        await ctx.channel.delete_messages(msg)
        await ctx.send(f"Purged {amount-1} messages of {member.mention}", delete_after=3)


    @clear.error
    async def purge_error(ctx, error):
      if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")

def setup(client):
    client.add_cog(Purge(client))