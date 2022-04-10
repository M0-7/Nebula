import nextcord
from nextcord.ext import commands
import random
import typing
import asyncio
from Assets.hi import hello_statements,hello_replies
from Assets.bye import bye_replies,bye_statements

class Messager(commands.Cog):
    def __init__(self, client): 
      self.client = client
      self._cd = commands.CooldownMapping.from_cooldown(1,20, commands.BucketType.member)

    def get_ratelimit(self, message: nextcord.Message) -> typing.Optional[int]:
      """Returns the ratelimit left"""
      bucket = self._cd.get_bucket(message)
      return bucket.update_rate_limit()
    
    @commands.Cog.listener()
    async def on_message(self, message):
      if "check something":
        ratelimit = self.get_ratelimit(message)
        if ratelimit is None:
          if message.author.bot:
            return
          if any(word in message.content for word in hello_statements):
            async with message.channel.typing():
              await asyncio.sleep(0.5)
            await message.channel.send(random.choice(hello_replies))
       
          if message.content == "hi":
            async with message.channel.typing():
              await asyncio.sleep(0.5)
            await message.channel.send(random.choice(hello_replies))

          if message.content == "sup":
            async with message.channel.typing():
              await asyncio.sleep(0.5)
            await message.channel.send(random.choice(hello_replies))

          if any(word in message.content for word in (bye_statements)):
            async with message.channel.typing():
              await asyncio.sleep(0.5)
            await message.channel.send(random.choice(bye_replies))

def setup(client):
    client.add_cog(Messager(client))